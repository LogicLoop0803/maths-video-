"""Rebuild the supplied visual sequence and mux the narration.

Run from project root:
    python Code/render_video.py

This orchestrator calls the visual renderer and retimer. Add the supplied
HeyGen WAV at Audio/gradient_narration_heygen.wav, then run
Code/combine_audio.py to create the narrated MP4.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for script in ("render_visual_draft.py", "retime_visual_track.py"):
    subprocess.run([sys.executable, str(ROOT / "Code" / script)], cwd=ROOT, check=True)
print("Visual track rebuilt. Add the HeyGen WAV, then run Code/combine_audio.py.")
