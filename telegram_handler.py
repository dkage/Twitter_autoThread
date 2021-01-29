from api_keys import BOT_KEY
import requests
import json


class TelegramHandler:
    def __init__(self):
        self.base_url = "https://api.telegram.org/bot{}/".format(BOT_KEY)

        self.name = ''
        self.user = ''
        self.bot_id = 0
        self.offset = None
        self.aux = 0
        self.updates_json = ''

    def get_me(self):
        http_return = requests.get(self.base_url+'getMe')
        json_return = http_return.json()
        self.name = json_return['result']['first_name']
        self.user = json_return['result']['username']
        self.bot_id = json_return['result']['id']

    def get_updates(self):
        update_url = self.base_url + 'getUpdates?timeout=100'

        # If offset is already set, concatenates it to tell API last ID already received
        if self.offset:
            update_url += "&offset={}".format(self.offset)
        http_response = requests.get(update_url)
        json_response = http_response.json()
        self.updates_json = json_response['result']

        # print(update_url)  # Keep for debugging
        # print(json_response)  # Keep for debugging

        # Grabs last offset update_id, and adds one so updates already received and not returned anymore
        if json_response['result']:
            self.offset = int(json_response['result'][-1]['update_id']) + 1
        if json_response['ok']:
            return json_response['result']
        else:
            return False

    @staticmethod
    def get_update_data(json_update):

        update_data = dict()
        update_data['text'] = json_update['text']
        update_data['id'] = json_update['from']['id']
        update_data['user'] = json_update['from']['username']

        # Prints to terminal message sent
        print("\n"
              "Parsing new message from user {}, chat_id = {}\n"
              "Message > {}\n".format(update_data['user'], update_data['id'], update_data['text']))

        if not update_data['text'] or not update_data['id']:
            return False
        else:
            return update_data

    @staticmethod
    def make_json(chat_id, text, keyboard=None):
        if keyboard:
            json_data = {
                'chat_id': chat_id,
                'text': text,
                'reply_markup': json.dumps(keyboard)
            }
        else:
            json_data = {
                'chat_id': chat_id,
                'text': text,
            }

        return json_data

    def send_message(self, text_to_send, receiver_id, receiver_user, inline_keyboard=None):

        json_data = self.make_json(receiver_id, text_to_send)
        http_response = requests.get(self.base_url + "sendMessage", data=json_data)
        if http_response.status_code == 200:
            print('\nMessage successfully sent to user {}, chat_id = {},\n'
                  'Message > {}\n'.format(receiver_user, receiver_id, text_to_send))
            return True
        else:
            print('Error delivering message, HTTP response {}'.format(http_response.status_code))
            return False
