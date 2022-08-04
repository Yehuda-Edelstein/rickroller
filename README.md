# rickroller

rickroller is a python script designed to create rick rolls, however it can be customized to make any type of video mashup.

![roll](https://media.giphy.com/media/Ju7l5y9osyymQ/giphy.gif)

## How it works

There are two files that can be run; one is for creating a single video, the other for multiple. However, both use the same logic which is as follows...

We retrieve a url from YouTube and download the video. Next, we clip the first 10 seconds and concatenate it with the music video for Rick Astley's famous hit single _Never Gonna Give You Up_. Finally, the original video is deleted to save space, leaving us with a rick roll.

## Usage

1. Fork and/or `git clone https://github.com/Yehuda-Edelstein/rickroller.git`
2. `cd rickroller/rickroller`
3. `mkdir originals rolls`
4. Pick a `search_word` and start rolling.

## Nayvadius DeMun Wilburn

I am working on adding a final (optional) piece to rickroller where the `roll.py` file generated can be uploaded to a chosen YouTube account, including with it a similar title, description, and taglist.
