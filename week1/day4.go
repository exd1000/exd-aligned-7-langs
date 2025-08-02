// 🏃 Day 4 – Go: Syntax & Core Logic

// Go is statically typed, compiled, and built for simplicity, speed, and concurrency. 

package main

import (
	"fmt"
	"time"
	"math/rand"
)

func main() {
	// 1. Variables & Types
	var year int = 2025
	var theme string = "regeneration"
	var ready bool = false
	var energy float64 = 88.5

	// Short declaration (inside functions only)
	location := "memory palace"

	// 2. Conditionals
	temperature := 98.6

	if temperature > 100 {
		fmt.Println("Too hot to hold.")
	} else if temperature < 97 {
		fmt.Println("A little cold-hearted today?")
	} else {
		fmt.Println("You’re just right.")
	}


	// 3. Loops (For + While Style)
		// Traditional for-loop
		for i := 1; i <= 5; i++ {
			fmt.Println("Iteration", i)
		}

		// Range loop
		colors := []string{"blue", "violet", "gold"}
		for index, color := range colors {
			fmt.Printf("Color %d: %s\n", index, color)
		}

		// While-style loop
		counter := 0
		for counter < 3 {
			fmt.Println("Still processing...")
			counter++
		}

	// 4. Functions
		// Function with no return
		func sayHi(name string) {
			fmt.Printf("👋 Hi, %s!\n", name)
		}

		// Function with one return
		func double(x int) int {
			return x * 2
		}

	// Function with multiple return values
	func swap(a, b string) (string, string) {
		return b, a
	}

	// 5. Scope (Local vs Global)
	var mode = "default" // Global scope

	func toggleMode() {
		mode := "experimental" // Local shadow
		fmt.Println("Inside:", mode)
	}

	func showMode() {
		fmt.Println("Outside:", mode)
	}

	// 6. Random + Time
	func coinFlip() {
		rand.Seed(time.Now().UnixNano())
		outcomes := []string{"heads", "tails"}
		fmt.Println("🪙 Result:", outcomes[rand.Intn(2)])
	}

	func timestampedNote() {
		now := time.Now()
		fmt.Printf("🕒 Logged at: %s\n", now.Format("Mon Jan 2 15:04:05 MST 2006"))
	}



	// Exercise 1: identityGlimmer
	// Goal: Create a whoAmI function that:
	// 	•	Prints your name, current emotion, and memory state.

	// Exercise 2: exMemoryLoop
	// Goal: Write a recallMemories function that loop through memories.Respond differently based on the memory.
	recallMemories([]string{"beach", "fight", "apology", "walk", "brunch", "benji", "end"})

	// Exercise 3: destabilizeCheck
	// Goal: Write a checkDrift function that returns “Stable”, “Destabilizing…”, or “Drifting” based on input.

	// Exercise 4: thresholdResponse
	// Goal: Create a thresholdResponse function and return response based on signal strength.
		// returns “Ignore” if < 40
		// returns “Log this” if 40–70
		// returns “Destabilize & update” if > 70

	// Exercise 5: benjiAgentV0
	// Goal: Print a comforting message randomly, with a timestamp.

	// import (
	// 	"math/rand"
	// 	"time"
	// )


}