## Go Syntax

### 🧠 What is switch / case in Go?

> switch is a control flow statement in Go (and many other languages) that lets you test a value against multiple possible conditions. Think of it like a cleaner alternative to multiple if / else if / else statements.

> switch is a type of conditional, just like if / else if / else, but often cleaner for checking multiple values of the same variable.

Instead of writing:

    if state == "baseline" {
        // do something
    } else if state == "triggered" {
        // do something else
    } else {
        // fallback case
    }

You can write:

    switch state {
    case "baseline":
        // do something
    case "triggered":
        // do something else
    default:
        // fallback case
    }

 EXD-themed example:

    emotion := "grief"

    switch emotion {
    case "anger":
        fmt.Println("⚡ Destabilizing fast.")
    case "grief":
        fmt.Println("💧 Slowing down… the system is vulnerable.")
    case "hope":
        fmt.Println("🌱 Reintegration possible.")
    default:
        fmt.Println("🌀 Unrecognized pattern.")
    }

### 🔄 When to use switch vs if?

| Use `if` when...                                         | Use `switch` when...                                             |
|----------------------------------------------------------|------------------------------------------------------------------|
| You have complex boolean logic (e.g., `if a > b && c != d`) | You're checking **one variable** against **multiple values**     |
| You need ranges or comparisons                           | You’re doing a **clean lookup** on discrete values (strings, ints, etc.) |



### 🔹 Basic Structure
    switch value {
    case condition1:
        // code block if value == condition1
    case condition2:
        // code block if value == condition2
    default:
        // code block if no case matches
    }

#### 🔹 1. Basic switch on string value
    func exdStateMood(state string) {
        switch state {
        case "baseline":
            fmt.Println("✅ All systems stable.")
        case "triggered":
            fmt.Println("⚠️ Destabilization detected.")
        case "drifting":
            fmt.Println("🌊 Emotional flux in motion.")
        default:
            fmt.Println("🤷 Unknown memory state.")
        }
    }

#### 🔹 2. switch on int value (threshold logic)
⚠️ See how we used switch without a value? That turns it into an if/else ladder.

    func destabilizeThreshold(val int) {
        switch {
        case val < 40:
            fmt.Println("🧊 Below sensitivity threshold: ignore.")
        case val <= 70:
            fmt.Println("📓 Logging for future review.")
        case val > 70:
            fmt.Println("🔥 Destabilize and adapt.")
        }
    }

#### 🔹 3. switch with multiple matching cases
    func reaction(memory string) {
        switch memory {
        case "beach", "walk", "brunch":
            fmt.Println("😊 Happy memory.")
        case "fight", "apology", "cry":
            fmt.Println("😔 Difficult memory.")
        default:
            fmt.Println("❓ Unclassified.")
        }
    }

#### 🔹 4. switch with fallthrough (manually allow case to continue)
⚠️ fallthrough is rarely used in Go but can be handy in some layered logic situations.

    func testFallthrough() {
        x := 2
        switch x {
        case 1:
            fmt.Println("One")
        case 2:
            fmt.Println("Two")
            fallthrough
        case 3:
            fmt.Println("Three (got here via fallthrough)")
        default:
            fmt.Println("Default")
        }
    }

#### 🔹 5. switch on type (type switch)
This is an advanced pattern but worth previewing:

    func analyze(x interface{}) {
        switch v := x.(type) {
        case int:
            fmt.Println("It's an int:", v)
        case string:
            fmt.Println("It's a string:", v)
        case bool:
            fmt.Println("It's a bool:", v)
        default:
            fmt.Println("Unknown type!")
        }
    }