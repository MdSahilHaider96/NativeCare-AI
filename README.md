# NativeCare-AI
What it does: It talks to people in their native language to give medical advice. It is smart enough to know if a situation is a "Red Alert" (Emergency) or just a minor injury.

How it works: * The Brain (AI): Uses Google Gemini to understand symptoms.

The Library: It searches a saved database of medical facts to give real answers (not just guesses).

The Face: A clean chat screen built with React and Tailwind CSS.

The Goal: To help people who don't speak English get the right medical help instantly.



A sophisticated multilingual medical assistance agent built with LangGraph and Gemini 2.5, featuring a modular "Triage-Search-Respond" architecture. It provides real-time first-aid guidance with automated emergency detection and native language translation.

Key Features
Modular Agentic Workflow: Utilizes LangGraph to manage complex logic states between triage, vector search, and response nodes.

Emergency Recognition: Automatically detects life-threatening keywords and triggers high-priority "Emergency Status" flags in the UI.

RAG Integration: Implements Retrieval-Augmented Generation using ChromaDB to provide medically grounded answers from verified documentation.

Full Stack Stack: Built with a React + Tailwind CSS frontend and a containerized FastAPI backend using Docker.

The Tech (Simplified):

React: The "Face" (The chat screen the user sees).

FastAPI: The "Bridge" (Connects the Face to the Brain).

LangGraph: The "Brain" (The logic that decides: Is this an emergency? Do I need to search the library?).

ChromaDB: The "Library" (Where all the first-aid facts are stored).
