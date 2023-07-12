from flask import Flask,request
from telegram import Bot

TOKEN = '6316010799:AAH3KDjpR9HxFBNRJaM-xfKjJTgNshCLQWg'

app = Flask(__name__)
bot = Bot(token=TOKEN)

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method == 'GET':
        return 'Hello World'
    elif request.method == 'POST':
        update = request.get_json()
        chat_id = update['message']['chat']['id']
        text = update['message']['text']

        bot.sendMessage(chat_id=chat_id,text=text)
        return 'ok'
