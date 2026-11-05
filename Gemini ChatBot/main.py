import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

MODEL = "gemini-3.8-flash"

def ask(question):
    for attempt in range(4):
        try:
            return client.models.generate_content(
                model=MODEL, contents=question
            ).text
        except errors.ServerError:
            time.sleep(2 ** attempt)  # 503 pe 1s, 2s, 4s, 8s wait retry
        except errors.ClientError as e:
            return f"Error: {e}"  
    return "Servers is busy , try again later."

while True:
    question = input("You: ")
    if question.lower() == "quit":
        break
    print("Gemini:", ask(question))