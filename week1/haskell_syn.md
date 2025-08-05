## Haskell Syntax

***In Haskell, main :: IO () is the single entry point for your program — just like main() in Go, C, or Rust.***

### 🧪 What is IO () in Haskell?

At a glance:

IO () is the type of an I/O action in Haskell that:

        •	Performs a side effect (e.g., printing, reading a file, taking user input)
        •	Returns no meaningful value (just () — pronounced “unit”, like void in other languages)



Let’s break it down:

1. IO

        •	Represents a computation that interacts with the outside world.
        •	Think: printing, reading, writing files, etc.
        •	Haskell separates pure logic (no side effects) from impure actions (side effects).
        •	IO wraps an action so the compiler knows it’s not pure.

2. ()

        •	The unit type, kind of like void in Python, Go, or Rust.
        •	It means “this action doesn’t return anything useful”.
        •	A function like putStrLn has type:
            putStrLn :: String -> IO ()

#### 🛠 Example:
    sayHi :: String -> IO ()
    sayHi name = putStrLn ("Hi, " ++ name)

This function:

	•	Takes a String
	•	Returns an IO action that, when run, prints “Hi, <name>”

You can’t “call” sayHi like in Python — you must run it within the main :: IO () block:

    main :: IO ()
    main = do
        sayHi "Emily"

### 🧠 Why does Haskell do this?

To cleanly separate:

	•	Pure logic (like math functions, type transformations, etc.)
	•	Side effects (like printing or I/O)

This makes reasoning about code safer and easier. 

Functions with type a -> b are always guaranteed to be pure. Any impurity is flagged with IO.


#### 🔄 Analogy:

In imperative languages:

	•	Everything mixes side effects and logic.

In Haskell:

	•	You write the recipe (IO () function)
	•	The main function is where the recipe is cooked



### 🔹 The Basics: String Concatenation with ++

        name = "Em"
        emotion = "loopy"
        msg = "Hi " ++ name ++ ", you're feeling " ++ emotion ++ " today."

•	++ is used to concatenate strings.

•	You must manually convert non-strings to strings using show.

        age = 27
        msg = "You are " ++ show age ++ " years old."

### 🔸 Fancy Option: Text.Printf

If you want cleaner formatting (like %s and %d), use:
        import Text.Printf

        main = do
        let name = "Benji"
            emotion = "tired"
        printf "Hi %s. You seem %s today.\n" name emotion

•	%s is for strings

•	%d for integers

•	%f for floats