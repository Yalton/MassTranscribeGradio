# Audio Transcription Web App

This is a simple web application built with Gradio that allows you to transcribe multiple audio files and download the combined transcription as a single text file.

## Features

- Upload multiple audio files in various formats (WAV, MP3, OGG, WEBM)
- Transcribe all the uploaded audio files using the Whisper API
- Display the combined transcription in the web interface
- Download the transcription as a text file

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/audio-transcription-app.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the Whisper API:
   - Create a `config.ini` file in the project directory
   - Add the following section and fill in the necessary details:
     ```
     [WHISPER_API]
     ip_addr = your_whisper_api_ip_address
     auth_token = your_whisper_api_auth_token
     ```

## Usage

1. Run the Gradio web application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to the provided URL (e.g., `http://localhost:7860`).

3. Upload one or more audio files using the "Audio Files" input.

4. Click the "Transcribe" button to start the transcription process.

5. The transcription will be displayed in the "Transcription" textbox.

6. Click the "Download Transcription" button to download the transcription as a text file.

## File Structure

- `main.py`: The main Gradio web application script
- `modules/transcription_interface.py`: Contains the `TranscriptionInterface` class for interacting with the Whisper API
- `modules/utils.py`: Utility functions for reading the configuration file
- `config.ini`: Configuration file for storing the Whisper API details
- `requirements.txt`: List of required Python packages

## Dependencies

- Gradio: A Python library for building web interfaces for machine learning models
- ConfigParser: A Python library for parsing configuration files

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgements

- [Whisper API](https://whisper.com/) for providing the audio transcription service
- [Gradio](https://gradio.app/) for the intuitive web interface framework