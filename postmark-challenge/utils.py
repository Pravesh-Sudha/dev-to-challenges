import os
import requests
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

# Create a client instance using your API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash-preview-04-17-thinking")

def get_response(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    
    except Exception as e:
        return f"Error: {e}"

def send_email_postmark(to_email, subject, body):
    postmark_token = os.getenv('POSTMARK_API_TOKEN')
    payload = {
        "From": "assistant@codewithpravesh.tech",
        "To": to_email,
        "Subject": subject or "No Subject",
        "TextBody": body or "Empty Response",
    }

    print("Sending to Postmark with payload:", payload)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Postmark-Server-Token": postmark_token
    }

    try:
        r = requests.post("https://api.postmarkapp.com/email", json=payload, headers=headers)
        if r.status_code != 200:
            print("Postmark error:", r.status_code, r.text)
        r.raise_for_status()
    except Exception as e:
        print("Failed to send email via Postmark:", e)
