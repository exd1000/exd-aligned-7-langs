# 🧬 Day 5 – Julia: Core Syntax & Logic

# 1. Variables & Types
year = 2025                    # Inferred type
emotion::String = "loopy"     # Explicit type
energy = 98.7

# 2. Conditionals
temp = 98.6
if temp > 100
    println("Too hot to hold.")
elseif temp < 97
    println("Feeling cold-hearted?")
else
    println("You’re just right.")
end

# 3. Loops
    # For loop
    for i in 1:5
        println("Looping ", i)
    end

    # While loop
    counter = 0
    while counter < 3
        println("Still stabilizing…")
        counter += 1
    end

# 4. Functions
    # Basic function
    function greet(name)
        println("Hi, ", name)
    end

    # Function with return
    double(x) = x * 2

    # Multiple return values
    function swap(a, b)
        return b, a
    end

# 5. Scope
mode = "default"  # Global

function toggle_mode()
    local mode = "experimental"
    println("Inside:", mode)
end

toggle_mode()
println("Outside:", mode)


# The ! convention (toggle_mode!) is idiomatic in Julia to indicate mutation.
global mode = "default"

function toggle_mode!()
    global mode = "experimental"
    println("Mode changed to: $mode")
end


# 6. Random + Time
using Random
using Dates

Random.seed!(123)
choices = ["heads", "tails"]
println("🪙", rand(choices))

now = Dates.now()
println("🕒 Time is: ", now)



# 1. identity_glimmer()
# Create a function that prints your name, current emotion, and EXD state

function who_am_i(name, curr_emo, exd_state)
    println("Hi $name. I see you're feeling $curr_emo and $exd_state.")
end

who_am_i("em", "meh", "distorted")
# 2. memory_drift_loop()
# Loop through sample memory states and print conditional responses
memories = ["beach", "fight", "apology", "walk", "brunch", "benji", "ex"]
for mem in memories
    if mem in ["beach", "walk", "brunch"]
        println("$mem: cool")
    elseif mem in ["fight", "apology", "ex"]
        println("$mem: ew")
    else 
        println("$mem: 🥺")
    end
end 



# 3. check_drift(state)
# Return “Stable”, “Drifting…”, or “Destabilized”
function check_drift(state) 
    if state == "baseline"
        println("stable") 
    elseif state == "triggered"
        println("destable")
    else 
        println("drifted")
    end
end

check_drift("baseline")
check_drift("triggered")
check_drift("yo")

# 🧠 Use == instead of === unless you’re intentionally checking object identity
# (which is rare and unnecessary for strings like "baseline").
# got confused between == and === usage like why 🥺


# ⚠️ Interesting note:
    # println(...) → shows it now but doesn’t give you back a value
    # return ... → gives you a value you can use later (or test, or pass along, or transform)

# You can always do both if you want feedback and utility:
function check_drift(state)
    result = state == "baseline" ? "Stable" :
             state == "triggered" ? "Destabilized" : "Drifting"
    println("Drift status: $result")
    return result
end

check_drift("baseline")
check_drift("triggered")
check_drift("yo")





# 4. signal_response(threshold)
# Return graded response depending on signal strength (like a soft max behavior!)
    # returns “Ignore” if < 40
    # returns “Log this” if 40–70
    # returns “Destabilize & update” if > 70
function signal_response(threshold)
    if threshold < 40 
        println("$threshold: ignore")
    elseif threshold <= 70 
        println("$threshold: log this")
    else 
        println("$threshold: destabilize & update")
    end
end

signal_response(22)
signal_response(44)
signal_response(77)

# ⭐ Return instead of println (for most utility functions)
# use return then call println(signal_response(77))
# This makes the function more composable and testable later.
 
# sigh i didn't want to println the function that's why but okie dokie

# 5. benji_vibes()
# Print a randomly chosen comforting Benji message, timestamped with Dates.now()
using Random
using Dates

function benji_vibes()
    Random.seed!(12)
    choices = ["woof!", "hi", "are you done yet", "can we go now"]
    msg = rand(choices)
    now = Dates.now()
    println("[$now]: Benji says '$msg'")
end

benji_vibes()

# ⚠️ Random Usage:
# You used Random.seed!(123) and Random.seed!(12) in the same file — 
# just make sure you know that reseeding multiple times resets the RNG state. 
# That’s fine here, just flagging it for when you’re debugging repeatability.