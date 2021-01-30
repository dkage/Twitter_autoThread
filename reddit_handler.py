from api_keys import reddit_id, reddit_secret
import praw
from prawcore import exceptions as reddit_errors
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

    def check_subreddit_exists(self, subreddit_name):
        try:
            self.reddit.subreddits.search_by_name(subreddit_name, include_nsfw=True, exact=True)
            return True
        except reddit_errors.NotFound:
            return False

    # TODO create function to download video/gif/picture from given thread
    def download_media(self):
        pass

    # TODO create function to grab all post info from given thread
    def thread_data(self, submission_id):
        thread_info = dict()
        current_submission = self.reddit.submission(id=submission_id)

        thread_info['title'] = current_submission.title if current_submission.title else ''
        thread_info['author'] = current_submission.author if current_submission.author else ''
        thread_info['score'] = current_submission.score if current_submission.score else ''
        thread_info['upvote_ratio'] = current_submission.upvote_ratio if current_submission.upvote_ratio else ''
        thread_info['url'] = current_submission.url if current_submission.url else ''
        thread_info['text'] = current_submission.selftext if current_submission.selftext else ''

        return thread_info
