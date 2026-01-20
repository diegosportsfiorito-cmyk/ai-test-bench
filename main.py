import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ai_openrouter import ask_openrouter
from ai_gemini import ask_gemini

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    prompt: str


@app.get("/")
def root():
    return {"status": "ok", "message": "AI Test Bench activo"}


@app.post("/test/openrouter")
def test_openrouter(body: Query):
    start = time.time()
    response = ask_openrouter(body.prompt)
    latency = round((time.time() - start) * 1000)
    return {"provider": "openrouter", "latency_ms": latency, "response": response}


@app.post("/test/gemini")
def test_gemini(body: Query):
    start = time.time()
    response = ask_gemini(body.prompt)
    latency = round((time.time() - start) * 1000)
    return {"provider": "gemini", "latency_ms": latency, "response": response}