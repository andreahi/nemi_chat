import subprocess

import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""

subprocess.call(["python3", "-m" "rasa_nlu.train",
                 "-c", "nlu_config.yml",
                 "--data", "data_md/",
                 "-o", "models",
                 "--fixed_model_name", "nlu",
                 "--project", "current",
                 "--num_threads", "6",
                 "--debug",
                 ])
subprocess.call(["python3", "-m" "rasa_core.train",
                 "-d", "domain.yml",
                 "-s", "stories/stories.md",
                 "-o", "models/current/dialogue",
                 "--epochs", "20",
                 "--verbose",
                 ])
