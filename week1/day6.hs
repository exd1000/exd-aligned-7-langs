-- 🦋 Day 6: Haskell — the ethereal plane of programming languages.

import System.Random
import Data.Time

-- 1. Variables / Values
-- All variables are constants (immutable).
year :: Int
year = 2025

theme :: String
theme = "destabilization"

-- 2. Conditionals
temperature :: Float -> String
temperature t =
  if t > 100 then "Too hot to hold."
  else if t < 97 then "A little cold-hearted?"
  else "You're just right."

--   3. Recursion instead of Loops
countdown :: Int -> IO ()
countdown 0 = putStrLn "Blast off!"
countdown n = do
  print n
  countdown (n - 1)

--   4. Functions
sayHi :: String -> IO ()
sayHi name = putStrLn ("Hi, " ++ name)

double :: Int -> Int
double x = x * 2

swap :: (a, b) -> (b, a)
swap (x, y) = (y, x)

-- 5. Scope (let, where)
describe :: Int -> String
describe x =
  let doubled = x * 2
  in "Twice is " ++ show doubled

describe2 x = "Twice is " ++ show doubled
  where doubled = x * 2

-- 6. Random + Time
benjiSays :: IO ()
benjiSays = do
  let msgs = ["You're safe.", "Let it go.", "I'm still with you."]
  i <- randomRIO (0, length msgs - 1)
  now <- getCurrentTime
  putStrLn $ "[" ++ show now ++ "] Benji says: " ++ msgs !! i


-- Exercise 1: identityGlimmer
-- Goal: Create a whoAmI function that:
-- Prints your name, current emotion, and memory state.


-- ⚠️ no commas between parameters
whoAmI :: String -> String -> String -> IO ()
whoAmI name currEmo memState = 
    putStrLn ("Hi " ++ name ++ " seems like you're feeling" ++ currEmo ++ "and" ++ memState ++".") 


-- Exercise 2: MemoryLoop
-- Goal: Write a recallMemories function that loop through memories.Respond differently based on the memory.
-- memories = ["beach", "fight", "apology", "walk", "brunch", "benji", "ex"]

recallMemories :: [String] -> IO ()
recallMemories [] = return ()
recallMemories (mem:rest) = do 
    putStrLn $ "recalling: " ++ mem
    if mem `elem` ["beach", "walk", "brunch"]
        then putStrLn "Cool"
    else if mem `elem` ["fight", "apology", "ex"]
        then putStrLn "Yikes"
    else 
        putStrLn "🥺"
    recallMemories rest 

-- 🧠 Explanation:
-- 	recallMemories (mem:rest) pattern-matches the list into head and tail.
-- 	elem checks if mem is in a given list.
-- 	Recursion continues the loop until the list is empty ([]).

-- ❌ What’s going wrong:
-- 	memories :: String -> IO() declares memories takes a String  but you actually want it to take a list or operate on one.
--  putStrLN is a typo (Haskell is case-sensitive) → should be putStrLn.
-- 	Haskell doesn’t use = like Python or JS for comparison it uses ==.
-- 	Pattern matching like mem = ["beach", ...] won’t work you need to test membership with elem.

    -- memories :: String -> IO()
    -- memories 0 = putStrLN ["beach", "fight", "apology", "walk", "brunch", "benji", "ex"]
    -- memories n = do 
    --     print n 
    --     memories (n - 1)
    --         mem :: String 
    --         if mem = ["beach", "brunch" "walk"] then "cool"
    --         else if mem = ["fight", "apology", "ex"] then "ew"
    --         else "🥺"




-- Exercise 3: destabilizeCheck
-- Goal: Write a checkDrift function that returns “Stable”, “Destabilizing…”, or “Drifting” based on input.
-- - “Stable” if the state is "baseline"
-- - “Destabilizing…” if the state is "triggered"
-- - “Drifting” for anything else

-- Pure Function (not pritnting just returns String)
checkDrift :: String -> String
checkDrift state = 
    if state == "baseline" then "stable"
    else if state == "triggered" then "destablized"
    else "drifting" 


-- IO Version (function prints result directly)

-- checkDrift :: String -> IO () --String >
-- checkDrift state =
--     if state == "baseline" then putStrLn "Stable"
--     else if state == "triggered" then putStrLn "Destabilizing…"
--     else putStrLn "Drifting"
-- main = do
--     checkDrift "baseline"
--     checkDrift "triggered"
--     checkDrift "yo"



-- Exercise 4: thresholdResponse
-- Goal: Create a thresholdResponse function and return response based on signal strength.
--     returns “Ignore” if < 40
--     returns “Log this” if 40–70
--     returns “Destabilize & update” if > 70

thresholdResponse :: Int -> String 
thresholdResponse signal = 
    if signal < 40 then show signal ++ ": ignore"
    else if signal <= 70 then show signal ++ ": log this"
    else show signal ++ ": destabilize & update"

-- Exercise 5: benjiAgentV0
-- Goal: Print a comforting message randomly, with a timestamp.
-- choices = ["woof!", "hi", "are you done yet", "can we go now"]

benjiAgentV0 :: IO ()
benjiAgentV0 = do 
    let msgs = ["Can we go for a walk now", "Are you done yet", "I'm going to take a nap", "Are you still going on about that"]
    i <- randomRIO (0, length msgs - 1)
    now <- getCurrentTime
    putStrLn $ "[" ++ show now ++ "]. Benji: " ++ msgs !! i


-- ⚠️ !! is the list index operator in Haskell.







-- ⚠️ Define all pure functions at the top (like whoAmI, checkDrift, etc.), and then
--  main block is where all your IO happens (printing, reading input, etc.).


main :: IO ()
main = do 
    -- ex1
    whoAmI "em" "confused" "scattered"

    -- ex2 
    let myMems = ["beach", "fight", "apology", "walk", "brunch","benji", "ex"]
    recallMemories myMems

    -- ex3
    putStrLn (checkDrift "baseline")
    putStrLn (checkDrift "triggered")
    putStrLn (checkDrift "yo")

    -- ex4
    putStrLn (thresholdResponse 22)
    putStrLn (thresholdResponse 44)
    putStrLn (thresholdResponse 77)

    -- ex5
    benjiAgentV0