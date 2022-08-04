# rickroller

rickroller is a python script designed to create rick rolls, however it can be customized to make any type of video mashup.

## How it works

There are two files that can be run; one is for creating a single video, the other for multiple. However, both use the same logic which is as follows...

We retrieve a url from YouTube and download the video. Next, we clip the first 10 seconds and concatenate it with the music video for Rick Astley's famous hit single _Never Gonna Give You Up_. Finally, the original video is deleted to save space, leaving us with a rick roll.

## Usage

1. Fork and/or clone the repo
2. `cd rickroller/rickroller`
3. `mkdir originals rolls`
4. Choose your `search_word` to query videos
5. Start rolling.

## Nayvadius DeMun Wilburn

I am working on adding a final (optional) piece to rickroller where the `roll.py` file generated can be uploaded to a chosen YouTube account, including with it a similar title, description, and taglist.

<br>
<p align="center">
  <img src="https://media.giphy.com/media/kFgzrTt798d2w/giphy.gif" alt="roll" />
</p>
