"""
Update Ideas:
  add in the ability to handle command-line options
"""

import os, sys
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from arguments import Arguments

# handles all argument informaiton given when program is executed
arg = Arguments(sys.argv)

# Creates output folder to store processed .mp4 files
check = os.path.exists("./output")
if not check:
  os.makedirs("./output")

# Returns the duration of a given video
def get_length(input_video):
    clip = VideoFileClip(input_video)
    return clip.duration

# Itterates through all .mp4 files found in given directory
for input_file in arg.input_files:
  file_name = os.path.basename(input_file)

  # Trims video from the start
  if not arg.trim_direction:
      ffmpeg_extract_subclip(input_file, arg.trim_time, get_length(input_file), targetname="./output/"+os.path.splitext(file_name)[0]+".mp4")

  # Trims video from the end
  if arg.trim_direction:
    ffmpeg_extract_subclip(input_file, 0, get_length(input_file) - arg.trim_time, targetname="./output/"+os.path.splitext(file_name)[0]+".mp4")