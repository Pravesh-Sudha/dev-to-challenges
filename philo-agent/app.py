from flask import Flask, render_template, request, jsonify
from services.transcription import transcribe_audio
from services.gemini import get_philosophical_reply
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "audio_data" not in request.files:
        return jsonify({"error": "No audio data"}), 400

    audio = request.files["audio_data"]
    audio_path = os.path.join(UPLOAD_FOLDER, "input.wav")
    audio.save(audio_path)

    try:
        transcribed_text = transcribe_audio(audio_path)
        response = get_philosophical_reply(transcribed_text)
        return jsonify({
            "question": transcribed_text,
            "response": response
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
