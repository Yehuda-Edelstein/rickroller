import urllib.request
import re
from pytube import YouTube
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

# use '+' signs between words as regular spaces will throw an error
search_word = 'never+gonna+give+you+up'

# get the video
link = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={search_word}")

# scan for video's unique 11 character id
r = r"watch\?v=(\S{11})"
id = re.findall(r, link.read().decode())

# create multiple videos at once using this for loop (set range to the amount of videos you want)
for i in range(2):
    vid = f"https://www.youtube.com/watch?v={id[i]}"
    yt = YouTube(vid)
    yt.streams.filter(mime_type="video/mp4", progressive=True).first().download(output_path='originals', filename=f"{search_word}_result_{i}.mp4")
    print("Video was succesfully downloaded!")

# loops through every video in the originals directory
x = 1
for video in os.listdir("originals"):
    original = VideoFileClip(f'originals/{video}').subclip(0, 5)
    rick = VideoFileClip('rick.mp4')
    new = concatenate_videoclips([original, rick])
    new.write_videofile(f'rolls/roll_{x}.mp4')
    x = x + 1

# deletes original videos to save space
for video in os.listdir("originals"):
    os.remove(os.path.join(f'originals/', video))

# python loops.py
# or
# python3 loops.py