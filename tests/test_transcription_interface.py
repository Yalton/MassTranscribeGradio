import asyncio
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import Mock, patch

from modules.transcription_interface import TranscriptionInterface


class TranscriptionInterfaceTests(unittest.TestCase):
    def test_returns_transcribed_text(self):
        with TemporaryDirectory() as directory:
            audio = Path(directory) / "sample.wav"
            audio.write_bytes(b"audio")
            response = Mock(status_code=200)
            response.json.return_value = {"text": "recognized words"}
            with patch("modules.transcription_interface.requests.session") as session:
                session.return_value.send.return_value = response
                text = asyncio.run(TranscriptionInterface("localhost", "token").transcribe(str(audio)))
                request = session.return_value.send.call_args.args[0]
        self.assertEqual(text, "recognized words")
        self.assertEqual(request.url, "http://localhost:8001/v1/audio/transcriptions/")
        self.assertEqual(request.headers["Authorization"], "token")

    def test_rejects_unexpected_response(self):
        with TemporaryDirectory() as directory:
            audio = Path(directory) / "sample.wav"
            audio.write_bytes(b"audio")
            response = Mock(status_code=200)
            response.json.return_value = {"result": "missing text"}
            with patch("modules.transcription_interface.requests.session") as session:
                session.return_value.send.return_value = response
                text = asyncio.run(TranscriptionInterface("localhost", "token").transcribe(str(audio)))
        self.assertIsNone(text)


if __name__ == "__main__":
    unittest.main()
