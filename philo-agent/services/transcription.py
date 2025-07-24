import assemblyai as aai
import os
from dotenv import load_dotenv
load_dotenv()

aai.settings.api_key = os.getenv('ASSEMBLY_AI_KEY')

def transcribe_audio(file_path):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(file_path)
    return transcript.text
