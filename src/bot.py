import requests
from .config import SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET
from slack_bolt import App
from .db import save_check_in

bot = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET
)


@bot.event("app_home_opened")
def update_home_tab(client, event, logger):
    try:
        client.views_publish(
            user_id=event["user"],
            view={
                "type": "home",
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Welcome, <@" + event["user"] + ">,* I hope you have had a nice week"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*We would like to know what you have been working on, the feedback will be reviewed and used in your performance evaluation.*"
                        }
                    },
                    {
                        "type": "actions",
                        "elements": [
                                {
                                    "type": "button",
                                    "text": {
                                            "type": "plain_text",
                                        "text": "Fill your Check In"
                                    },
                                    "style": "primary",
                                    "action_id": "submit_weekly_check_in_button"
                                }
                        ]
                    }
                    # {
                    #     "type": "section",
                    #     "text": {
                    #         "type": "mrkdwn",
                    #         "text": "*Fill your Weekly Check In*"
                    #     },
                    #     "accessory": {
                    #         "type": "button",
                    #         "text": {"type": "plain_text", "text": "Fill Form"},
                    #         "action_id": "submit_weekly_check_in_button"
                    #     },
                    # }
                ]
            }
        )

    except Exception as e:
        logger.error(f"Error opening modal: {e}")


@bot.action("submit_weekly_check_in_button")
def open_modal(ack, body, client):
    # user = body['user']['id']
    username = body['user']['username']
    ack()
    client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "weekly_checkin_view",
            "title": {"type": "plain_text", "text": "Weekly Check In"},
            "submit": {"type": "plain_text", "text": "Submit"},
            "blocks": [
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                            "type": "plain_text",
                        "text": ":wave: Hey <@"+username+">!\n\nWe'd love to hear from you how we can make this place the best place you’ve ever worked.",
                                "emoji": True
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "input",
                    "block_id": "block_recommend",
                    "label": {
                        "type": "plain_text",
                        "text": "On a scale of 0 - 10, How likely is it you would recommend Andela as a place to work? (0 = Not at all, 10 = Absolutely)"},
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "recommend_work",
                        "multiline": False,
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Your score"
                        }
                    }
                },

                {
                    "type": "section",
                    "block_id": "block_good_stuff",
                    "text": {
                            "type": "mrkdwn",
                                "text": "*What things are working for you?*"
                    },
                    "accessory": {
                        "action_id": "text_good_stuff",
                        "type": "multi_static_select",
                        "placeholder": {
                                "type": "plain_text",
                                "text": "Select "
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Great partner team"
                                },
                                "value": "Great partner team"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Reasonable workload"
                                },
                                "value": "Reasonable workload"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Strong partner support"
                                },
                                "value": "Strong partner support"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Clear requirements & priorities"
                                },
                                "value": "Clear requirements & priorities"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Preferred Tech Stack"
                                },
                                "value": "Preferred Tech Stack"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Andela Policies"
                                },
                                "value": "Andela Policies"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Promotions and Compensation"
                                },
                                "value": "Promotions and Compensation"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Lack of Growth"
                                },
                                "value": "Lack of Growth"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Work-From-Home Setup"
                                },
                                "value": "Work-From-Home Setup"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Work-Life Balance"
                                },
                                "value": "Work-Life Balance"
                            }
                        ]
                    }
                },
                {
                    "type": "section",
                    "block_id": "block_frustrations",
                    "text": {
                            "type": "mrkdwn",
                                "text": "*What things are causing you frustration?*"
                    },
                    "accessory": {
                        "action_id": "text_frustrations",
                        "type": "multi_static_select",
                        "placeholder": {
                                "type": "plain_text",
                                "text": "Select "
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Difficult partner environment"
                                },
                                "value": "Difficult partner environment"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Unfair workload"
                                },
                                "value": "Unfair workload"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Unclear requirements and priorities"
                                },
                                "value": "Unclear requirements and priorities"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Not my preferred tech stack"
                                },
                                "value": "Not my preferred tech stack"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Lack of work"
                                },
                                "value": "Lack of work"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Andela Policies"
                                },
                                "value": "Andela Policies"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Promotions and Compensation"
                                },
                                "value": "Promotions and Compensation"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Lack of Growth"
                                },
                                "value": "Lack of Growth"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Work-From-Home Setup"
                                },
                                "value": "Work-From-Home Setup"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Work-Life Balance"
                                },
                                "value": "Work-Life Balance"
                            }
                        ]
                    }
                },
                {
                    "type": "input",
                    "block_id": "block_recent_accomplishments",
                    "label": {"type": "plain_text", "text": "What did you accomplish in the last 7 days?"},
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "recent_accomplishments",
                        "multiline": True,
                        "placeholder": {
                            "type": "plain_text",
                            "text": "My most recent accomplishments are :-"
                        }
                    }
                },
                {
                    "type": "input",
                    "block_id": "block_any_blockers",
                    "label": {"type": "plain_text", "text": "What would you like to escalate?"},
                    "optional": True,
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "any_escalations",
                        "multiline": True,
                        "placeholder": {
                            "type": "plain_text",
                            "text": "I would like to escalate"
                        }
                    }
                },
            ]
        }
    )

    # Handle a view_submission event


@bot.view("weekly_checkin_view")
def handle_submission(ack, body, client, view):
    ack()
    respond_to_submission(client, body)
    return save_check_in(body)


def respond_to_submission(client, body):
    user = body["user"]["id"]
    username = body["user"]["username"]
    msg = ""
    try:
        msg = f"Hey, <@{username}> submission of was successful. We will review and get back to you if we have any questions"
    except Exception as e:
        msg = "There was an error with your submission"
    finally:
        client.chat_postMessage(channel=user, text=msg)

@bot.action("text_frustrations")
def select_frustrations(ack, action, respond, say):
    ack()


@bot.action("text_good_stuff")
def select_good_stuff(ack, action, respond, say):
    ack()


@bot.action("recommend_work")
def recommend_work(ack, action, respond, say):
    print(action)
    ack()


def respond_back(url):
    data = {
        "text": "Thanks for your request, we'll process it and get back to you."
    }
    return requests.post(url, data=data)
