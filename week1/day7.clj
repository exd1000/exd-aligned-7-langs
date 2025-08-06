;; 🦋 Day 7 Clojure – Syntax & Core Logic

;; 1. Variables / Values
(def year 2025)
(def theme "destabilization")

;; 2. Conditionals
(defn temperature [t]
  (cond
    (> t 100) "Too hot to hold."
    (< t 97)  "A little cold-hearted?"
    :else     "You're just right."))

;; 3. Recursion instead of Loops
(defn countdown [n]
  (if (zero? n)
    (println "Blast off!")
    (do
      (println n)
      (recur (dec n))))) ; recur = tail-recursive call

;; 4. Functions
(defn say-hi [name]
  (println (str "Hi, " name)))

(defn double [x]
  (* 2 x))

(defn swap [[x y]]
  [y x])

;; 5. Scope (let blocks)
(defn describe [x]
  (let [doubled (* 2 x)]
    (str "Twice is " doubled)))

(defn describe2 [x]
  (str "Twice is " (* 2 x))) ; inline version

;; 6. Random + Time
(ns benji.core
  (:import [java.time LocalDateTime])
  (:gen-class))

(def msgs ["You're safe." "Let it go." "I'm still with you."])

(defn benji-says []
  (let [i (rand-int (count msgs))
        now (str (LocalDateTime/now))]
    (println (str "[" now "] Benji says: " (nth msgs i)))))


;; Exercise 1: identity_glimmer
;; Create a function called who_am_i() that prints out:
;; •	your current emotion
;; •	your name
;; •	your memory state (just a fake label like “stable”, “fragmented”, “drifting”)

(defn who-am-i [[name current-emo mem-state]]
  (println (str "Hi, " name ". I see you're feeling " current-emo " and " mem-state ".")))

(who-am-i ["Em", "stresed", "spaced out"])

;; Exercise 2: ex_memory_loop
;; Create a loop that simulates 5 memory recalls from a list like:
;; memories = ["beach", "fight", "apology", "walk", "brunch", "benji", "goodbye"]
;; Each recall should print something like:
;; "🔁 Recalling: beach"
(def memories ["beach", "fight", "apology", "walk", "brunch", "benji", "goodbye"])


(defn recall-mem [mem]
  (cond 
   (some #{"beach" "walk" "brunch"} [mem]) (str mem ": Nice.")
   (some #{"fight" "apology" "goodbye"} [mem]) (str mem ": Ew.")
   :else (str mem ": 🥺")))

(doseq [m (take 5 memories)]
  (println "recalling: " m (recall-mem m)))

;; Exercise 3: destabilize_check
;; Write a function check_drift(state) that prints:
;; •	“Stable” if the state is "baseline"
;; •	“Destabilizing…” if the state is "triggered"
;; •	“Drifting” for anything else

(defn check-drift [state]
  (cond
    (= state "baseline") "stable"
    (= state "triggered") "destabilized"
    :else "drifted"))


(println(check-drift "baseline"))
(println(check-drift "triggered"))
(println(check-drift "hi"))

;; Exercise 4: threshold_response
;; Take a “signal” (numeric value between 0–100).
;; Write a function that:
;; •	returns “Ignore” if < 40
;; •	returns “Log this” if 40–70
;; •	returns “Destabilize & update” if > 70
(defn threshold-response [signal]
  (cond
    (< signal 40) (str signal ": ignore")
    (<= signal 70) (str signal ": log this")
    :else (str signal ": destabilize & update")))


(println(threshold-response 22))
(println(threshold-response 44))
(println(threshold-response 77))

;; Exercise 5: benji_agent_v0
;; Make a tiny agent function benji_says() that:
;; picks a random message from a list like:
;; ["You’re safe.", "It’s okay to let go.", "I’m still with you."]
;; and prints it with a timestamp

(def msgs ["You’re safe.", "It’s okay to let go.", "I’m still with you."])

(defn benji-agent-v0 []
  (let [i (rand-int (count msgs))
    now (str (LocalDateTime/now))]
    (println (str "[" now "]. Benji says: " (nth msgs i)))))


(benji-agent-v0)