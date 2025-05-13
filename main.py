from fastapi import FastAPI, HTTPException, BackgroundTasks # type: ignore
from fastapi.responses import FileResponse # type: ignore
from pydantic import BaseModel # type: ignore
from downloader import download_video
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}

class VideoRequest(BaseModel):
    url: str

@app.post("/download/")
async def download_youtube_video(video_request: VideoRequest, background_tasks: BackgroundTasks):
    """
    Endpoint to download a YouTube video.
    """
    video_url = video_request.url

    try:
        # Download video in the background
        file_path = download_video(video_url)
        background_tasks.add_task(clean_up_file, file_path)
        return {"message": "Video downloaded successfully!", "download_path": file_path}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/download/{file_name}")
def get_video(file_name: str):
    """
    Serve the downloaded video file.
    """
    file_path = os.path.join("downloads", file_name)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path, media_type="video/mp4", filename=file_name)


def clean_up_file(file_path: str):
    """
    Deletes the downloaded file after serving.
    """
    if os.path.exists(file_path):
        os.remove(file_path)
