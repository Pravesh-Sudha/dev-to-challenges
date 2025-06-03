from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from utils import get_response, send_email_postmark

app = FastAPI()

class PostmarkInbound(BaseModel):
    From: str
    Subject: str
    TextBody: str

@app.post("/inbound-email")
async def receive_email(payload: PostmarkInbound):
    sender = payload.From
    subject = payload.Subject
    body = payload.TextBody

    # Avoid infinite loop by skipping self-sent emails
    if sender == "assistant@codewithpravesh.tech":
        return {"message": "Self-email detected, skipping."}

    response = get_response(body)

    try:
        send_email_postmark(
            to_email=sender,
            subject=f"Re: {subject}",
            body=response
        )
    except Exception as e:
        print("Email send failed, but continuing:", e)

    return JSONResponse(content={"message": "Processed"}, status_code=200)
