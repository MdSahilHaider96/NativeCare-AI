from langchain_google_genai import ChatGoogleGenerativeAI
from app.graph.state import AgentState

# NODE 1: Triage & Language Detection
def Triage_node(state: AgentState):
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    
    prompt = f"""
    Analyze this health query: "{state['query']}"
    
    CRITERIA FOR EMERGENCY (YES):
    - Difficulty breathing, chest pain, heavy bleeding, or loss of consciousness.
    - Fever ABOVE 104°F (40°C).

    1. Is this a life-threatening emergency? (YES/NO)
    2. Does the user ask for a specific language? (Name it or 'NONE')
    
    Answer format: EMERGENCY: [YES/NO], LANG: [Language Name or NONE]
    """
    res = llm.invoke(prompt).content.strip().upper()
    
    is_emergency = "EMERGENCY: YES" in res
    requested_lang = res.split("LANG:")[1].strip() if "LANG:" in res else "NONE"
    
    return {"is_emergency": is_emergency, "detected_lang": requested_lang}