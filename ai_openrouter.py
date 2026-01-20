import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def ask_openrouter(prompt: str) -> str:
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "meta-llama/llama-3-8b-instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        r = requests.post("https://openrouter.ai/api/v1/chat/completions",
                          json=data, headers=headers)

        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]

    except Exception as e:
        return f"ERROR: {str(e)}"