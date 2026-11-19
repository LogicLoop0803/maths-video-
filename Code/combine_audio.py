"""Combine the visual track with the approved HeyGen narration.
Save the WAV at Audio/gradient_narration_heygen.wav, then run:
    python Code/combine_audio.py
Requires FFmpeg on PATH.
"""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
VIDEO = ROOT / "Video" / "Gradient_Visual_Track_1080p.mp4"
AUDIO = ROOT / "Audio" / "gradient_narration_heygen.wav"
OUTPUT = ROOT / "Video" / "Gradient_Animation_Final.mp4"

for path in (VIDEO, AUDIO):
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")

cmd = ["ffmpeg", "-y", "-i", str(VIDEO), "-i", str(AUDIO),
       "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
       "-c:a", "aac", "-b:a", "192k", "-shortest",
       "-movflags", "+faststart", str(OUTPUT)]
subprocess.run(cmd, check=True)
print(f"Created narrated video: {OUTPUT}")
