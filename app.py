import os
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, JSONResponse
from dotenv import load_dotenv
from groq_client import GroqClient

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Initialize Groq client with API key from .env
client = GroqClient()  


# Serve the chat UI
@app.get("/", response_class=HTMLResponse)
async def get_ui():
    with open("chat_ui.html", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

# Handle user queries
@app.post("/ask")
async def ask_movie(query: str = Form(...)):
    result = client.query_movie(query)
    return JSONResponse(content={"response": result})