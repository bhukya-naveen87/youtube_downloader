import yt_dlp  # type: ignore
import os

def download_playlist(playlist_url):
    print(f"Downloading playlist: {playlist_url}")
    
    output_folder = "playlistdownloads"
    os.makedirs(output_folder, exist_ok=True)

    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        'merge_output_format': 'mp4',
        'outtmpl': f'{output_folder}/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s',
        'quiet': True,
        'no_warnings': True,
        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }
        ],
        'noplaylist': False,  # ensure it processes the whole playlist
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        print("Playlist downloaded successfully.")
    except yt_dlp.utils.DownloadError as e:
        raise Exception(f"Download error: {e}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

# Example playlist URL
playlist_url = "https://youtube.com/playlist?list=PLANRDZaL1nlv6v_6dZusn8BryzUGB7dGp"
download_playlist(playlist_url)
