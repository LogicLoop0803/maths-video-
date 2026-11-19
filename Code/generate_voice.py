"""Generate the M3 narration using HeyGen Text-to-Speech.

Voice used for the project: Devansh (Indian English male)
Voice ID: 129cbbad06554f28a7351d192221cb1e

Requirements:
    pip install requests

Set HEYGEN_API_KEY in the environment. Never commit the key.
Run from project root:
    python Code/generate_voice.py
"""
from __future__ import annotations
import os
import re
import sys
import subprocess
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_FILE = ROOT / "Documentation" / "Narration_Script.md"
OUTPUT_FILE = ROOT / "Audio" / "gradient_narration_heygen.wav"
VOICE_NAME = "Devansh"
VOICE_ID = "129cbbad06554f28a7351d192221cb1e"
LANGUAGE = "en"
TTS_ENDPOINT = "https://api.heygen.com/v3/voices/speech"

def extract_narration(markdown: str) -> str:
    lines = []
    for raw_line in markdown.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or line == "---":
            continue
        if re.match(r"^(\*\*|\*|_)?(Scene|Section|Timing|Duration)\b", line, re.I):
            continue
        line = re.sub(r"^[-*]\s+", "", line)
        line = re.sub(r"\*\*(.*?)\*\*", r"\1", line)
        line = re.sub(r"\*(.*?)\*", r"\1", line)
        line = re.sub(r"`([^`]*)`", r"\1", line)
        lines.append(line)
    return "\n\n".join(lines).strip()

def split_text(text: str, limit: int = 4500) -> list[str]:
    chunks, current = [], ""
    for paragraph in text.split("\n\n"):
        candidate = f"{current}\n\n{paragraph}" if current else paragraph
        if len(candidate) <= limit:
            current = candidate
            continue
        if current:
            chunks.append(current)
        if len(paragraph) <= limit:
            current = paragraph
            continue
        current = ""
        for sentence in re.split(r"(?<=[.!?])\s+", paragraph):
            candidate = f"{current} {sentence}".strip()
            if len(candidate) > limit and current:
                chunks.append(current)
                current = sentence
            else:
                current = candidate
    if current:
        chunks.append(current)
    return chunks

def main() -> int:
    api_key = os.getenv("HEYGEN_API_KEY")
    if not api_key:
        print("ERROR: HEYGEN_API_KEY is not set. Never paste the key into this file.")
        return 1
    if not SCRIPT_FILE.exists():
        print(f"ERROR: Narration script not found: {SCRIPT_FILE}")
        return 1
    narration = extract_narration(SCRIPT_FILE.read_text(encoding="utf-8"))
    if not narration:
        print("ERROR: No narration text was found.")
        return 1

    headers = {"X-Api-Key": api_key, "Content-Type": "application/json"}
    parts = []
    for index, chunk in enumerate(split_text(narration), start=1):
        print(f"Generating narration part {index}...")
        response = requests.post(
            TTS_ENDPOINT, headers=headers,
            json={"voice_id": VOICE_ID, "text": chunk, "language": LANGUAGE,
                  "engine": "heygen_voice"}, timeout=180)
        if not response.ok:
            print(f"HeyGen API error ({response.status_code}): {response.text[:1000]}")
            return 1
        audio_url = response.json().get("data", {}).get("audio_url")
        if not audio_url:
            print("ERROR: HeyGen response did not include data.audio_url.")
            return 1
        audio_response = requests.get(audio_url, timeout=180)
        audio_response.raise_for_status()
        parts.append(audio_response.content)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    if len(parts) == 1:
        OUTPUT_FILE.write_bytes(parts[0])
    else:
        temp_dir = OUTPUT_FILE.parent / "voice_parts"
        temp_dir.mkdir(exist_ok=True)
        part_paths = []
        for i, part in enumerate(parts, start=1):
            p = temp_dir / f"part_{i:02d}.wav"
            p.write_bytes(part)
            part_paths.append(p)
        concat_file = temp_dir / "concat.txt"
        concat_file.write_text("".join(f"file '{p.as_posix()}'\n" for p in part_paths), encoding="utf-8")
        result = subprocess.run(
            ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_file),
             "-c", "copy", str(OUTPUT_FILE)], capture_output=True, text=True)
        if result.returncode:
            print(result.stderr[-2000:])
            return 1
    print(f"Audio saved to: {OUTPUT_FILE}")
    print("A regenerated take may differ slightly from the originally delivered narration.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
