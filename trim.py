import os, glob
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


directory = "./"
input_files = glob.glob(f"{directory}/*.mp4")
start_time = 4

# Creates output folder to store processed .mp4 files
check = os.path.exists("./output")
if not check:
  os.makedirs("./output")

# Returns the duration of a given video
def get_length(input_video):
    clip = VideoFileClip(input_video)
    return clip.duration

# Itterates through all .mp4 files found in given directory
for input_file in input_files:
  file_name = os.path.basename(input_file)
  ffmpeg_extract_subclip(input_file, start_time, get_length(input_file), targetname="./output/"+os.path.splitext(file_name)[0]+".mp4")
