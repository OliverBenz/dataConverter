import os
from moviepy.editor import *
video = VideoFileClip(os.path.join("testvid.mp4"))
video.audio.write_audiofile(os.path.join("testsound.mp3"))