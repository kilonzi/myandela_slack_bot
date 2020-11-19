import os
from dotenv import load_dotenv
load_dotenv(override=True)

SLACK_BOT_TOKEN=os.getenv('SLACK_BOT_TOKEN')
SLACK_SIGNING_SECRET=os.getenv('SLACK_SIGNING_SECRET')
PORT=3000