# Week 4: Debugging & Testing 

# 1. Error Handling (try / except)
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("⚠️ You can't divide by zero.")
        return None
    
# 2. Custom Exceptions
class MemoryOverloadError(Exception):
    pass

def recall_memory(intensity):
    if intensity > 100:
        raise MemoryOverloadError("💥 Emotional overload detected!")
    return "Memory retrieved successfully."


# 3. Logging (using logging)
import logging

logging.basicConfig(level=logging.INFO)
logging.info("EXD-Net system initialized.")
logging.warning("⚠️ Drift rate approaching threshold.")
logging.error("❌ Attractor collapse detected.")

# 4. Debugging Tools
import pdb

def unstable_fn(x):
    pdb.set_trace()  # Drop into debugger
    return x + 1

# 5. Unit Testing (unittest)
import unittest

def stabilize_emotion(state):
    return "stable" if state in ["sad", "angry"] else "neutral"

class TestEmotionFunctions(unittest.TestCase):
    def test_stabilize(self):
        self.assertEqual(stabilize_emotion("sad"), "stable")
        self.assertEqual(stabilize_emotion("happy"), "neutral")

if __name__ == '__main__':
    unittest.main()


# Exercises
# 💖 error_empath.py
# 	•	Create a function that validates emotional input.
# 	•	If the input is unexpected, print a graceful and emotionally supportive error message.
# 	•	Ensure the function does not crash on bad input.

# ⸻

# 💖 destabilization_log.py
# 	•	Use Python’s logging module to log destabilization events.
# 	•	Log events at different severity levels (info, warning, error).
# 	•	Save logs to a file called destabilization.log.

# ⸻

# 💖 test_empathy.py
# 	•	Write unit tests for functions in your EXD model (e.g., stabilize/destabilize).
# 	•	Use unittest or pytest to define multiple test cases.
# 	•	Include both passing and failing scenarios.

# ⸻

# 💖 recovery_wrapper.py
# 	•	Wrap a potentially “emotional” function in a try/except block.
# 	•	Catch custom or built-in exceptions as symbolic “emotional breakdowns”.
# 	•	Include a finally clause that prints a recovery message.

# ⸻

# 💖 agent_trace.py
# 	•	Simulate a memory traceback where an agent replays destabilizing events.
# 	•	Use loops and conditional logic to trace events.
# 	•	If the trace breaks (e.g. bad format), catch the error and print a symbolic fallback message.
