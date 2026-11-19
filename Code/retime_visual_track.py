"""Align the visual draft to the measured narration duration.
Requires FFmpeg on PATH.
"""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Video" / "Gradient_Visual_Draft_1080p.mp4"
OUTPUT = ROOT / "Video" / "Gradient_Visual_Track_1080p.mp4"
TARGET_SECONDS = 255.2736281179

if not SOURCE.exists():
    raise FileNotFoundError(f"Missing source visual draft: {SOURCE}")

# The supplied visual draft is 320 seconds; this speed change aligns it to narration.
speed_factor = 320.0 / TARGET_SECONDS
cmd = ["ffmpeg", "-y", "-i", str(SOURCE),
       "-vf", f"setpts={1/speed_factor:.8f}*PTS,fps=15",
       "-an", "-c:v", "libx264", "-preset", "ultrafast", "-crf", "25",
       "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(OUTPUT)]
subprocess.run(cmd, check=True)
print(f"Created {OUTPUT} ({TARGET_SECONDS:.2f}s, 1920x1080, 15fps stream).")
