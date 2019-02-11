from slackclient import SlackClient
import time

SLACK_BOT_TOKEN = "xoxp-547704002851-547209488609-548029262341-c87b58015dc71f15705b74fbc2cd5d6a"
slack_client = SlackClient(SLACK_BOT_TOKEN)

msg = "Hello Slack!"

while True:
    updateMsg = slack_client.api_call(
        "chat.postMessage",
        channel='#general',
        text=msg
    )
    time.sleep(10)