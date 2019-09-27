from moviepy.editor import *

import os
from os import listdir
from os.path import isfile, join
files = [f for f in listdir("./") if isfile(join("./", f))]

for file in files:
    if ".mp4" in file:
        video = VideoFileClip(os.path.join(file))
        video.audio.write_audiofile(os.path.join(file.split(".")[0] + ".mp3"))