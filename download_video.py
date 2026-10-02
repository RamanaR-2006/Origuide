#!/usr/bin/env python3
"""Download one YouTube video into this project's videos directory."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from urllib.parse import urlparse


PROJECT_DIR = Path(__file__).resolve().parent
VIDEOS_DIR = PROJECT_DIR / "videos"
YOUTUBE_HOSTS = ("youtube.com", "youtube-nocookie.com", "youtu.be")


def is_youtube_url(value: str) -> bool:
    """Return whether *value* is an HTTP(S) URL hosted by YouTube."""
    try:
        parsed = urlparse(value)
        hostname = (parsed.hostname or "").lower().rstrip(".")
    except ValueError:
        return False

    return parsed.scheme in {"http", "https"} and any(
        hostname == host or hostname.endswith(f".{host}") for host in YOUTUBE_HOSTS
    )


def download_video(url: str, output_dir: Path = VIDEOS_DIR) -> None:
    """Download one video from *url* to *output_dir*."""
    try:
        from yt_dlp import YoutubeDL
        from yt_dlp.utils import DownloadError
    except ImportError as exc:
        raise RuntimeError(
            "yt-dlp is not installed. Run: python -m pip install -r requirements.txt"
        ) from exc

    output_dir.mkdir(parents=True, exist_ok=True)
    options = {
        "noplaylist": True,
        "outtmpl": str(output_dir / "%(title)s [%(id)s].%(ext)s"),
        "windowsfilenames": True,
    }

    try:
        with YoutubeDL(options) as downloader:
            downloader.download([url])
    except DownloadError as exc:
        raise RuntimeError(f"Download failed: {exc}") from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Download a single YouTube video into the videos/ folder."
    )
    parser.add_argument("url", help="YouTube video URL")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if not is_youtube_url(args.url):
        print("Error: provide a valid YouTube URL.", file=sys.stderr)
        return 2

    try:
        download_video(args.url)
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Download complete. Files are in: {VIDEOS_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
