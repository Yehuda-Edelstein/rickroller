import os
import urllib.request
import re
from pytube import YouTube
from moviepy.editor import VideoFileClip, concatenate_videoclips

# use '+' signs between words as regular spaces will throw an error
search_word = 'never+gonna+give+you+up'

# get the video
link = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={search_word}")

# scan for video's unique 11 character id
r = r"watch\?v=(\S{11})"
id = re.findall(r, link.read().decode())

#  id[0] returns the first video (i.e., most popular or relevant)
vid = f"https://www.youtube.com/watch?v={id[0]}"

# converts vid into a YouTube object using pytube
yt = YouTube(vid)

# downloads the file with video/audio, then saves it to the originals directory
yt.streams.filter(mime_type="video/mp4", progressive=True).first().download(output_path='originals', filename=f"{search_word}.mp4")
print("Video was succesfully downloaded!")

# moviepy.editor cuts the first 5 seconds of the video using .subclip(start_time, stop_time) and concatenates it with our rick
original = VideoFileClip(f'originals/{search_word}.mp4').subclip(0, 5)
rick = VideoFileClip('rick.mp4')
new = concatenate_videoclips([original, rick])
new.write_videofile(f'rolls/roll.mp4')

# deletes original video to save space
os.remove(os.path.join(f'originals/{search_word}.mp4'))

# python single.py
# or
# python3 single.py




