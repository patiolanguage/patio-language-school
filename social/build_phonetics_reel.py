#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Audio Reels for the "Sound of the week" carousels, with Sofia's WhatsApp voice notes.
Same method as build_mandarin_reel.py.

Frames come from build_phonetics_sounds.slides(set, reel=True), 1080x1920.
Audio: Sofia's voice notes in the Patio Vault inbox, named phonetics-<word>.ogg.
Timeline: cover (silent), word 1, word 2, word 3, workshop invite (closing voice note if there is one).

Usage:  python build_phonetics_reel.py 1      (or 2, 3)
Outputs (social/Phonetics/reels/):
  sound{n}-reel-1080x1920.mp4          with Sofia's voice
  sound{n}-reel-silent-1080x1920.mp4   no audio, to add Instagram music instead
  sound{n}-reel-cover-1080x1920.png    cover for the Reel
"""
import glob, os, subprocess, sys
import build_mandarin as bm
import build_phonetics_sounds as ps

OUT = os.path.join(bm.SOCIAL, "Phonetics", "reels")
os.makedirs(OUT, exist_ok=True)
AUDIO = r"C:\Users\Claire\Documents\Patio-Vault\inbox"
FF = glob.glob(os.path.expandvars(
    r"%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg*\ffmpeg-*\bin"))[0]
FFMPEG, FFPROBE = os.path.join(FF, "ffmpeg.exe"), os.path.join(FF, "ffprobe.exe")
LEAD, TAIL = 0.4, 0.8

# voice note file per set: three words, then the closing line
VOICES = {
    1: ["phonetics-nao.ogg", "phonetics-mao.ogg", "phonetics-cao.ogg"],
    2: ["phonetics-lagos.ogg", "phonetics-pastel-de-nata.ogg", "phonetics-dois.ogg"],
    3: ["phonetics-trabalho.ogg", "phonetics-vinho.ogg", "phonetics-rua.ogg"],
}
CLOSING = "phonetics-closing.ogg"

def run(args):
    subprocess.run(args, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def duration(path):
    out = subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", path], capture_output=True, text=True, check=True)
    return float(out.stdout.strip())

def frames(s, n):
    pngs = []
    for k, html in enumerate(ps.slides(s, reel=True), start=1):
        h = os.path.join(OUT, f"sound{n}-frame-{k}.html")
        with open(h, "w", encoding="utf-8") as f:
            f.write(html)
        png = h.replace(".html", ".png")
        run([bm.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
             "--force-device-scale-factor=1", "--window-size=1080,1920",
             "--virtual-time-budget=6000", f"--screenshot={png}", h])
        pngs.append(png)
    cover = os.path.join(OUT, f"sound{n}-reel-cover-1080x1920.png")
    run(["cmd", "/c", "copy", "/y", pngs[0].replace("/", "\\"), cover.replace("/", "\\")])
    return pngs

def segment(png, voice, hold, out):
    video = ["-loop", "1", "-framerate", "30", "-i", png]
    enc = ["-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p", "-r", "30",
           "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2"]
    if voice:
        dur = LEAD + duration(voice) + TAIL + hold
        run([FFMPEG, "-y", *video, "-i", voice,
             "-af", f"loudnorm=I=-16:TP=-1.5:LRA=11,adelay={int(LEAD*1000)}:all=1,apad",
             "-t", f"{dur:.2f}", *enc, out])
    else:
        run([FFMPEG, "-y", *video, "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
             "-t", f"{hold:.2f}", *enc, out])
    return out

def build(n):
    s = next(x for x in ps.SETS if x["n"] == n)
    voices = [os.path.join(AUDIO, v) for v in VOICES[n]]
    missing = [v for v in voices if not os.path.exists(v)]
    if missing:
        sys.exit("Missing voice notes: " + ", ".join(os.path.basename(m) for m in missing))
    closing = os.path.join(AUDIO, CLOSING)
    closing = closing if os.path.exists(closing) else None
    pngs = frames(s, n)
    plan = [(pngs[0], None, 2.5)] + [(pngs[i + 1], voices[i], 0.4) for i in range(3)]
    plan.append((pngs[4], closing, 2.0 if closing else 4.0))
    segs = [segment(p, v, h, os.path.join(OUT, f"sound{n}-seg-{k}.mp4")) for k, (p, v, h) in enumerate(plan)]
    lst = os.path.join(OUT, f"sound{n}-segments.txt")
    with open(lst, "w", encoding="utf-8") as f:
        f.writelines(f"file '{x.replace(os.sep, '/')}'\n" for x in segs)
    final = os.path.join(OUT, f"sound{n}-reel-1080x1920.mp4")
    run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", "-movflags", "+faststart", final])
    silent = os.path.join(OUT, f"sound{n}-reel-silent-1080x1920.mp4")
    run([FFMPEG, "-y", "-i", final, "-an", "-c:v", "copy", "-movflags", "+faststart", silent])
    print("rendered", os.path.basename(final), f"{duration(final):.1f}s", "(closing voice)" if closing else "(no closing voice yet)")

if __name__ == "__main__":
    build(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
