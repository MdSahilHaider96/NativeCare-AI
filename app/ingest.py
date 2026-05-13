# This script will ingest the documents in the data folder and store them in the vector database
import os
import time
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

# Load environment variables from .env
load_dotenv()

def build_nativecare_db():
    # 1. Setup Folders
    data_folder = "./data"
    db_folder = "./db/nativecare_db"
    
    print("Loading documents from data directory...")

    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
        print(f"Created {data_folder} folder. Please put your PDFs there!")
        return

    # 2. Load PDFs
    all_docs = []
    for filename in os.listdir(data_folder):
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(data_folder, filename)) 
            all_docs.extend(loader.load()) # take all the pages from pdf into one big list of data
    
    if not all_docs:
        print("No PDFs found in the data folder. Ingestion aborted.")
        return

    # 3. Chunking logic
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200) 
    splits = text_splitter.split_documents(all_docs)
    print(f"Created {len(splits)} text chunks.")

    # 4. Create Embeddings (convert text into a long list of numbers (a Vector)
    embeddings_model = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-2",
        task_type="retrieval_document"
    )
    
    # Patch GoogleGenerativeAIEmbeddings to fix batching bug in the current SDK
    def patched_embed_documents(self, texts: list[str], **kwargs) -> list[list[float]]:
        embeddings = []
        for j, text in enumerate(texts):
            while True:
                try:
                    result = self.client.models.embed_content(
                        model=self.model,
                        contents=text,
                        config=self._build_config(
                            task_type=self.task_type or "RETRIEVAL_DOCUMENT",
                            output_dimensionality=self.output_dimensionality,
                        )
                    )
                    # The response has a list of embeddings, but we only have 1 since we passed 1 string
                    if hasattr(result, 'embeddings') and result.embeddings:
                        embeddings.append(list(result.embeddings[0].values))
                    else:
                        # Fallback for unexpected response structures
                        embeddings.append([0.0] * 768) 
                    break
                except Exception as e:
                    if '429' in str(e):
                        print(f"    Rate limit hit, sleeping for 15 seconds...")
                        time.sleep(15)
                    else:
                        raise e
            # Removed the 0.5s sleep to speed up ingestion by 2x. 
            # The API can handle ~2 requests/second safely without it.
        return embeddings

    GoogleGenerativeAIEmbeddings.embed_documents = patched_embed_documents

    # Initialize VectorStore
    print("Connecting to Vector Store and embedding chunks in batches...")
    vectorStore = Chroma(
        persist_directory=db_folder,
        embedding_function=embeddings_model
    )
    
    # Batch insertion to avoid rate limits
    batch_size = 100
    total_batches = (len(splits) + batch_size - 1) // batch_size
    
    for i in range(0, len(splits), batch_size):
        batch = splits[i:i + batch_size]
        print(f"Processing batch {i // batch_size + 1} of {total_batches} ({len(batch)} documents)...")
        vectorStore.add_documents(batch)
    
    print(f"✓ Success! Medical Memory created at {db_folder}")

# Run this script to build your database
if __name__ == "__main__": 
    build_nativecare_db()