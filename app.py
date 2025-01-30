from flask import Flask, render_template, request, jsonify
import whisper_s2t
import time
import gc
import torch
import os

app = Flask(__name__)

# Set up the model
device = 'cuda'
computetype = 'float32'
batch_size = 16

# Load the Whisper model globally
model = whisper_s2t.load_model(model_identifier="small", backend="CTranslate2",
                               device=device, compute_type=computetype)

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_audio():
    """Handles audio file upload and transcription for multiple recordings."""
    if 'audio' not in request.files or 'language' not in request.form or 'voice_id' not in request.form:
        return jsonify({"error": "Missing file, language selection, or voice ID"}), 400

    audio_file = request.files['audio']
    language = request.form['language']  # Get selected language
    voice_id = request.form['voice_id']  # Identify which voice recording it is
    
    file_path = os.path.join(UPLOAD_FOLDER, f"recorded_audio_{voice_id}.wav")
    audio_file.save(file_path)

    # Transcribe the audio
    transcribed_text = run_transcription(file_path, language)

    return jsonify({"transcription": transcribed_text, "voice_id": voice_id})

def run_transcription(file_path, language):
    """Transcribes the audio file using the selected language."""
    lang_codes = [language]
    tasks = ['transcribe']
    initial_prompts = [None]

    start = time.time()
    out = model.transcribe_with_vad([file_path],
                                    lang_codes=lang_codes,
                                    tasks=tasks,
                                    initial_prompts=initial_prompts,
                                    batch_size=batch_size)
    end = time.time()

    transcribed_text = out[0][0]['text']
    print(f"Transcription ({language}): {transcribed_text}")
    print(f"Time taken: {end - start}")

    gc.collect()
    torch.cuda.empty_cache()

    return transcribed_text

if __name__ == '__main__':
    app.run(debug=True)
