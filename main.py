from fastapi import FastAPI

from graph import run_graph
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to The AI Munshi's Backend"}

@app.post("/chat")
def get_users(query:str):
    return run_graph(str)
