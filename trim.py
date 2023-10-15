from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

input_file = "./test.mp4"
output_file = "./output.mp4"
start_time = 5


def get_length(input_video):
    clip = VideoFileClip(input_video)
    return clip.duration

ffmpeg_extract_subclip(input_file, start_time, get_length(input_file), targetname=output_file)
