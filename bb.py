from config import PORT,SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET
from slack_bolt import App

# Initializes your app with your bot token and signing secret
bot = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET
)

@bot.message("message")
def say_hello(message, say):
    print(message)
    user = message['user']
    say(f"Hi there, <@{user}>!")

# Start your app
if __name__ == "__main__":
    bot.start(port=PORT)