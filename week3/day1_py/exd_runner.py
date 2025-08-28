# exd_runner.py
# 	•	Create a script that ties everything together:
# 	•	Loads from config
# 	•	Calls module functions
# 	•	Runs the CLI
# 	•	Acts as a central entry point with a main() function

import json
from exd_module import stabilize, destabilize
from exd_cli import mood_status
from scene_writer import save_states, save_drift_log, load_drift_log
import os


def load_config(path='config.json'):
    if not os.path.exists(path):
        print('No file found')
        return {}
    with open(path, 'r') as f: 
        config = json.load(f)
    print(f'loaded config: {config}')
    return config

def load_memory(path='memory.json'):
    if not os.path.exists(path):
        print('No file found')
        return {}
    with open('memory.json') as f:
        memories = json.load(f)
    for mem, emo in memories.items():
        print(f'{mem}: {emo}')
    return memories 

def main(): 
    config = load_config()
    memories = load_memory()

    mood_status()

    states = ["happy","sad","calm", "sleepy", "confused", "annoyed", "tired"]
    drift_log = {"happy":"10:45", "sad":"8:29", "curious":"3:23"}

    save_states(states)
    save_drift_log(drift_log)

    reloaded = load_drift_log()
    print(reloaded)

if __name__ == '__main__':
    main()
    