# Video Converter

This is a simple video converter that converts a video file to a different format. It uses the `ffmpeg` library to convert the video file.

## Features

- Convert video files to different formats
- Compression of video files
- Change the resolution of the video file

## Requirements

- Python 3 or higher
- ffmpeg library

## Installation

1. Create a virtual environment

```bash
python3 -m venv venv
```

2. Activate the virtual environment

```bash
source venv/bin/activate
```

3. Install the required libraries

```bash
pip install -r requirements.txt
```

## Usage

1. Convert a video file to a different format

```bash
# Convert a video to MP4
python3 src/main.py convert input_videos/example.mkv output.mp4
```

2. Compress a video file
```bash
# Compress a video with a specific CRF value
python3 src/main.py compress input_videos/example.mp4 output_compressed.mp4 --crf 24
```

3. Change the resolution of a video file
```bash
# Upscale a video to 720p
python3 src/main.py upscale input_videos/example.mp4 output_720p.mp4 --resolution 720p
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
