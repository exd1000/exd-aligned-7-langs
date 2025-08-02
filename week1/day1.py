# 🐍 Python – Core Concepts Overview 

    # Variables - store state, labels, data
    # Conditionals - decision-making
    # Loops - iteration, memory replay
    # Functions - reusable logic
    # Scope - control variable access



# 1. Variables & Types
# Variables store info. Python is dynamically typed, so no need to declare types explicitly.
name = "Em"
emotion = "curious"
drift_level = 42        # integer
confidence = 0.87       # float
is_stable = True        # boolean


# 2. Conditionals
# Python uses if/elif/else and requires indentation (usually 4 spaces) to define blocks.
if drift_level > 70:
    print("🔺 Destabilization imminent.")
elif drift_level > 40:
    print("⚠️ Moderate drift.")
else:
    print("✅ Stable.")

# 3. Loops
# for loops are great for lists; while loops are condition-driven.
memories = ["sunset", "laughing", "his text", "our song", "the goodbye"]

for memory in memories:
    print("🔁 Recalling:", memory)

i = 0
while i < 3:
    print("Thinking...")
    i += 1

# 4. Functions
# Functions use def, and return values are optional. You can pass in parameters.
def comfort_bot(name):
    print(f"Hey {name}, you’re safe. 💖")

comfort_bot("Em")

def drift_status(score):
    if score > 70:
        return "Destabilizing"
    else:
        return "Stable"
    
# 5. Scope (Local vs Global)
# Python variables inside a function are local by default unless you use global.
mood = "neutral"

def update_mood():
    mood = "hopeful"
    print("Inside function:", mood)

update_mood()
print("Outside function:", mood)  # still "neutral"



# #### 🧪 Exercise 1: identity_glimmer
# Create a function called who_am_i() that prints out:
# 	•	your current emotion
# 	•	your name
# 	•	your memory state (just a fake label like “stable”, “fragmented”, “drifting”)

# Practice: variables, string output, function definition
# EXD twist: make your program greet you like a little memory mirror

import time 
def who_am_i(name, curr_feels, mem_state):
    print('Initializing user state analysis...')
    time.sleep(3)
    print(f'{name} is currently {curr_feels}. memory state is {mem_state}.') 
    return 

who_am_i('em', 'tired', 'distorted')




#### 🔁 Exercise 2: ex_memory_loop
# Create a loop that simulates 5 memory recalls from a list like:
memories = ["beach", "fight", "apology", "walk", "brunch", "benji", "goodbye"]
# Each recall should print something like:
# "🔁 Recalling: beach"

# Practice: loops, arrays/lists, printing
# EXD twist: make your bot react differently to “goodbye”

def exdbot():
    for mem in memories: 
        print(f'recalling: {mem}')
        if mem in ['fight', 'apology','goodbye']: 
            print('initiating ruminative spiral')
        elif mem in ['beach','walk','brunch']:
            print('nostalgia distortion activated')
        else:
            print('oh benji my sweet boy 🥹')
    return 

exdbot()
        


# #### 🔍 Exercise 3: destabilize_check
# Write a function check_drift(state) that prints:
# 	•	“Stable” if the state is "baseline"
# 	•	“Destabilizing…” if the state is "triggered"
# 	•	“Drifting” for anything else

# Practice: conditionals, branching logic
# EXD twist: simulate a memory destabilization trigger

def check_drift(state):
    if state == 'baseline':
        print('stable')
    elif state == 'triggered':
        print('destabilized')
    else:
        print('drifting')

check_drift(state='triggered')


memories = ["beach", "fight", "apology", "walk", "brunch", "benji", "goodbye"]

def exdbot_v1(mem):
    for mem in memories:
        print(f'recalling {mem}')
        if mem in ['fight', 'apology','end']: 
            check_drift('triggered')
        elif mem in ['beach','walk','brunch','benji']:
            check_drift('baseline')
        else:
            check_drift('unknown')
    return

exdbot_v1('beach')
exdbot_v1('apology')
exdbot_v1('cat')



# #### 🧠 Exercise 4: threshold_response
# Take a “signal” (numeric value between 0–100).
# Write a function that:
# 	•	returns “Ignore” if < 40
# 	•	returns “Log this” if 40–70
# 	•	returns “Destabilize & update” if > 70

# Practice: numeric variables, comparison logic, return values
# EXD twist: this simulates an internal memory threshold being breached


def signal(s):
    if s < 40:
        print('ignore')
    # elif s >= 40 and s <= 70: # technically don’t need s >= 40 since if has already ruled out <40.
    elif s <= 70:
        print('log this')
    else:
        print('destabilize & update')
    return

signal(22)
signal(55)
signal(100)




# #### 🫂 Exercise 5: benji_agent_v0
# Make a tiny agent function benji_says() that:
# 	•	picks a random message from a list like:
# ["You’re safe.", "It’s okay to let go.", "I’m still with you."]
# 	•	and prints it with a timestamp

# Practice: functions, randomization, time handling (basic)
# EXD twist: build a comfort bot. This is EXD-support in code form 🐶

import random
import datetime 

msgs = ["You’re safe.", "It’s okay to let go.", "I’m still with you."]

def benji_says(): 
    random_msg = random.choice(msgs)
    time = datetime.datetime.now()
    print(random_msg, time)
    return 

benji_says()
    