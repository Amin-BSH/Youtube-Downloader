import argparse
from pathlib import Path
from typing import Optional

from pytubefix import YouTube
from pytubefix.exceptions import VideoUnavailable
from tqdm import tqdm


class YouTubeDownloader:
    """Downloads YouTube videos using the pytubefix library.

    Args:
        url (str): YouTube video URL.
        output_path (Optional[Path]): Output directory for downloaded video (default: current working directory).
        quality (Optional[str]): Video quality (default: "highest").

    Attributes:
        url (str): The YouTube video URL.
        output_path (Path): The output directory for downloaded videos.
        quality (str): The desired video quality.

    Methods:
        download(): Downloads the video.
        on_progress(stream: YouTube, chunk: bytes, bytes_remaining: int): Callback for download progress.
        on_complete(stream: YouTube, file_path: str): Callback for download completion.
    """

    def __init__(
        self,
        url: str,
        output_path: Optional[Path] = None,
        quality: Optional[str] = None,
    ):
        self.url = url
        self.output_path = output_path or Path.cwd()
        self.quality = quality or "highest"
        self.yt = YouTube(
            self.url,
            on_progress_callback=self.on_progress,
            on_complete_callback=self.on_complete,
        )

    def download(self) -> None:
        try:
            self.yt.check_availability()
        except VideoUnavailable:
            print("Video is unavailable")
            return

        if self.quality == "highest":
            stream = self.yt.streams.filter(
                progressive=True, file_extension="mp4"
            ).get_highest_resolution()
        else:
            stream = self.yt.streams.filter(
                progressive=True, file_extension="mp4", res=self.quality
            ).first()

        self.pbar = tqdm(
            desc="Downloading ...",
            total=stream.filesize,
            unit="B",
            unit_scale=True,
        )

        stream.download(self.output_path)

    def on_progress(self, stream: YouTube, chunk: bytes, bytes_remaining: int) -> None:
        current = stream.filesize - bytes_remaining
        self.pbar.update(current - self.pbar.n)

    def on_complete(self, stream: YouTube, file_path: str) -> None:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube Downloader")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("-q", "--quality", help="Video quality", default="highest")
    parser.add_argument("-o", "--output_path", help="Output path", default=None)

    args = parser.parse_args()

    YouTubeDownloader(
        url=args.url,
        quality=args.quality,
        output_path=args.output_path,
    ).download()
