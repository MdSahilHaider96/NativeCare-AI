from langchain_google_genai import ChatGoogleGenerativeAI
from app.graph.state import AgentState

# NODE 3:Respond & Translate 
def final_respond_node(state: AgentState):
    if state.get('is_emergency'):
        return {"response": "🚨 EMERGENCY: Please call 102/108 or go to the nearest hospital immediately."}
    
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)
    
   
    target_lang = state.get('detected_lang', 'NONE')
    translation_instruction = ""
    if target_lang != "NONE":
        translation_instruction = f"ALSO, provide a full translation of your answer in {target_lang} immediately following the English version."

    history_text = ""
    if state.get('chat_history'):
        for msg in state['chat_history']:
            role = "AI" if msg.get("role") == "ai" else "User"
            history_text += f"{role}: {msg.get('content')}\n"

    prompt = f"""
    Chat History:
    {history_text}

    Facts from Medical Manuals: {state.get('context', '')}
    User Question: {state['query']}
    
    Instructions:
    1. Provide a helpful, concise first-aid response in English based ONLY on the facts above.
    2. {translation_instruction}
    """
    res = llm.invoke(prompt).content
    return {"response": res}