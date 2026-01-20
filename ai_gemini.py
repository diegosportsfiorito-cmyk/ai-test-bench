import os
import google.generativeai as genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

def ask_gemini(prompt: str) -> str:
    try:
        response = genai.generate_text(
            model="gemini-1.5-pro-latest",
            prompt=prompt,
            temperature=0.7,
        )
        return response.result
    except Exception as e:
        return f"ERROR: {str(e)}"
