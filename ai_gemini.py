import os
import google.genai as genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

def ask_gemini(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-1.5-pro-latest",
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"ERROR: {str(e)}"
