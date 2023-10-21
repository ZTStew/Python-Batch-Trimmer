"""
Update Ideas:
  add in the ability to handle command-line options
"""

import os, glob, sys
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


help_flag = False

if len(sys.argv) > 1:
  # Prints how to use program into command line
  if sys.argv[1].lower() == "help":
    print("Arguments:\n  Trim Amount (Seconds): Int\n  Trim Direction [s/e]: String")
    print("    Trim Amount: The number of seconds you would like to trim. Default: 5 seconds")
    print("    Trim Direction: Determines if the trim will be applied to the [s]tart of the video or the [e]nd of the video. Default: Start of the video")

    help_flag = True

if not help_flag:
  directory = "./"
  input_files = glob.glob(f"{directory}/*.mp4")
  trim_time = 5
  # False -> Trim start of video
  # True -> Trim end of video
  trim_direction = False

  # assigns trim_time value
  if len(sys.argv) > 1:
    trim_time = int(sys.argv[1])

  # assigns trim_direction value
  if len(sys.argv) > 2:
    if "e" in sys.argv[2]:
      trim_direction = True


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

    # Trims video from the start
    if not trim_direction:
        ffmpeg_extract_subclip(input_file, trim_time, get_length(input_file), targetname="./output/"+os.path.splitext(file_name)[0]+".mp4")

    # Trims video from the end
    if trim_direction:
      ffmpeg_extract_subclip(input_file, 0, get_length(input_file) - trim_time, targetname="./output/"+os.path.splitext(file_name)[0]+".mp4")