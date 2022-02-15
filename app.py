import reddit_scrapper as rs
import make_movie as mm
import upload as u
from datetime import date


def magic(subname="nextfuckinglevel", post_count=20, sort="new", path=".//Download", opfilename="final", category=24,
          title="Internet is Awesome | Best Meme Compilation #1", description=""):
    # Download the videos from the subreddit
    print("REDDIT SCRAPPER RUNNING")
    rs.download_videos(subname, post_count=post_count, sort=sort, path=path)

    # Compile the videos into a single file with intro and outro
    print("MOVIE MAKER RUNNING")
    movie_name = opfilename + str(date.today()) + ".mp4"
    mm.movie(opfilename=movie_name)

    # Upload the movie to YT
    print("UPLOADER RUNNING")
    u.api_upload(str(movie_name), category=category,
                 title=title, description=description)


if __name__ == "__main__":
    magic(subname="nextfuckinglevel", post_count=5, sort="new",
          path=".//Download", opfilename="final", category=24,
          title="Internet is Awesome | Best Meme Compilation #1", description="")
