import praw
from redvid import Downloader
from uritemplate import variables
import config
from datetime import date

# Global Variables
client_id = config.client_id
client_secret = config.client_secret
user_agent = config.user_agent


def get_metadata(subredditname="", post_count=15, sort="new"):
    reddit_praw = praw.Reddit(client_id=client_id,
                              client_secret=client_secret, user_agent=user_agent)

    post_metadata = {}

    print("Getting Posts Metadata")

    if sort == 'new':
        new_posts = reddit_praw.subreddit(subredditname).new(
            limit=post_count)
        for post in new_posts:
            if post.url.startswith("https://v."):
                post_metadata[post.title] = "https://www.reddit.com" + \
                    post.permalink

    if sort == 'hot':
        hot_posts = reddit_praw.subreddit(subredditname).hot(limit=post_count)
        for post in hot_posts:
            if post.url.startswith("https://v."):
                post_metadata[post.title] = "https://www.reddit.com" + \
                    post.permalink

    if sort == 'top':
        top_posts = reddit_praw.subreddit(subredditname).top(limit=post_count)
        for post in top_posts:
            if post.url.startswith("https://v."):
                post_metadata[post.title] = "https://www.reddit.com" + \
                    post.permalink

    print("Retrieved all Posts Metadata")

    return post_metadata


def download_videos(subredditname="", post_count=15, sort="new", path=".//Download"):
    post_metadata = get_metadata(
        subredditname=subredditname, post_count=post_count, sort=sort)
    today = date.today()
    path = path + "//" + str(today)
    print("Downloading Videos")
    for title, url in post_metadata.items():
        reddit_redvid = Downloader(max_q=True)
        reddit_redvid.max = True
        reddit_redvid.path = path
        reddit_redvid.url = url
        reddit_redvid.download()

    print("Download Completed")


if __name__ == "__main__":
    download_videos("nextfuckinglevel", post_count=5)
