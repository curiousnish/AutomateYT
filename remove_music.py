from moviepy.editor import VideoFileClip

intro_path = ".//introoutro//intro.mp4"
intro = VideoFileClip(intro_path)
intro_clip = intro.without_audio()
intro_clip.write_videofile("intro_musicless.mp4")


outro_path = ".//introoutro//outro.mp4"
outro = VideoFileClip(outro_path)
outro_clip = outro.without_audio()
outro_clip.write_videofile("outro_musicless.mp4")
