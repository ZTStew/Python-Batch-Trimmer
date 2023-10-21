"""
Object handles command line arguments, stores them together for reference

"""

class Arguments:
  __init__(self,
    directory = "./",
    start_time = 5,
    trim_direction = False):

    self.directory = directory
    self.input_files = glob.glob(f"{self.directory}/*.mp4")
    self.start_time = start_time
    # False -> Trim start of video
    # True -> Trim end of video
    self.trim_direction = trim_direction
