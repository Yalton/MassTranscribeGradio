import json
import os
import requests
from modules.utils import logging


class TranscriptionInterface:
    def __init__(self, ip_addr, auth_token):
        logging.info("Instantiating Transcription Interface")

        self.ip_addr = ip_addr
        self.auth_token = auth_token

    async def transcribe(self, audio_file):
        url = f'http://{self.ip_addr}:8000/v1/audio/transcriptions/'
        headers = {
            "Authorization": f'{self.auth_token}',
            # "Content-Type": "multipart/form-data"
        }
        files = {
            'file': (os.path.basename(audio_file), open(audio_file, 'rb'), 'video/webm')
        }

        request = requests.Request('POST', url, headers=headers, files=files)
        prepared_request = request.prepare()

        # Print the raw request
        logging.info("Raw Request:")
        logging.info(f"URL: {prepared_request.url}")
        logging.info(f"Headers: {prepared_request.headers}")
        # print(f"Body: {prepared_request.body}")

        # Send the request
        response = requests.session().send(prepared_request)

        if response.status_code == 200:
            data = response.json()
            logging.info(f"Response data: {data}")
            if isinstance(data, dict) and "text" in data:
                return data["text"]
            else:
                logging.error("Unexpected response format. 'text' key not found.")
                return None
        else:
            try:
                error_response = response.json()
                logging.error(f"Error: {response.status_code} - {error_response}")
            except ValueError:
                logging.error(f"Error: {response.status_code} - {response.text}")
            return None
