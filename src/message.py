# This will match any message that contains 👋

from bot import bot

@bot.message("message")
def say_hello(message, say):
    user = message['user']
    say(f"Hi there, <@{user}>!")