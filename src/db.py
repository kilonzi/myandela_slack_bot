# from .config import SLACK_BOT_TOKEN
from .config import MONGO_USERNAME, MONGO_PASSWORD, MONGO_DB, FIREBASE_URL

# import pymongo
from firebase import firebase
from datetime import datetime

# print(MONGO_USERNAME, MONGO_PASSWORD, MONGO_DB)

firebase = firebase.FirebaseApplication(FIREBASE_URL, None)


# connection_string = "mongodb+srv://{}:{}@cluster0.sbzd7.mongodb.net/{}?retryWrites=true&w=majority".format(
#     MONGO_USERNAME, MONGO_PASSWORD, MONGO_DB)
# client = pymongo.MongoClient(connection_string)
# db = client.weekly_checks


def parse_submission(data):
    state = data["view"]["state"]["values"]
    body = {
        "submitted_on": datetime.now(),
        "team_id": data["team"]["id"],
        "team_domain": data["team"]["domain"],
        "user_id": data["user"]["id"],
        "user_username": data["user"]["username"],
        "user_fullname": data["user"]["name"],
        "trigger_id": data["trigger_id"],
        "recommend_work": state["block_recommend"]["recommend_work"]["value"],
        "good_stuff": get_select_options(
            state["block_good_stuff"]["text_good_stuff"]["selected_options"]
        ),
        "frustrations": get_select_options(
            state["block_frustrations"]["text_frustrations"]["selected_options"]
        ),
        "recent_accomplishments": state["block_recent_accomplishments"][
            "recent_accomplishments"
        ]["value"],
        "blockers": state["block_any_blockers"]["any_escalations"]["value"],
    }
    return body


def get_select_options(options):
    selected = []
    for option in options:
        selected.append(option["value"])
    return selected


def save_check_in(data):
    body = parse_submission(data)
    result = firebase.post(
        "/checks", body, {"print": "pretty"}, {"X_FANCY_HEADER": "VERY FANCY"}
    )
    print(result)
    return result
