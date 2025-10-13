import os
import requests
import subprocess
import shutil

# --- CONFIG ---
VIDEO_CODE = "YOUR_VIDEO_CODE_HERE"
WORK_DIR = "temp"
API_URL = "https://sys.vt3.io/highlights"
SEGMENT_DURATION = 30  # API limit
TOTAL_DURATION = 120  # change depending on how long your source video is
OUTPUT_FILE = "./output.mp4"


def get_highlight(video_code, start, duration):
    payload = {
        "videoCode": video_code,
        "startTimeSeconds": start,
        "durationSeconds": duration,
    }
    headers = {"Content-Type": "application/json"}
    r = requests.post(API_URL, json=payload, headers=headers)
    r.raise_for_status()
    data = r.json()
    if "url" in data:
        return data["url"]
    else:
        print("Error:", data)
        return None


def download_file(url, filename):
    r = requests.get(url, stream=True)
    r.raise_for_status()
    with open(filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)


if __name__ == "__main__":
    if os.path.exists(WORK_DIR):
        shutil.rmtree(WORK_DIR)
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
    os.makedirs(WORK_DIR)
    os.chdir(WORK_DIR)

    clip_files = []
    start = 0
    part = 1

    while start < TOTAL_DURATION:
        url = get_highlight(VIDEO_CODE, start, SEGMENT_DURATION)
        if url is None:
            break

        filename = f"clip_{part}.mp4"
        download_file(url, filename)
        clip_files.append(filename)
        print(f"Downloaded: {filename}")
        start += SEGMENT_DURATION
        part += 1

    with open("file_list.txt", "w") as f:
        for clip in clip_files:
            f.write(f"file '{clip}'\n")

    subprocess.run(
        [
            "ffmpeg",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            "file_list.txt",
            "-c",
            "copy",
            f"../{OUTPUT_FILE}",
        ]
    )

    print(f"✅ Final video created: {OUTPUT_FILE}")
