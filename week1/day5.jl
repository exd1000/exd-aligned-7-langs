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

# 2. memory_drift_loop()
# Loop through 5 sample memory states and print conditional responses

# 3. check_drift(state)
# Return “Stable”, “Drifting…”, or “Destabilized”

# 4. signal_response(threshold)
# Return graded response depending on signal strength (like a soft max behavior!)

# 5. benji_vibes()
# Print a randomly chosen comforting Benji message, timestamped with Dates.now()
