# scene_writer.py
# 	•	Save a vector of states or current drift to a file (any format).
import pickle 

def save_states(states, path='states.txt'):
    with open(path, "w") as f: 
        for state in states:
            f.write(f"{state}\n")


def save_drift_log(log, path='save.pkl'):
    with open(path, 'wb') as f:
        pickle.dump(log, f)

def load_drift_log(path='save.pkl'):
    with open(path, 'rb') as f:
        return pickle.load(f)


