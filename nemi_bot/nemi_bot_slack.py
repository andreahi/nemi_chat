# coding=utf-8
import time
from slackclient import SlackClient


slack_client = SlackClient("xoxb-12629735638-381575587716-kizBdLSqzdmGvgaCPgomXVF4")
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

import requests
import json

username_cache = {}
def parse_bot_commands(slack_events):

    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            if event["channel"][0]=='D' :#direct message
                if "go to sleep" in event["text"]:
                    exit(0)

                parse_res = requests.post('http://localhost:5005/conversations/'+event['user']+'/parse',
                                   json={"query": event["text"]})
                parse_res = json_to_dict(parse_res.content)
                print("parse_res: ", parse_res)
                confidence = parse_res["tracker"]["latest_message"]["intent"]["confidence"]
                if confidence > 0.7:
                    res = requests.post('http://localhost:5005/conversations/'+event['user']+'/respond',
                                       json={"query": event["text"]})

                    message = json_to_dict(res.content)[0]['text']
                else:
                    message = "Jeg forstår desverre ikke hva du mener. Hvis mulig formuler deg på en annen måte. Eller så kan snakke med en av mine kolegaer på tlf: 915 09000"

                return message, event["channel"]
    return None, None

def get_user_firstname(userId):

 user_info = slack_client.api_call(
        "users.info",
     user=userId
    )
 return user_info["user"]["profile"]["first_name"]


def json_to_dict(content):
    str_response = content.decode('utf-8')
    return json.loads(str_response)


def string2numeric_hash(text):
    import hashlib
    return int(hashlib.md5(text.encode('utf-8')).hexdigest()[:8], 16)

def handle_command(command, channel):

    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=command
    )

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")