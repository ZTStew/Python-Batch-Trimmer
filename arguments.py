"""
Description:
  Object handles command line arguments, stores them together for reference
"""

import sys, glob, os, argparse

class Arguments:
  def __init__(self):
    # Handles command line options/arguments
    args = argparse.ArgumentParser(description="Program searches given folder for video files and trims a specified number of seconds from the start or the end of the video. The file is then saved in a specified location.")

    # command line option for trim amount
    args.add_argument(
      "-t",
      "--trim_amount",
      type=int,
      help="Trim Amount (Seconds): Int -> The number of seconds you would like to trim. Default: 5 seconds"
    )
    # command line option for trim direction
    args.add_argument(
      "-d",
      "--trim_direction",
      type=str,
      help="Trim Direction [s/e]: String -> Determines if the trim will be applied to the [s]tart of the video or the [e]nd of the video. Default: Start of the video"
    )

    # Parse the command-line arguments
    self.args = args.parse_args()

    # Time user wants to trim off videos
    self.trim_amount = 5
    # False -> Trim start of video
    # True -> Trim end of video
    self.trim_direction = False
    # Video format to search for to trim
    self.file_type = ".mp4"
    # Identifies the directory containing files user wants to trim
    self.directory = "./"
    # Collects all files inside of the given directory to trim
    self.input_files = glob.glob(f"{self.directory}/*" + self.file_type)
    # Identifies the location the processed files are saved to
    self.output_dir = "./output"

    self.assign_args()


  # Method overwrites default variables with values proveded by users
  def assign_args(self):
    # assigns trim_amount value
    if self.args.trim_amount:
      self.trim_amount = self.args.trim_amount

    # assigns trim_direction value
    if self.args.trim_direction:
      if "e" in self.args.trim_direction:
        self.trim_direction = True


  # Method creates output folder to store processed .mp4 files
  def set_output_directory(self):
    # Confirms if the specified output directory already exists
    check = os.path.exists(self.output_dir)
    # If the output directory doesn't already exist, create the output directory
    if not check:
      os.makedirs(self.output_dir)
