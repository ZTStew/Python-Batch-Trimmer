import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

input_file = "./test.mp4"
output_file = "./output.mp4"
start_time = 5
end_time = None  # None to keep the rest of the video

ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)
