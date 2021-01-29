from telegram_handler import TelegramHandler as Telegram
import reddit_handler as reddit
import twitter_handler as twitter
from time import sleep


def main():
    bot = Telegram()
    bot.get_me()

    while True:
        last_updates = bot.get_updates()
        if last_updates:
            print(last_updates)
        else:
            print('nada')
        sleep(5)


if __name__ == '__main__':

    main()

# TODO create functions to interact via Telegram
