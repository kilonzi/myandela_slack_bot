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
        # Call views.publish with the built-in client
        client.views_publish(
            # Use the user ID associated with the event
            user_id=event["user"],
            # Home tabs must be enabled in your app configuration
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
    # Acknowledge the command request
    ack()
    # Call views_open with the built-in client
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
        # View payload
        view={
            "type": "modal",
            # View identifier
            "callback_id": "view_1",
            "title": {"type": "plain_text", "text": "Weekly Check In"},
            "submit": {"type": "plain_text", "text": "Submit"},
            "blocks": [
                # {
                #     "type": "section",
                #     "text": {"type": "mrkdwn", "text": "Welcome to a modal with _blocks_"},
                #     "accessory": {
                #         "type": "button",
                #         "text": {"type": "plain_text", "text": "Click me!"},
                #         "action_id": "button_abc"
                #     }
                # },
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
                    "label": {"type": "plain_text", "text": "Do you have any blockers?"},
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "any_blockers",
                        "multiline": True
                    }
                },
                # {
                #     "label": "What are the top 3 things that causing you frustration?",
                #     "type": "select",
                #     "name": "frustrating_things",

                {
                    "type": "input",
                    "block_id": "block_working_things",
                    "label": {"type": "plain_text", "text": "What are the top 3 things that are working for you?"},
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "working_things",
                        "multiline": True
                    }
                },
                {
                    "type": "input",
                    "block_id": "block_frustrating_things",
                    "label": {"type": "plain_text", "text": "What are the top 3 things that causing you frustration?"},
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "frustrating_things",
                        "multiline": True
                    }
                },
                {
                    "type": "section",
                    "block_id": "section678",
                    "text": {
                            "type": "mrkdwn",
                                "text": "Pick items from the list"
                    },
                    "accessory": {
                        "action_id": "text1234",
                        "type": "multi_static_select",
                        "placeholder": {
                                "type": "plain_text",
                                "text": "Select items"
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
                                    "text": "Partner support issues"
                                },
                                "value": "Partner support issues"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Partner support issues"
                                },
                                "value": "Partner support issues"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Partner support issues"
                                },
                                "value": "Partner support issues"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Partner support issues"
                                },
                                "value": "Partner support issues"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Partner support issues"
                                },
                                "value": "Partner support issues"
                            }
                        ]
                    }
                }
            ]
        }
    )


                #         {
                #             "label": "Unfair workload",
                #             "value": "Unfair_workload"
                #         }
                #         # {
                #         #     "label": "Partner support issues",
                #         #     "value": "Partner support issues"
                #         # },
                #         # {
                #         #     "label": "Unclear requirements and priorities",
                #         #     "value": "Unclear requirements and priorities"
                #         # },
                #         # {
                #         #     "label": "Not my preferred tech stack",
                #         #     "value": "Not my preferred tech stack"
                #         # }, {
                #         #     "label": "Lack of work",
                #         #     "value": "Lack of work"
                #         # }, {
                #         #     "label": "Andela Policies",
                #         #     "value": "Andela Policies"
                #         # }, {
                #         #     "label": "Promotions and Compensation",
                #         #     "value": "Promotions and Compensation"
                #         # }, {
                #         #     "label": "Lack of Growth",
                #         #     "value": "Lack of Growth"
                #         # }, {
                #         #     "label": "Work-From-Home Setup",
                #         #     "value": "Work-From-Home Setup"
                #         # }, {
                #         #     "label": "Work-Life Balance",
                #         #     "value": "Work-Life Balance"
                #         # }
                #     ]
                # },

bot.action("button_abc")


def select_user(ack, action, respond):
    ack()
    respond(f"You selected <@{action['selected_user']}>")
