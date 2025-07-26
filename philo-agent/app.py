from flask import Flask, render_template, request, jsonify
from services.transcription import transcribe_audio_stream
from services.gemini import get_philosophical_reply
import os
import traceback, asyncio

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "audio_data" not in request.files:
        print("❌ No audio data found in request.")
        return jsonify({"error": "No audio data"}), 400

    try:
        audio = request.files["audio_data"]
        audio_path = os.path.join(UPLOAD_FOLDER, "input.wav")
        audio.save(audio_path)
        print(f"✅ Audio saved at: {audio_path}")

        transcribed_text = asyncio.run(transcribe_audio_stream(audio_path))
        print(f"📝 Transcription: {transcribed_text}")

        response = get_philosophical_reply(transcribed_text)
        print(f"🧠 Response: {response}")

        return jsonify({
            "question": transcribed_text,
            "response": response
        })
    except Exception as e:
        print("🔥 Exception occurred:")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
