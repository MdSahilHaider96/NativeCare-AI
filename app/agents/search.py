from app.graph.state import AgentState
from app.tools.vector_store import vector_db

# NODE 2: Medical Search (RAG)
def search_node(state: AgentState):
    if state['is_emergency']:
        return {"context": "EMERGENCY_DETECTED"}
    
    # Retrieve top 3 relevant chunks from your medical PDFs
    docs = vector_db.similarity_search(state['query'], k=3)
    context_text = "\n\n".join([d.page_content for d in docs])
    return {"context": context_text}
