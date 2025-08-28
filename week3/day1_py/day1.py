# 🧠 Week 3 – Python: Modular Code, CLI Tools, Integration

# 1. Modules & Imports
    # math_utils.py
    # def square(x):
    #     return x * x

   # main.py
    # from math_utils import square

    # print(square(4))  # 16


# 2. Multi-file Project Structure
    # project/
    # ├── main.py
    # ├── utils/
    # │   ├── __init__.py
    # │   └── io_tools.py

    # utils/io_tools.py
    # def read_text(path):
    #     with open(path) as f:
    #         return f.read()
        
    # main.py
    # from utils.io_tools import read_text

    # print(read_text("example.txt"))


# 3. __main__ and Script Execution
# Run from terminal: python script.py
    # script.py
    # def hello():
    #     print("Hello from a function!")

    # if __name__ == "__main__":
    #     hello()


# 4. CLI Tools with argparse
    # Run: python cli_greet.py --name Emily
    # import argparse

    # parser = argparse.ArgumentParser()
    # parser.add_argument("--name", help="Your name")
    # args = parser.parse_args()

    # print(f"Hello, {args.name}!")


# 5. Lightweight Config (.json / .yaml)
    # config.json
    # {
    # "mode": "train",
    # "learning_rate": 0.01
    # }

    # Python:
    # import json

    # with open("config.json") as f:
    #     config = json.load(f)

    # print(config["mode"])  # "train"


# 6. Dependency Tracking (requirements.txt)
    # Create file:
        # numpy==1.26.0
        # pandas>=2.0.0
    # Terminal:
        # pip install -r requirements.txt

# 7. Virtual Environment (venv)
    # python -m venv venv
    # source venv/bin/activate  # Mac/Linux
    # venv\Scripts\activate     # Windows
    # pip install pandas

# 8. File I/O
    # .txt
    # with open("notes.txt", "w") as f:
    #     f.write("Memory is a strange mirror.\n")

    # .json
    # import json

    # data = {"emotion": "hope", "intensity": 0.8}
    # with open("emotion.json", "w") as f:
    #     json.dump(data, f)

    # .csv
    # import csv

    # with open("log.csv", "w", newline="") as f:
    #     writer = csv.writer(f)
    #     writer.writerow(["time", "state"])
    #     writer.writerow(["0", "stable"])


# 9. Reading JSON / CSV
    # .json
    # with open("emotion.json") as f:
    #     loaded = json.load(f)
    # print(loaded["emotion"])

    # # .csv
    # with open("log.csv") as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         print(row)


# 10. Serialization (Pickle)
    # import pickle

    # data = {"name": "Emily", "model": "EXD-Net"}

    # with open("save.pkl", "wb") as f:
    #     pickle.dump(data, f)

    # with open("save.pkl", "rb") as f:
    #     restored = pickle.load(f)

    # print(restored["model"])  # EXD-Net



# 11. Directory Layout Example (Larger Project)
    # exd_net/
    # ├── __main__.py
    # ├── config/
    # │   └── default.json
    # ├── core/
    # │   ├── memory.py
    # │   └── drift.py
    # ├── utils/
    # │   └── logger.py
    # ├── run.py
    # ├── requirements.txt
    # └── README.md

    # run.py
    # from core.memory import MemoryBank
    # from utils.logger import log_state




# 💖 EXD-Aligned Exercises 


# exd_module.py
# 	•	Create a module with at least 2 functions: stabilize() and destabilize()
# 	•	Each should print something emotionally dramatic
# 	•	Import it from another script and call them
from exd_module import stabilize, destabilize

stabilize()
destabilize()


# exd_cli.py
# 	•	Build a CLI tool using argparse
# 	•	Options:
# 	•	--mood to specify emotional state
# 	•	--trigger to log an external stimulus
# 	•	Output should reflect memory destabilization impact


from exd_cli import mood_status

mood_status()

# run in terminal:
    # python main.py --trigger photo --mood sad 




# memory_loader.py
# 	•	Load emotional memory data from a .json or .yaml file
# 	•	File should contain at least 3 memory → emotion mappings
# 	•	Loop and print them with intensity ratings


import json

with open("memory.json") as f: 
    memories = json.load(f)
for mem in memories:
    print(memories[mem])

# again is another .py file really necessary


# scene_writer.py
# 	•	Save a vector of states or current drift to a file (any format).

state_vect = ["happy","sad","calm", "sleepy", "confused", "annoyed", "tired"]
with open("states.txt", "w") as f: 
    for state in state_vect:
        f.write(f"{state}\n")


# 	•	Serialize state over time (log drift or memory snapshots to a file).



import pickle 

drift_log = {"happy":"10:45", 
             "sad":"8:29",
             "curious":"3:23"}

with open("save.pkl", "wb") as f: 
    pickle.dump(drift_log,f)

with open("save.pkl", "rb") as f: 
    reopen = pickle.load(f)

print(reopen)



# run_simulation.py
# 	•	Load a config (e.g., config.json) and execute model logic from it.

with open("config.json") as f: 
    config = json.load(f)

print(config["model"])


# exd_runner.py
# 	•	Create a script that ties everything together:
# 	•	Loads from config
# 	•	Calls module functions
# 	•	Runs the CLI
# 	•	Acts as a central entry point with a main() function