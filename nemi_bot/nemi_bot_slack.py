import os
import time
import re
from slackclient import SlackClient


# instantiate Slack client
slack_client = SlackClient("xoxb-")
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

import requests
import json
import hashlib

USE_CLARA = False
username_cache = {}
def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            if event["channel"][0]=='D' :#and event['user'] == 'U4CM9TC2K':
                if "go to sleep" in event["text"]:
                    exit(0)
                if USE_CLARA:
                    if event['user'] not in username_cache:
                        firstname = get_user_firstname(event['user'])


                        res = requests.get('http://127.0.0.1:5000/reply',
                                           params={"sessionId": 0, "question": "My name is " + firstname})
                        sessionId = json_to_dict(res.content)["sessionId"]
                        requests.get('http://127.0.0.1:5000/reply',
                                           params={"sessionId": sessionId, "question": "Please call me " + firstname})
                        username_cache[event['user']] = sessionId

                    message = parse_direct_mention(username_cache[event['user']], event["text"])
                else:


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

def parse_direct_mention(sessionId, message_text):

    res = requests.get('http://127.0.0.1:5000/reply', params={"sessionId":sessionId,"question":message_text})

    response = json_to_dict(res.content)
    if response["sessionId"] != sessionId or sessionId == 1:
        username_cache.clear() # the cache is corrupt
    return response["sentence"]


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