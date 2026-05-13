import sys
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
from app.graph.workflow import native_care

app = FastAPI(title="NativeCare AI API")

# Allow your React Frontend to communicate with this Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "*",
    "Access-Control-Allow-Headers": "*",
}

# Global exception handler - ensures CORS headers are present even on 500 errors
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    error_message = str(exc)
    if "RESOURCE_EXHAUSTED" in error_message or "429" in error_message or "quota" in error_message.lower():
        friendly = "⚠️ The AI is temporarily unavailable due to API rate limits. Please wait a moment and try again."
    else:
        friendly = "An internal server error occurred while processing your request. Please try again later."

    return JSONResponse(
        status_code=500,
        content={"answer": friendly, "is_emergency": False, "language": "NONE"},
        headers=CORS_HEADERS,
    )

# Define what the incoming request looks like
class UserQuery(BaseModel):
    query: str
    history: list = []

@app.post("/api/chat")
async def chat(data: UserQuery):
    try:
        result = native_care.invoke({"query": data.query, "chat_history": data.history})
        return JSONResponse(
            status_code=200,
            content={
                "answer": result.get("response", "I could not generate an answer."),
                "is_emergency": result.get("is_emergency", False),
                "language": result.get("detected_lang", "NONE"),
            },
            headers=CORS_HEADERS,
        )
    except Exception as exc:
        error_message = str(exc)
        if "RESOURCE_EXHAUSTED" in error_message or "429" in error_message or "quota" in error_message.lower():
            friendly = "⚠️ The AI API quota has been exceeded or the key is rate limited. Please wait and try again later."
        else:
            friendly = "An internal server error occurred while processing your request. Please try again later."

        return JSONResponse(
            status_code=500,
            content={"answer": friendly, "is_emergency": False, "language": "NONE"},
            headers=CORS_HEADERS,
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)