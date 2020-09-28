from moviepy.editor import *
import os
import sys


def main(dirpath):
	for file in [f for f in os.listdir(dirpath) if f.endswith(".mp4")]:
		video = VideoFileClip(os.path.join(dirpath, file))
		video.audio.write_audiofile(os.path.join(dirpath, file.split(".")[0] + ".mp3"))


if __name__ == "__main__":
	if len(sys.argv) == 2:
		main(sys.argv[1])
	else:
		main("./")