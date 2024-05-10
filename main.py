import gradio as gr
import configparser
from modules.transcription_interface import TranscriptionInterface
from modules.utils import read_config

async def transcribe_files(audio_files):
    config = read_config()
    ip_addr = config.get('WHISPER_API', 'ip_addr')
    auth_token = config.get('WHISPER_API', 'auth_token')

    interface = TranscriptionInterface(ip_addr, auth_token)

    transcriptions = []
    for audio_file in audio_files:
        transcription = await interface.transcribe(audio_file.name)
        if transcription:
            transcriptions.append(transcription)

    combined_text = "\n".join(transcriptions)
    return combined_text

def create_text_file(text):
    return text, "transcription.txt"

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            audio_files = gr.File(label="Audio Files", file_count="multiple", file_types=[".wav", ".WAV", ".mp3", ".ogg", ".webm"])
            transcribe_button = gr.Button("Transcribe")
        with gr.Column():
            output_text = gr.Textbox(label="Transcription", lines=10)
            download_button = gr.File(None, label="Download Transcription", file_count="single", file_types=[".txt"], interactive=False)

    transcribe_button.click(fn=transcribe_files, inputs=audio_files, outputs=output_text, queue=False, show_progress=True)
    download_button.upload(fn=create_text_file, inputs=output_text, outputs=download_button)

demo.launch()