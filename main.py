from fastapi import FastAPI
from ai_gemini import ask_gemini
from ai_openrouter import ask_openrouter
import time

app = FastAPI()

@app.get("/")
def root():
    return {"status": "AI Test Bench OK"}

# -------------------------------
# Test individual: Gemini
# -------------------------------
@app.post("/test/gemini")
async def test_gemini(payload: dict):
    prompt = payload.get("prompt", "")

    t0 = time.time()
    response = ask_gemini(prompt)
    latency = int((time.time() - t0) * 1000)

    return {
        "provider": "gemini",
        "latency_ms": latency,
        "response": response
    }

# -------------------------------
# Test individual: OpenRouter
# -------------------------------
@app.post("/test/openrouter")
async def test_openrouter(payload: dict):
    prompt = payload.get("prompt", "")

    t0 = time.time()
    response = ask_openrouter(prompt)
    latency = int((time.time() - t0) * 1000)

    return {
        "provider": "openrouter",
        "latency_ms": latency,
        "response": response
    }

# -------------------------------
# Test combinado: Gemini + OpenRouter
# -------------------------------
@app.post("/test/all")
async def test_all(payload: dict):
    prompt = payload.get("prompt", "")

    # Gemini
    t1 = time.time()
    gemini_resp = ask_gemini(prompt)
    gemini_latency = int((time.time() - t1) * 1000)

    # OpenRouter
    t2 = time.time()
    openrouter_resp = ask_openrouter(prompt)
    openrouter_latency = int((time.time() - t2) * 1000)

    return {
        "gemini": {
            "latency_ms": gemini_latency,
            "response": gemini_resp
        },
        "openrouter": {
            "latency_ms": openrouter_latency,
            "response": openrouter_resp
        }
    }
