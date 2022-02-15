import os
from moviepy.editor import *
from datetime import date


def movie(opfilename="final.mp4"):
    total_length = 0
    videos = []
    today = date.today()
    path = ".//Download//" + str(today)
    intro_path = ".//introoutro//intro_musicless.mp4"
    intro = VideoFileClip(intro_path)
    intro = intro.resize(width=1920)
    intro = intro.resize(height=1080)
    videos.append(intro)
    print(intro_path)

    outro_path = ".//introoutro//outro_musicless.mp4"
    outro = VideoFileClip(outro_path)
    outro = outro.resize(width=1920)
    outro = outro.resize(height=1080)
    print(outro_path)

    print("Making Video")
    for fileName in os.listdir(path):
        if os.path.isfile(os.path.join(path, fileName)) and fileName.endswith(".mp4"):
            print(fileName)
            filePath = os.path.join(path, fileName)
            # Destination path
            clip = VideoFileClip(filePath)
            clip = clip.resize(width=1920)
            clip = clip.resize(height=1080)
            duration = clip.duration
            videos.append(clip)
            total_length += duration

    videos.append(outro)

    final_clip = concatenate_videoclips(videos, method="compose")
    final_clip.write_videofile(filename=opfilename)

    print("Video Complete")


if __name__ == "__main__":
    movie()
