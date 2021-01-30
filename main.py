from telegram_handler import TelegramHandler as Telegram
from reddit_handler import RedditHandler
from twitter_handler import TwitterHandler
from time import sleep
from messages import bot_messages
from my_telegram_data import my_user_id, my_user, my_first_name


def main():
    t_bot = Telegram()
    reddit = RedditHandler()
    twitter = TwitterHandler()

    t_bot.get_me()
    t_bot.send_message(bot_messages['start'].format(my_first_name), my_user_id, my_user)
    aux = 0

    while True:
        last_updates = t_bot.get_updates()

        if last_updates:
            for update in last_updates:
                if aux == 0 and reddit.check_subreddit_exists(update['message']['text']):
                    reddit.subreddit_hot(update['message']['text'])



        sleep(2)


if __name__ == '__main__':
    main()
