# 🧠 Week 2 – Data Structures in Python

# 1. Lists – ordered, mutable collections
memories = ["beach", "fight", "apology"]
memories.append("brunch")
print(memories[0])  # 'beach'

# 2. Dictionaries (dict) – key-value pairs (associative memory)
memory_bank = {
    "beach": "calm",
    "fight": "tense",
    "brunch": "warm"
}
print(memory_bank["beach"])  # 'calm'

# 3. Sets – unordered, no duplicates
scene_set = {"beach", "brunch", "fight", "beach"}
print(scene_set)  # {'beach', 'brunch', 'fight'}

# 4. Tuples – immutable ordered collections
timeline_tuple = ("walk", "hug", "goodbye")
print(timeline_tuple[1])  # 'hug'

💖 EXD-Aligned Practice Prompts


1. memory_bank
Use a dictionary to store memory:emotion pairs
Add a few entries and print the emotional tone of “brunch”

2. scene_set
Use a set to store memory labels. Add a duplicate.
Show that duplicates are removed.

3. timeline_tuple
Make a tuple of 3 meaningful events.
Try to mutate it — see the error!

4. trigger_map
Create a dictionary mapping stimuli (e.g., “text”, “smell”) → emotional responses
Add or update a mapping.

5. em_logbook
Use a list of dictionaries to simulate memory snapshots.
Each dict contains {"time": "14:10", "state": "triggered"}