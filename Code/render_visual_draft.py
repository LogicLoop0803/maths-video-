"""Create a lightweight silent visual draft (1280x720).

Run from project root: python Code/render_visual_draft.py
This script makes a short 60-second preview. The supplied final visual MP4
and retimed project render are separately included in the ZIP package.
"""
import cv2
import numpy as np
import os
import math
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1280, 720, 15
OUT = os.path.join(os.path.dirname(__file__), "..", "Video", "Gradient_Animation.mp4")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

def font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/Library/Fonts/Arial.ttf"
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def draw_text(draw, xy, text, size=30, fill=(240,244,250), bold=False, anchor=None):
    draw.text(xy, text, font=font(size, bold), fill=fill, anchor=anchor)

def frame(scene, t):
    im = Image.new("RGB", (W, H), (16,19,29))
    d = ImageDraw.Draw(im)
    draw_text(d, (70,42), "M3 / MULTIVARIABLE CALCULUS", 20, (130,150,175), True)
    draw_text(d, (70,82), "THE GRADIENT", 40, (85,214,190), True)
    for x in range(80, W, 60):
        d.line((x,160,x,H-60), fill=(31,39,55), width=1)
    for y in range(180, H-40, 60):
        d.line((60,y,W-60,y), fill=(31,39,55), width=1)
    if scene == 0:
        draw_text(d,(80,230),"Which direction takes you uphill fastest?",34,(255,200,87),True)
        cx,cy=640,450
        for r in range(45,240,28):
            d.ellipse((cx-r,cy-r*.62,cx+r,cy+r*.62),outline=(63,112,150),width=3)
        a=0.5+0.35*math.sin(t*1.8)
        end=(cx+int(220*a),cy-int(135*a))
        d.line((cx,cy,*end),fill=(85,214,190),width=8)
        d.ellipse((cx-9,cy-9,cx+9,cy+9),fill=(255,200,87))
        draw_text(d,(80,610),"A gradient answers this question locally.",24)
    elif scene == 1:
        draw_text(d,(80,220),"A function assigns a height to each input pair.",30)
        draw_text(d,(80,290),"z = f(x, y)",48,(255,200,87),True)
        draw_text(d,(80,390),"The gradient collects the two partial derivatives:",28)
        draw_text(d,(80,465),"∇f(x,y) = ( ∂f/∂x , ∂f/∂y )",42,(85,214,190),True)
        draw_text(d,(80,570),"Each component measures change along one coordinate axis.",23)
    elif scene == 2:
        draw_text(d,(80,210),"Contour map: each curve joins equal function values.",28)
        cx,cy=640,440
        for r in range(38,260,28):
            d.ellipse((cx-r,cy-r*.58,cx+r,cy+r*.58),outline=(67,125,164),width=3)
        px,py=640,440
        d.ellipse((px-9,py-9,px+9,py+9),fill=(255,200,87))
        ex,ey=px+190,py-130
        d.line((px,py,ex,ey),fill=(85,214,190),width=9)
        ang=math.atan2(ey-py,ex-px)
        for da in [2.55,-2.55]:
            q=(ex+28*math.cos(ang+da),ey+28*math.sin(ang+da))
            d.line((ex,ey,*q),fill=(85,214,190),width=8)
        draw_text(d,(830,300),"Gradient",25,(85,214,190),True)
        draw_text(d,(80,610),"It points across level curves, not along them.",24)
    elif scene == 3:
        draw_text(d,(80,210),"WORKED EXAMPLE",30,(255,200,87),True)
        lines=["f(x,y) = x² + 2y²","fₓ = 2x                 fᵧ = 4y","∇f(x,y) = (2x, 4y)","At P = (1,1):  ∇f(1,1) = (2,4)","Magnitude = √(2² + 4²) = 2√5"]
        for i,s in enumerate(lines):
            draw_text(d,(100,285+i*65),s,34,(85,214,190) if i in (2,3) else (238,242,248),i in (0,3))
    elif scene == 4:
        draw_text(d,(80,210),"DIRECTIONAL DERIVATIVE",30,(255,200,87),True)
        lines=["For a unit direction u:","Dᵤf = ∇f · u","= ||∇f|| ||u|| cos θ","Since ||u|| = 1:  Dᵤf = ||∇f|| cos θ","The largest value occurs at θ = 0.","So u points in the same direction as ∇f."]
        for i,s in enumerate(lines):
            draw_text(d,(95,280+i*57),s,30,(85,214,190) if i>=4 else (238,242,248),i==5)
    else:
        draw_text(d,(80,210),"THREE TAKEAWAYS",32,(255,200,87),True)
        lines=["1. The gradient is made of partial derivatives.","2. It is perpendicular to a level curve.","3. It points toward the greatest local increase.","","Mohammad Mustafa  •  E25B070875"]
        for i,s in enumerate(lines):
            draw_text(d,(100,300+i*65),s,28,(85,214,190) if i==2 else (238,242,248),i==2)
    draw_text(d,(70,675),"GRADIENT • M3 ANIMATION PROJECT",16,(105,122,148))
    return cv2.cvtColor(np.array(im),cv2.COLOR_RGB2BGR)

writer = cv2.VideoWriter(OUT, cv2.VideoWriter_fourcc(*"mp4v"), FPS, (W,H))
for scene in range(6):
    for i in range(FPS*10):
        writer.write(frame(scene, i/FPS))
writer.release()
print("Created:", os.path.abspath(OUT))
