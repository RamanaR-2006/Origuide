# Origuide
A project to assist with origami via computer vision and simulation

## Download a YouTube video

Use this only for videos you have permission to download.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python download_video.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

The script creates `videos/` automatically and downloads only one video, even
when the supplied URL contains playlist information. Installing `ffmpeg` is
recommended so `yt-dlp` can merge separate high-quality video and audio streams.
