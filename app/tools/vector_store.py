from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

# Initialize embeddings and vector db
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-2",
    task_type="retrieval_query"
)

vector_db = Chroma(
    persist_directory="./db/nativecare_db", 
    embedding_function=embeddings 
)