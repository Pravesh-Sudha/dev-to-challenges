import os
import asyncio
import wave
from dotenv import load_dotenv
import assemblyai as aai

load_dotenv()
aai.settings.api_key = os.getenv("ASSEMBLY_AI_KEY")

PHILOSOPHY_PHRASES = [
    "existentialism", "epistemology", "Plato", "Socrates", "Nietzsche",
    "Aristotle", "Descartes", "dualism", "stoicism", "Kant", "ontology",
    "utilitarianism", "phenomenology", "nihilism", "teleology"
]

async def simulate_audio_stream(file_path, chunk_size=3200):
    with wave.open(file_path, 'rb') as wf:
        while True:
            data = wf.readframes(chunk_size)
            if not data:
                break
            yield data
            await asyncio.sleep(0.08) 

async def transcribe_audio_stream(file_path):
    config = aai.RealtimeConfig(
        language_code="en_us",
        custom_vocabulary=PHILOSOPHY_PHRASES,
        speech_model="universal-v2",
        disfluencies=False,
        punctuate=True
    )

    transcriber = aai.RealtimeTranscriber(config=config)
    transcript_text = ""

    async def on_data(transcript: aai.RealtimeTranscript):
        nonlocal transcript_text
        if isinstance(transcript, aai.RealtimeFinalTranscript):
            transcript_text += transcript.text + " "

    await transcriber.connect()
    transcriber.on("transcript", on_data)

    async for chunk in simulate_audio_stream(file_path):
        await transcriber.send(chunk)

    await transcriber.close()
    return transcript_text.strip()