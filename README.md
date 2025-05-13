### Youtube Downloader:
- #### Install Pip packages:
  ```
  pip install -r requirements.txt
  ```
- #### Install ffmpeg for Windows:
    - Step 1: Download ffmpeg
      - source: [FFmpeg Builds](https://www.gyan.dev/ffmpeg/builds/)
      - Under "Release builds", download the ZIP for ffmpeg-release-essentials (e.g., ffmpeg-6.x-essentials_build.zip)

    - Step 2: Extract it
      - Extract the zip (e.g., to C:\ffmpeg)
      - Inside that folder, go to bin – you'll find ffmpeg.exe

    - Step 3: Add ffmpeg to PATH
      - Copy the path to the bin folder (e.g., C:\ffmpeg\bin)
      - Press Win + S → search “Environment Variables” → Open it
      - In System Properties → Environment Variables:
      - Under User variables → Select Path → Click Edit
      - Click New → Paste the C:\ffmpeg\bin path
      - Click OK on all dialogs

    - Step 4: Verify ffmpeg is installed
      - Restart your terminal and run:
        - ```ffmpeg -version```
- In downloader.py, at bottom of the file, paste the youtube url which you want to download.
- Run ```py downloader.py```
- It downloads the video into **downloads** folder.

echo "# youtube_downloader" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/bhukya-naveen87/youtube_downloader.git
git push -u origin main