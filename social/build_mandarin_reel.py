#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Audio Reel for "Your first 3 words in Mandarin", with Michelle's voice notes.

Frames come from build_mandarin_words.slides(reel=True), 1080x1920.
Audio: Michelle's WhatsApp voice notes, saved in the Patio Vault inbox.

Timeline: cover (silent), nǐ hǎo, xièxie, zàijiàn, taster invite ("see you Oct 12").
Each slide lasts as long as its voice note plus a short lead and tail.

Outputs (social/Mandarin/words/reel/):
  words-reel-1080x1920.mp4          with Michelle's voice
  words-reel-silent-1080x1920.mp4   no audio, to add Instagram music instead
  words-reel-cover-1080x1920.png    cover, content inside the 3:4 grid crop
"""
import glob, os, subprocess
import build_mandarin as bm
import build_mandarin_words as bw

OUT = os.path.join(bw.OUT, "reel")
os.makedirs(OUT, exist_ok=True)
AUDIO = r"C:\Users\Claire\Documents\Patio-Vault\inbox"
FF = glob.glob(os.path.expandvars(
    r"%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg*\ffmpeg-*\bin"))[0]
FFMPEG, FFPROBE = os.path.join(FF, "ffmpeg.exe"), os.path.join(FF, "ffprobe.exe")

LEAD, TAIL = 0.4, 0.7
# (slide index, voice note or None, extra hold seconds)
PLAN = [
    (0, None, 2.5),
    (1, "mandarin-audio-ni-hao.ogg", 0),
    (2, "mandarin-audio-xiexie.ogg", 0),
    (3, "mandarin-audio-zaijian.ogg", 0),
    (4, "mandarin-audio-see-you-oct-12.ogg", 2.0),
]

def run(args):
    subprocess.run(args, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def duration(path):
    out = subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", path], capture_output=True, text=True, check=True)
    return float(out.stdout.strip())

def frames():
    """Frame 1 is the dedicated cover (grid safe), then slides 2 to 5."""
    cover = os.path.join(OUT, "frame-cover.html")
    with open(cover, "w", encoding="utf-8") as f:
        f.write(bw.reel_cover())
    cover_png = os.path.join(OUT, "words-reel-cover-1080x1920.png")
    run([bm.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
         "--force-device-scale-factor=1", "--window-size=1080,1920",
         "--virtual-time-budget=6000", f"--screenshot={cover_png}", cover])
    paths = []
    for n, html in enumerate(bw.slides(reel=True), start=1):
        h = os.path.join(OUT, f"frame-{n}.html")
        with open(h, "w", encoding="utf-8") as f:
            f.write(html)
        png = h.replace(".html", ".png")
        run([bm.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
             "--force-device-scale-factor=1", "--window-size=1080,1920",
             "--virtual-time-budget=6000", f"--screenshot={png}", h])
        paths.append(png)
    paths[0] = cover_png
    return paths

def segments(pngs):
    segs = []
    for k, (i, voice, hold) in enumerate(PLAN):
        seg = os.path.join(OUT, f"seg-{k}.mp4")
        video = ["-loop", "1", "-framerate", "30", "-i", pngs[i]]
        enc = ["-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p", "-r", "30",
               "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2"]
        if voice:
            src = os.path.join(AUDIO, voice)
            dur = LEAD + duration(src) + TAIL + hold
            run([FFMPEG, "-y", *video, "-i", src,
                 "-af", f"loudnorm=I=-16:TP=-1.5:LRA=11,adelay={int(LEAD*1000)}:all=1,apad",
                 "-t", f"{dur:.2f}", *enc, seg])
        else:
            run([FFMPEG, "-y", *video, "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                 "-t", f"{hold:.2f}", *enc, seg])
        segs.append(seg)
    return segs

def join(segs):
    lst = os.path.join(OUT, "segments.txt")
    with open(lst, "w", encoding="utf-8") as f:
        f.writelines(f"file '{s.replace(os.sep, '/')}'\n" for s in segs)
    final = os.path.join(OUT, "words-reel-1080x1920.mp4")
    run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", "-movflags", "+faststart", final])
    silent = os.path.join(OUT, "words-reel-silent-1080x1920.mp4")
    run([FFMPEG, "-y", "-i", final, "-an", "-c:v", "copy", "-movflags", "+faststart", silent])
    print("rendered", os.path.basename(final), f"{duration(final):.1f}s")
    print("rendered", os.path.basename(silent))

if __name__ == "__main__":
    join(segments(frames()))
