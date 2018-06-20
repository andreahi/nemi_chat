#!/usr/bin/env bash

curl -XPOST http://localhost:5005/conversations/default/continue -d \
    '{"executed_action": "utter_buy_data"}' | python3 -m json.tool