// Rust Data Structures


// Lists / Arrays (Vectors in Rust) → Vec<T>, [T; N]
fn lists() {
    let mut groceries = vec!["eggs", "milk", "bread"];
    groceries.push("butter");
    
    for item in &groceries {
        println!("Need to buy: {}", item);
    }

}
// Dictionaries / Maps (HashMap) → HashMap<K, V>
use std::collections::HashMap;

fn dicts() {
    let mut fruit_colors = HashMap::new();
    fruit_colors.insert("apple", "red");
    fruit_colors.insert("banana", "yellow");
    fruit_colors.insert("grape", "purple");

    if let Some(color) = fruit_colors.get("banana") {
        println!("Banana is {}", color);
    }
}


// Sets (HashSet) → HashSet<T>
use std::collections::HashSet;

fn sets() {
    let mut seen_animals = HashSet::new();
    seen_animals.insert("fox");
    seen_animals.insert("deer");
    seen_animals.insert("fox"); // duplicate!

    for animal in &seen_animals {
        println!("Saw a {}", animal);
    }
}


// Tuples / Immutable Collections → (T1, T2, ...) + &str, &[T]
fn tups() {
    let person: (&str, i32, bool) = ("Emily", 27, true);
    let (name, age, is_active) = person;

    println!("Name: {}, Age: {}, Active: {}", name, age, is_active);

    // Try modifying tuple element (won’t work unless reassigning entire tuple)
    // person.0 = "Not Emily"; // Error: cannot assign
}


fn exs() { 
    lists();
    dicts();
    sets();
    tups();
}




// 💖 EXD-Aligned Exercises 
// You’ll need use std::collections::{HashMap, HashSet}; for most of these.

// memory_bank
// 	•	Use a HashMap<String, String> to store memory → emotion pairs.
// 	•	Add at least 4 entries.
// 	•	Access and print the emotion for "brunch".
// 	•	Update an existing memory’s emotion.

// scene_set
// 	•	Use a HashSet<String> to store unique scene labels.
// 	•	Add 5 scenes (include duplicates intentionally).
// 	•	Print the set to show duplicates are removed.
// 	•	Loop through the set and print each scene with a chosen emoji.

// timeline_tuple
// 	•	Create a tuple of 3 emotional events ((String, String, String)).
// 	•	Print the full timeline.
// 	•	Try to mutate one element (see what happens).
// 	•	Create an immutable reference to it and attempt mutation again (observe the compiler error).

// trigger_map
// 	•	Use a HashMap<String, String> to map stimuli → emotional responses.
// 	•	Include mappings like "text", "smell", "photo".
// 	•	Add a new mapping.
// 	•	Update an existing one.
// 	•	Print the entire map.


//  em_logbook
// 	•	Use a Vec<HashMap<String, String>> to simulate a memory logbook.
// 	•	Add 3 entries, each a HashMap with keys like "time", "state", "trigger".
// 	•	Access and print a specific field from each log entry.

fn main() {
    println!("Hello, world!");
    exs()
}
