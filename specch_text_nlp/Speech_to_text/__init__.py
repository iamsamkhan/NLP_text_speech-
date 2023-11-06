import os
from pydub import AudioSegment

ALLOWED_EXTENSIONS = {'mp3', 'wav'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_audio_to_wav(audio_path):
    # Converts audio file (e.g., MP3) to WAV format using pydub
    sound = AudioSegment.from_mp3(audio_path)
    wav_path = audio_path.replace('.mp3', '.wav')
    sound.export(wav_path, format="wav")
    return wav_path
