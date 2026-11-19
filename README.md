# M3 Animation Project — Gradient: Direction of Steepest Increase

**Student:** Mohammad Mustafa  
**Student ID:** E25B070875  
**Course:** M3 — Multivariable Calculus  
**Topic:** Gradient — Direction of Steepest Increase

## Learning objective

Explain the gradient of a two-variable function, calculate it at a point, interpret its direction and magnitude, and show why it gives the direction of steepest local increase.

## Mathematical example

We study

\[
f(x,y)=x^2+2y^2.
\]

Its gradient is

\[
\nabla f(x,y)=(2x,4y).
\]

At \(P=(1,1)\),

\[
\nabla f(1,1)=(2,4),\qquad
\|\nabla f(1,1)\|=\sqrt{20}=2\sqrt5.
\]

The unit steepest-ascent direction is

\[
\left(\frac1{\sqrt5},\frac2{\sqrt5}\right).
\]

For any unit direction \(\mathbf u\),

\[
D_{\mathbf u}f=\nabla f\cdot\mathbf u
=\|\nabla f\|\cos\theta,
\]

so the maximum occurs when \(\theta=0\), i.e. when the direction matches the gradient.

## Repository contents

- `Code/`: Python source for the visual renderer, Manim scene, retiming, audio muxing, and HeyGen voice generation.
- `Documentation/`: narration, storyboard and mathematical verification PDFs (see local project package), references, AI disclosure, submission checklist and viva notes.
- `Audio/`: generated WAV narration (available in the downloadable project package; binary upload is not included in this GitHub source commit).
- `Video/`: final narrated MP4 and visual tracks (available in the downloadable project package; binary upload is not included in this GitHub source commit).

## Rebuild

Install Python 3.10+, FFmpeg, and dependencies:

```bash
python -m pip install -r Code/requirements-render.txt
```

Render the visual assets:

```bash
python Code/render_video.py
```

To rebuild the narration, create a HeyGen API key, set it as `HEYGEN_API_KEY` (never commit the key), then run:

```bash
python -m pip install requests
python Code/generate_voice.py
```

To combine a downloaded narration WAV with the visual track:

```bash
python Code/combine_audio.py
```

## AI disclosure

AI assistance supported planning, narration drafting, code development and documentation. HeyGen Voice generated the Indian-English narration. The mathematical derivation is documented for independent review. See `Documentation/AI_Disclosure.md`.

## Video export note

The final export is 1920×1080 at a 15 fps MP4 stream; the original authored visual source uses 4 fps, so some motion may look less smooth than native 15 fps animation.
