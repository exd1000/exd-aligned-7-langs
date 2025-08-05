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