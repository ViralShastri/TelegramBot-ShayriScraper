import time
import schedule
import requests
import random
import os


def send(bot_message):

    bot_token = os.environ["bot_token"]
    bot_chatID = os.environ["bot_chatID"]
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


def fetchShayri():
    line = ''
    while line == "":
        lines = open("shayri.txt", encoding="utf-8").read()
        line = random.choice(lines.split("\n\n"))
    heartEmoji = "\U00002764"
    kissEmoji = "\U0001F48B"
    send(f"{heartEmoji}{kissEmoji}{line}{kissEmoji}{heartEmoji}")


schedule.every().day.at("7:00").do(fetchShayri)

while True:
    schedule.run_pending()
    time.sleep(1)
