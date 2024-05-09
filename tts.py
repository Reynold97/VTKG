import os
import shutil
from datetime import datetime
from dotenv import load_dotenv
from deepgram import DeepgramClient, PrerecordedOptions

load_dotenv()
API_KEY = os.getenv('DEEPGRAM_API_KEY')
deepgram = DeepgramClient(API_KEY) 

def ensure_dir(directory):
    """Ensure the specified directory exists; if not, create it."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def transcribe_audio(audio_path):
    """Transcribes audio using Deepgram's API and saves the audio file with a unique timestamp."""
    audio_storage_dir = "permanent_audio_files"
    ensure_dir(audio_storage_dir)
    
    # Generate a unique filename with a timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"audio_{timestamp}.wav"
    permanent_audio_path = os.path.join(audio_storage_dir, filename)
    
    shutil.copy(audio_path, permanent_audio_path)
    print(f"Saved audio file to: {permanent_audio_path}")  # Debug: Confirm file save

    options = PrerecordedOptions(model="nova-2", smart_format=True)

    try:
        # Open the permanently stored audio file for transcription
        with open(permanent_audio_path, 'rb') as audio:
            source = {'buffer': audio}
            response = deepgram.listen.prerecorded.v("1").transcribe_file(source, options)
            transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
            return transcript
    except Exception as e:
        print("Error during transcription:", e)
        return str(e)

