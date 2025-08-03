// 🏃 Day 4 – Go: Syntax & Core Logic

// Go is statically typed, compiled, and built for simplicity, speed, and concurrency.

package main

import (
	"fmt"
	"math/rand"
	"time"
)

// 1. Variables & Types
// var year int = 2025
// var theme string = "regeneration"
// var ready bool = false
// var energy float64 = 88.5

// Short declaration (inside functions only)
// location := "memory palace"

// 2. Conditionals
// temperature := 98.6

// if temperature > 100 {
// 	fmt.Println("Too hot to hold.")
// } else if temperature < 97 {
// 	fmt.Println("A little cold-hearted today?")
// } else {
// 	fmt.Println("You’re just right.")
// }

// 3. Loops (For + While Style)
// Traditional for-loop
// for i := 1; i <= 5; i++ {
// 	fmt.Println("Iteration", i)
// }

// Range loop
// colors := []string{"blue", "violet", "gold"}
// for index, color := range colors {
// 	fmt.Printf("Color %d: %s\n", index, color)
// }

// While-style loop
// counter := 0
// for counter < 3 {
// 	fmt.Println("Still processing...")
// 	counter++
// }

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
	fmt.Println("🪙 Result:", outcomes[rand.Intn(len(outcomes))])
}

func timestampedNote() {
	now := time.Now()
	fmt.Printf("🕒 Logged at: %s\n", now.Format("Mon Jan 2 15:04:05 MST 2006"))
}

func examples() {
	sayHi("Em")
	fmt.Println(double(2))
	fmt.Println(swap("em", "eli"))
	toggleMode()
	showMode()
	coinFlip()
	timestampedNote()
}

// Exercise 1: identityGlimmer
// Goal: Create a whoAmI function that:
//   - Prints your name, current emotion, and memory state.
func whoAmI(name string, currentEmo string, memState string) {
	fmt.Printf("Hi, %s. I see you're feeling %s and %s.\n", name, currentEmo, memState)
}

// Exercise 2: exMemoryLoop
// Goal: Write a recallMemories function that loop through memories.Respond differently based on the memory.

func recallMemories(memories []string) {
	for _, mem := range memories {
		fmt.Printf("recalling: %s\n", mem)
		switch mem {
		case "beach", "walk", "brunch":
			fmt.Println("Sounds fun!")
		case "fight", "apology", "end":
			fmt.Println("Yikes!")
		default:
			fmt.Println("Woof! 🐶")
		}
	}
}

// ❌ Go string types don't have Contains
// func recallMemories(memories []string) {
// 	for _, mem := range memories {
// 		if mem.Contains("beach", "walk", "brunch") {
// 			fmt.Printf("Recalling: %s", mem)
// 			fmt.Println("Sounds fun!")
// 		} else if mem.Contains("fight", "apology", "end") {
// 			fmt.Printf("Recalling: %s", mem)
// 			fmt.Println("Yikes!")
// 		} else {
// 			fmt.Println("Woof! 🐶")
// 		}
// 	}
// }

// Exercise 3: destabilizeCheck
// Goal: Write a checkDrift function that returns “Stable”, “Destabilizing…”, or “Drifting” based on input.
//   - “Stable” if the state is "baseline"
//   - “Destabilizing…” if the state is "triggered"
//   - “Drifting” for anything else
func checkDrift(x string) string {
	if x == "baseline" {
		return "Stable"
	} else if x == "triggered" {
		return "Destabilized"
	} else {
		return "Drifting"
	}
}

// Exercise 4: thresholdResponse
// Goal: Create a thresholdResponse function and return response based on signal strength.
// returns “Ignore” if < 40
// returns “Log this” if 40–70
// returns “Destabilize & update” if > 70

func thresholdResponse(x int) {
	if x < 40 {
		fmt.Printf("%d: ignore\n", x)
	} else if x <= 70 {
		fmt.Printf("%d: log this\n", x)
	} else {
		fmt.Printf("%d: destabilize & update\n", x)
	}
}

// Exercise 5: benjiAgentV0
// Goal: Print a comforting message randomly, with a timestamp.

// import (
// 	"math/rand"
// 	"time"
// )

func benjiAgentV0() {
	rand.Seed(time.Now().UnixNano())
	msgs := []string{"I love you!", "Walkie?", "Food please", "Okay can we go to sleep now?"}
	now := time.Now()
	fmt.Println(now.Format("Mon Jan 2 15:04:05 MST 2006"), "Benji says:", msgs[rand.Intn(len(msgs))])
}

func exercises() {
	whoAmI("Em", "tired", "loopy")
	recallMemories([]string{"beach", "fight", "apology", "walk", "brunch", "benji", "end"})
	fmt.Println(checkDrift("baseline"))
	fmt.Println(checkDrift("triggered"))
	fmt.Println(checkDrift("hey"))
	thresholdResponse(22)
	thresholdResponse(44)
	thresholdResponse(77)
	benjiAgentV0()
}

func main() {
	examples()
	exercises()
}
