# AI Voice Generation

The delivered project narration used HeyGen Voice, public voice **Devansh** (Indian-English male).

- Voice ID: `129cbbad06554f28a7351d192221cb1e`
- Language: English (`en`)
- Input: `Documentation/Narration_Script.md`
- Output: `Audio/gradient_narration_heygen.wav`
- Script: `Code/generate_voice.py`

## Re-generate

1. Install: `python -m pip install requests`
2. Create a HeyGen API key in your HeyGen account.
3. Set it as `HEYGEN_API_KEY` in your environment. Never commit the key.
4. Run `python Code/generate_voice.py` from the project root.

API access for a public voice depends on your HeyGen plan and current API availability. A regenerated take may differ from the original audio.
