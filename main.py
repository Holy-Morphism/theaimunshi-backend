from models.request.chat import Message
from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from graph import run_graph
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Welcome to The AI Munshi's Backend"}

@app.post("/chat")
def chatbot(message:Message):
    return {
        "role":"assisstant",
        "content":"Hello it's working now!",
        "timestampe":message.timestamp
    }
