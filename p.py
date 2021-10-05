from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(_name_)
english_bot = ChatBot("ChatterBot", storage_adapter="ChatterBot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))
if _name_ == '_main_':
    app.run()