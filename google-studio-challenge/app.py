import os
import base64
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
from werkzeug.utils import secure_filename

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    prompt_text = request.form.get("prompt", "")
    style = request.form.get("style", "fantasy")  # default style
    image_file = request.files.get("image")
    audio_file = request.files.get("audio")

    # collect multimodal inputs
    inputs = []
    modalities = []

    if prompt_text.strip():
        inputs.append(prompt_text)
        modalities.append("text")

    if image_file:
        image_path = os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(image_file.filename))
        image_file.save(image_path)
        with open(image_path, "rb") as f:
            image_b64 = base64.b64encode(f.read()).decode("utf-8")
        inputs.append({"mime_type": "image/jpeg", "data": image_b64})
        modalities.append("image")

    if audio_file:
        audio_path = os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(audio_file.filename))
        audio_file.save(audio_path)
        with open(audio_path, "rb") as f:
            audio_b64 = base64.b64encode(f.read()).decode("utf-8")
        inputs.append({"mime_type": "audio/wav", "data": audio_b64})
        modalities.append("audio")

    if not inputs:
        return jsonify({"error": "Please provide at least one input (text, image, or audio)."}), 400

    # Build structured prompt
    modalities_str = ", ".join(modalities)
    story_prompt = f"""
    You are StoryWeave AI.
    Use the following {modalities_str} inputs to create a creative {style} story.

    Provide:
    1. A 300-400 word story
    2. A short narration script

    ⚠️ Important:
    - Do NOT use any Markdown formatting (no **bold**, no *italics*, no bullet points).
    - Return plain text only.
    """

    # put the instructions prompt at the beginning
    multimodal_inputs = [story_prompt] + inputs

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(multimodal_inputs)

    return jsonify({"story": response.text})


if __name__ == "__main__":
    app.run(debug=True)
