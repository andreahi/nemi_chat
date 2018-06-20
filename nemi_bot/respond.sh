#!/usr/bin/env bash

curl -XPOST localhost:5005/conversations/654654/respond -d '{"query":"Hvor mye data har jeg brukt på 99999999"}' | python -mjson.tool