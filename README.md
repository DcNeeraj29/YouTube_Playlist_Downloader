# YouTube Playlist Downloader

A Python-based application for downloading YouTube Playlist with both GUI and CLI interfaces. Supports various video resolutions and formats.

This application is not capable of downloading a single video for now.

## Features
- Download YouTube videos in multiple resolutions (e.g., 720p, 1080p)
- Audio-only download option
- Graphical user interface (GUI) for easy interaction
- Command-line interface (CLI) for advanced users
- Configurable download folder and preferences
- Progress tracking and logging

## Installation
1. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage
### GUI Mode
1. Run the application:
   ```bash
   python main.py
   ```
2. Enter the YouTube video URL in the provided field.
3. Select your preferred resolution and click "Download".

### CLI Mode
1. Run the application with the `--cli` flag:
   ```bash
   python main.py --cli
   ```
2. Follow the prompts to enter the YouTube video URL and select options.

## Configuration
Modify the settings in `config.py` to customize the application:
- `DOWNLOAD_FOLDER`: Set the default download directory
- `VIDEO_RESOLUTION`: Choose the default video resolution
- `AUDIO_ONLY`: Enable/disable audio-only downloads

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeatureName`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeatureName`)
5. Open a pull request
