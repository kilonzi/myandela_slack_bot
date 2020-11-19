from flask import Flask, request
from config import PORT
from src.bot import bot
from slack_bolt.adapter.flask import SlackRequestHandler

app = Flask(__name__)
handler = SlackRequestHandler(bot)

@app.route("/slack/interactions", methods=["POST"])
def slack_interactions():
    return handler.handle(request)

@app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

if __name__ == "__main__":
    app.run(host='localhost',port=PORT,debug=True)