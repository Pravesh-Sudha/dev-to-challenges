import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_KEY'))
model = genai.GenerativeModel("gemini-2.0-flash")

def get_philosophical_reply(prompt):
    question_prompt = f"You are a wise philosopher. Answer deeply:\nUser: {prompt}\nPhilosopher:"
    response = model.generate_content(question_prompt)
    return response.text
