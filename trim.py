import os, glob, sys
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


help_flag = False

if len(sys.argv) > 1:
  # Prints how to use program into command line
  if sys.argv[1].lower() == "help":
    print("Arguments:\n  Trim Amount (Seconds): Int")

    help_flag = True

if not help_flag:
  directory = "./"
  input_files = glob.glob(f"{directory}/*.mp4")
  start_time = 5

  if len(sys.argv) > 1:
    start_time = int(sys.argv[1])

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
