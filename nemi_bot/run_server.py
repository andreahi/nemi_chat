import os
import subprocess
os.environ["CUDA_VISIBLE_DEVICES"] = ""


subprocess.call(["python3", "-m" "rasa_core.server",
                 "-d", "models/current/dialogue",
                 "-u", "models/current/nlu",
                 ])


