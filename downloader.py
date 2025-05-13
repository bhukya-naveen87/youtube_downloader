import yt_dlp # type: ignore
import os

def download_video(url):
    print(url)
    """
    Downloads a YouTube video in 720p or 1080p, if available.
    """
    output_folder = "downloads"
    os.makedirs(output_folder, exist_ok=True)

    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        'merge_output_format': 'mp4',
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
        'quiet': True,
        'no_warnings': True,
        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }
        ],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download=True)
            file_name = ydl.prepare_filename(result)
            return file_name
    except yt_dlp.utils.DownloadError as e:
        raise Exception(f"Download error: {e}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

url = "https://www.youtube.com/watch?v=BLlEgtp2_i8"
download_video(url)