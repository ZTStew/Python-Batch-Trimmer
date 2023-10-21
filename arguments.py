"""
Object handles command line arguments, stores them together for reference

"""

import sys, glob

class Arguments:
  def __init__(self, args):
  # def __init__(self, directory = "./", trim_time = 5, trim_direction = False):
    # Contains command line arguments given by user
    self.args = args

    # Checks if the first argument in 'args' is "help"
    self.help_check()

    # Time user wants to trim off videos
    self.trim_time = 5
    # False -> Trim start of video
    # True -> Trim end of video
    self.trim_direction = False
    # Video format to search for to trim
    self.file_type = ".mp4"
    # Identifies the directory containing files user wants to trim
    self.directory = "./"
    # Collects all files inside of the given directory to trim
    self.input_files = glob.glob(f"{self.directory}/*" + self.file_type)

    self.assign_args()

  # checks if the user typed in "help" as an argument. If they did, prints help text and exits program
  def help_check(self):
    if len(self.args) > 1:
      if self.args[1].lower() == "help":
        print("Arguments:")
        print("    Trim Amount (Seconds): Int -> The number of seconds you would like to trim. Default: 5 seconds")
        print("    Trim Direction [s/e]: String -> Determines if the trim will be applied to the [s]tart of the video or the [e]nd of the video. Default: Start of the video")
        
        # Program should not run its main function if 'help' argument is found
        sys.exit()

  def assign_args(self):
    # assigns trim_time value
    if len(self.args) > 1:
      self.trim_time = int(self.args[1])

    # assigns trim_direction value
    if len(self.args) > 2:
      if "e" in self.args[2].lower():
        self.trim_direction = True
