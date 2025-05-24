import gradio as gr
import asyncio
from modules.transcription_interface import TranscriptionInterface
from modules.utils import read_config, create_directories


def transcribe_files(audio_files):
    if not audio_files:
        return "No files selected"
    
    config = read_config()
    ip_addr = config.get("WHISPER_API", "ip_addr")
    auth_token = config.get("WHISPER_API", "auth_token")

    interface = TranscriptionInterface(ip_addr, auth_token)

    transcriptions = []
    for audio_file in audio_files:
        # Run the async method in sync context
        transcription = asyncio.run(interface.transcribe(audio_file.name))
        if transcription:
            transcriptions.append(transcription)

    combined_text = "\n".join(transcriptions)
    return combined_text


create_directories()

demo = gr.Interface(
    fn=transcribe_files,
    inputs=gr.File(file_count="multiple", file_types=[".wav", ".mp3", ".ogg"]),
    outputs=gr.Textbox(label="Transcription", lines=10),
    title="Audio Transcription"
)

demo.launch(share=True)