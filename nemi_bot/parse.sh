#!/usr/bin/env bash

curl -XPOST localhost:5005/conversations/test/parse -d '{"query":"Hvor mye data har jeg brukt på 91158634"}' | python3 -m json.tool