from prompts.movie_prompts import build_prompt
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

class GroqClient:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.endpoint = os.getenv("GROQ_ENDPOINT")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def query_movie(self, user_input: str):
        prompt = build_prompt(user_input)
        payload = {
            "model": "llama3-8b-8192",  # or llama3-8b-8192, gemma-7b-it
            "messages": [
                {"role": "system", "content": "You are a helpful movie assistant."},
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(self.endpoint, json=payload, headers=self.headers)

        # Check and raise if bad request
        if response.status_code != 200:
            print("❌ ERROR:", response.text)  # Debug
            response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"]
