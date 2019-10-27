from slackclient import SlackClient
import time

SLACK_BOT_TOKEN = "xoxp-560904392741-560457746483-573665323909-922729fe28cec60eb35ad7709af44d45"
slack_client = SlackClient(SLACK_BOT_TOKEN)

msg = "Hello Slack!"

while True:
    updateMsg = slack_client.api_call(
        "chat.postMessage",
        channel='#general',
        text=msg
    )
    time.sleep(2)
