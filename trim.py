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
arg.set_output_directory()


# Returns the duration of a given video
def get_length(input_video):
    clip = VideoFileClip(input_video)
    return clip.duration

# Itterates through all files found in given directory
for input_file in arg.input_files:
  # Extracts file path from input_file's name
  file_name = os.path.basename(input_file)

  # Gives the output file's path, name, and extension
  output = arg.output_dir + "/" + os.path.splitext(file_name)[0] + arg.file_type

  # Trims video from the start
  if not arg.trim_direction:
    # input file -> file that is being trimmed
    # arg.trim_time -> amount of time to be trimmed from input file
    # get_length(input_file) -> length of the file after trimming
    # targetname=output -> output file's path, name, and extension
    ffmpeg_extract_subclip(input_file, arg.trim_time, get_length(input_file), targetname=output)

  # Trims video from the end
  if arg.trim_direction:
    ffmpeg_extract_subclip(input_file, 0, get_length(input_file) - arg.trim_time, targetname=output)
