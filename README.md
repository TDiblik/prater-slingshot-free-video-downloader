# Prater Slingshot Free Video Downloader

Did you go on the **Slingshot ride at Prater** and don’t want to pay **15 €** just to get your own video recording?
This tool allows you to download your ride video directly using its **video code**.

⚠️ **Disclaimer:** This project is for educational and research purposes only. Please respect the ride operators’ terms of service and support them if you enjoyed your experience.

---

## ✨ Features

- Download your slingshot video using only the video code
- Automatically fetches and stitches video segments into a single file
- Produces a clean `output.mp4` file

---

## 📦 Requirements

- **Python 3**
- **ffmpeg** (installed and available in your PATH)
- Python libraries:

  - `requests`

Install dependencies with:

```bash
pip install requests
```

---

## 🚀 Usage

1. Clone or download this repository.
2. Open `downloader.py` in your editor.
3. Set your **video code**:

   ```python
   VIDEO_CODE = "YOUR_VIDEO_CODE_HERE"
   ```

4. (Optional) Adjust `TOTAL_DURATION` if your video is longer than `120` seconds.
5. Run the script:

   ```bash
   python3 downloader.py
   ```

6. The script will:

   - Download video segments
   - Concatenate them using ffmpeg
   - Save the final result as `output.mp4` in the project root.

---

## ⚙️ Configuration

Inside `downloader.py` you can tweak:

- `VIDEO_CODE` → Your unique video identifier
- `TOTAL_DURATION` → Total video length in seconds (default: `120`)
- `SEGMENT_DURATION` → How long each downloaded chunk is (default: `30`)

---

## 🛠 How It Works

1. The script queries the **VT3 highlights API** for video chunks.
2. It downloads all parts into a temporary folder.
3. It generates a `file_list.txt` containing the clips.
4. ffmpeg concatenates the chunks into a seamless `output.mp4`.

---

## 📂 Example Output

```
Downloaded: clip_1.mp4
Downloaded: clip_2.mp4
Downloaded: clip_3.mp4
✅ Final video created: output.mp4
```

---

## ⚠️ Disclaimer

This project is intended for **research and personal use only**.
Downloading copyrighted content without permission may violate laws or terms of service. The authors take **no responsibility** for misuse.
