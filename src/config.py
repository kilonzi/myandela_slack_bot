import os
from dotenv import load_dotenv
load_dotenv(override=True)

SLACK_BOT_TOKEN=os.getenv('SLACK_BOT_TOKEN')
SLACK_SIGNING_SECRET=os.getenv('SLACK_SIGNING_SECRET')
MONGO_USERNAME=os.getenv('MONGO_USERNAME')
MONGO_PASSWORD=os.getenv('MONGO_PASSWORD')
MONGO_DB=os.getenv('MONGO_DB')
FIREBASE_URL=os.getenv('FIREBASE_URL')
PORT=3000