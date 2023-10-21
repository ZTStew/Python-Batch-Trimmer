"""
Object handles command line arguments, stores them together for reference

"""

import os, sys, glob

class Arguments:
  def __init__(self, args):
  # def __init__(self, directory = "./", start_time = 5, trim_direction = False):

    self.args = args
    # self.directory = directory
    # self.input_files = glob.glob(f"{self.directory}/*.mp4")
    self.start_time = 5
    # False -> Trim start of video
    # True -> Trim end of video
    self.trim_direction = False

    self.help_check()

  # checks if the user typed in "help" as an argument. If they did, prints help text and exits program
  def help_check(self):
    if len(self.args) > 1:
      if self.args[1].lower() == "help":
        print("Arguments:\n  Trim Amount (Seconds): Int\n  Trim Direction [s/e]: String")
        print("    Trim Amount: The number of seconds you would like to trim. Default: 5 seconds")
        print("    Trim Direction: Determines if the trim will be applied to the [s]tart of the video or the [e]nd of the video. Default: Start of the video")
        
        sys.exit()
