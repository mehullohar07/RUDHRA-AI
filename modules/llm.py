import os

from dotenv import load_dotenv
from groq import Groq
from core.assistant import ASSISTANT_NAME

load_dotenv()

MODEL_NAME = "openai/gpt-oss-20b"

def get_ai_response(prompt):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return "Groq API key missing. Please check your .env file."

    try:
        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": (
                        f"You are {ASSISTANT_NAME}, a helpful personal "
                        "assistant created by Mehul. Give clear, "
                        "accurate, and concise answers."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            max_completion_tokens=500,
        )

        answer = response.choices[0].message.content
        return answer.strip() if answer else "No response generated."

    except Exception as error:
        print(f"AI Error: {error}")
        return (
            "Sorry, I could not connect to the AI service. "
            "Check your API key, internet connection, and model availability."
        )