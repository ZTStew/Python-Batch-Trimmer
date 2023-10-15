# Batch Video File Trimmer  
---
# Program proved unable to achieve goals through the use of Batch Files as they are incapable of handle floating point variables

---
## Description:  
Program should be able to take all .mp4 files in a given directory, trim off a set amount of time from the start of the video and overwrite the old .mp4 file with the new one.  

---
### Usage:
(explanation of how to use the program)
1. To run program, must first install `ffmpeg` and add it to your computer's path
2. Add `trim.bat` to computer's path using: `setx /m PATH "C:\Users\ZT\Documents\Tools\ffmpeg\bin;%PATH%"`
3. Navigate to folder containing .mp4 files you want to convert and run: `trim.bat`

setx /m PATH "C:\[path to program folder];%PATH%"