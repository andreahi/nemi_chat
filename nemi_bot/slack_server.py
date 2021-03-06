#!/usr/bin/env bash

import subprocess
import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""

subprocess.call(["python3", "-m" "rasa_core.run",
                 "-d", "models/current/dialogue",
                 "-u", "models/current/nlu",
                 "--connector", "slack",
                 "--credentials", "slack_credentials.yml",
                 ])


