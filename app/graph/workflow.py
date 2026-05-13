from langgraph.graph import StateGraph, END 
from app.graph.state import AgentState
from app.agents.triage import Triage_node
from app.agents.search import search_node
from app.agents.responder import final_respond_node

# 3. Build the Graph
builder = StateGraph(AgentState)

builder.add_node("triage", Triage_node)
builder.add_node("search", search_node)
builder.add_node("respond", final_respond_node)

builder.set_entry_point("triage")
builder.add_edge("triage", "search")
builder.add_edge("search", "respond")
builder.add_edge("respond", END)

native_care = builder.compile()