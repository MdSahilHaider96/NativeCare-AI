from typing import TypedDict

# Define the Agents State
class AgentState(TypedDict):
    query: str
    chat_history: list
    is_emergency: bool
    context: str
    response: str
    detected_lang: str