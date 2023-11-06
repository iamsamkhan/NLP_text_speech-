import os
from flask import Flask, request, render_template, redirect, url_for
from utils.utils import allowed_file, convert_audio_to_wav
from utils.speech_to_text import convert_audio_to_text

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def create_upload_directory():
    # Create the 'uploads' directory if it doesn't exist
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        create_upload_directory()  # Ensure 'uploads' directory exists

        if 'audio_file' not in request.files:
            return redirect(request.url)
        
        file = request.files['audio_file']
        
        if file.filename == '':
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            # Save the uploaded file
            audio_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(audio_path)
            
            # Convert audio to WAV format
            wav_path = convert_audio_to_wav(audio_path)
            
            # Convert WAV to text
            text = convert_audio_to_text(wav_path)
            
            return render_template('index.html', text=text)
    
    return render_template('index.html', text=None)

if __name__ == '__main__':
    app.run(debug=True)