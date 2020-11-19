from config import SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET
from slack_bolt import App

bot = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET
)


@bot.message("message")
def say_hello(message, say):
    print(message)
    user = message['user']
    say(f"Hi there, <@{user}>!")


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
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Fill your Weekly Check In*"
                        },
                        "accessory": {
                            "type": "button",
                            "text": {"type": "plain_text", "text": "Fill Form"},
                            "action_id": "button_abc"
                        },
                    }
                ]
            }
        )

    except Exception as e:
        logger.error(f"Error opening modal: {e}")


@bot.action("button_abc")
def open_modal(ack, body, client):
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
                    "type": "input",
                    "block_id": "block_recent_accomplishments",
                    "label": {"type": "plain_text", "text": "What did you accomplish in the last 7 days"},
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "recent_accomplishments",
                        "multiline": True
                    }
                },
                {
                    "type": "input",
                    "block_id": "block_any_blockers",
                    "label": {"type": "plain_text", "text": "What would you like to escalate?"},
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "any_escalations",
                        "multiline": True
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
                }
            ]
        }
    )


    # Handle a view_submission event
@bot.view("weekly_checkin_view")
def handle_submission(ack, body, client, view):
    # Assume there's an input block with `block_1` as the block_id and `input_a`
    print(view["state"]["values"])
    val = 'Done'
    # val = view["state"]["values"]["block_1"]["input_a"]
    user = body["user"]["id"]
    username = body["user"]["username"]
    # # Validate the inputs
    errors = {}
    if val is not None and len(val) <= 5:
        errors["block_1"] = "The value must be longer than 5 characters"
    if len(errors) > 0:
        ack(response_action="errors", errors=errors)
        return
    # Acknowledge the view_submission event and close the modal
    ack()
    # Do whatever you want with the input data - here we're saving it to a DB
    # then sending the user a verification of their submission

    # Message to send user
    msg = ""
    try:
        # Save to DB
        msg = f"Hey, @{username}submission of {val} was successful"
    except Exception as e:
        # Handle error
        msg = "There was an error with your submission"
    finally:
        # Message the user
        client.chat_postMessage(channel=user, text=msg)


# Listens to actions triggered with action_id of “user_select”
@bot.action("text_frustrations")
def select_frustrations(ack, action, respond):
    ack()
    # respond(f"You selected <@{action['selected_user']}>")

@bot.action("text_good_stuff")
def select_good_stuff(ack, action, respond):
    ack()
    # respond(f"You selected <@{action['selected_user']}>")

