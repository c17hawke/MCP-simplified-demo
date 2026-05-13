import os
import requests
from dotenv import load_dotenv

# 1) Load environment variables once
load_dotenv()

# 2) Configuration (kept separate for readability)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set. Add it to your .env file.")

URL = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json",
}
MODEL_NAME = "llama-3.3-70b-versatile"


def ask_groq(question: str) -> str:
    """
    Send one question to Groq and return the assistant's answer.

    Parameters
    ----------
    question : str
        The user's question in plain text.

    Returns
    -------
    str
        The assistant's response text.
    """
    # 3) Build request payload from the single input
    payload = {
        "messages": [{"role": "user", "content": question}],
        "model": MODEL_NAME,
    }

    # 4) Call API
    response = requests.post(URL, headers=HEADERS, json=payload, timeout=30)
    response.raise_for_status()

    # 5) Extract answer
    response_data = response.json()
    assistant_message = response_data["choices"][0]["message"]["content"]
    return assistant_message
