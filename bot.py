import time
import schedule
import requests
import random


def send(bot_message):

    bot_token = '1515603394:AAHsfio0thgzKcmLGKqSh7uZuWrUP_5u-rI'
    # bot_chatID = '739035170'
    bot_chatID = '841442500'
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
    send(f"Dikkkuu{heartEmoji}")
    send(f"Good Morning{kissEmoji}")
    send(f"I love you so much{heartEmoji}")
    send(f"{heartEmoji}{line}{heartEmoji}")
    send(heartEmoji)
    send(kissEmoji)


schedule.every().day.at("7:00").do(fetchShayri)

while True:
    schedule.run_pending()
    time.sleep(1)
