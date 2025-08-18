# exd_cli.py
# 	•	Build a CLI tool using argparse
# 	•	Options:
# 	•	--mood to specify emotional state
# 	•	--trigger to log an external stimulus
# 	•	Output should reflect memory destabilization impact



import argparse 
from exd_module import stabilize, destabilize

def mood_status(): # main.py as runner 
    parser = argparse.ArgumentParser()
    parser.add_argument("--mood", help="specifies emotional state")
    parser.add_argument("--trigger", help="logs external stim")
    args = parser.parse_args()

    if args.trigger in ["text", "photo", "memories"]: 
        if args.mood in ["sad", "anxious", "nostalgic"]:
            destabilize()
        else: 
            stabilize()


if __name__ == "__main__":
    mood_status()