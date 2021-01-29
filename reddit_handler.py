from api_keys import reddit_id, reddit_secret
import praw
import requests
import urllib3


class RedditHandler:
    def __init__(self):
        self.reddit = praw.Reddit(client_id=reddit_id,
                                  client_secret=reddit_secret,
                                  user_agent='reddit_to_twitter')
        self.thread_list = []

    def subreddit_hot(self, subreddit_name):
        self.thread_list = self.reddit.subreddit(subreddit_name).hot(limit=25)

    # TODO create function to download video/gif/picture from given thread
    def download_media(self):
        pass

    # TODO create function to grab all post info from given thread
    def thread_data(self):
        pass
