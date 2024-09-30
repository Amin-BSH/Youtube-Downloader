# YouTube Downloader

This Python script allows you to download YouTube videos using the `pytubefix` library. You can specify the video quality and output directory for downloaded videos.

## Project Structure

```
|
|-src
| |-main.pu
|-README.md
|-requirements.txt
```

## Installation

1. Make sure you have Python 3.x installed.
2. Install the required dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Open a terminal or command prompt.
2. Run the script with the following command:

    ```bash
    python main.py [OPTIONS] URL
    ```

    Replace `[OPTIONS]` with any of the following (optional):
    - `-q`, `--quality`: Specify video quality (default: "highest").
    - `-o`, `--output_path`: Specify the output directory (default: current working directory).

    Example usage:

    ```bash
    python main.py -q 720p -o /path/to/output https://www.youtube.com/watch?v=VIDEO_ID
    ```

3. The video will be downloaded to the specified output directory.

## Notes

- If the video is unavailable, the script will display a message.
- The progress of the download will be shown using a progress bar.

---

Remember to replace `[OPTIONS]` and `URL` with actual values when running the script. Feel free to customize the README further to include additional information or instructions specific to your use case.