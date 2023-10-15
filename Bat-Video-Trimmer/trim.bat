rem @echo off

cd /d "%CD%"
setlocal enabledelayedexpansion

if not exist ".\trimmed" mkdir .\trimmed

for %%I in (*.mp4) do (
  set input_file="%%I"
  set output_file=".\trimmed\trimmed_%%~nI.mp4"
  set trim_time=300
  set total_duration=0

  ffprobe -v error -select_streams v:0 -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1 "!input_file!" > duration.txt

  set /p total_duration=<duration.txt
  set /a total_duration=total_duration * 100

  set /a final_duration=total_duration - trim_time
  set /a final_duration=final_duration / 100

  echo !total_duration!
  echo !final_duration!

  ffmpeg -v error -y -i !input_file! -ss !trim_time! -t !duration_to_keep! -c:v copy -c:a aac !output_file!

)

rem -t !duration_to_keep!
