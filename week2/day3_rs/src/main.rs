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


fn examples() { 
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
// use std::collections::{HashMap};

fn memory_bank() {
    let mut mem = HashMap::<String, String>::new(); 
    mem.insert("brunch".to_string(), "love".to_string());
    mem.insert("park".to_string(), "fun".to_string());
    mem.insert("benji".to_string(), "cutie".to_string()); 
    mem.insert("laptop".to_string(), "happy".to_string());

    if let Some(emotion) = mem.get("brunch") {
        println!("brunch is {}", emotion);
    }

    mem.insert("brunch".to_string(), "yum".to_string());
    
    if let Some(emotion) = mem.get("brunch") {
        println!("brunch is {}", emotion);
    }
}
// scene_set
// 	•	Use a HashSet<String> to store unique scene labels.
// 	•	Add 5 scenes (include duplicates intentionally).
// 	•	Print the set to show duplicates are removed.
// 	•	Loop through the set and print each scene with a chosen emoji.
// use std::collections::{HashSet};

use rand::seq::SliceRandom;
use rand::thread_rng; 

fn scene_set() {
    let mut scenes = HashSet::<String>::new(); 
    scenes.insert("movie".to_string());
    scenes.insert("movie".to_string());
    scenes.insert("dinner".to_string());
    scenes.insert("park".to_string());
    scenes.insert("home".to_string());

    println!("{:?}", scenes);

    for scene in &scenes {
        let emojis = vec!["🙂", "🥰", "🥹", "😎", "🤩"]; 
        let mut rng = thread_rng();
        if let Some(rand_emo) = emojis.choose(&mut rng) {
            println!("{}:{}", scene, rand_emo);
        }
    }
}


// timeline_tuple
// 	•	Create a tuple of 3 emotional events ((String, String, String)).
// 	•	Print the full timeline.
// 	•	Try to mutate one element (see what happens).
// 	•	Create an immutable reference to it and attempt mutation again (observe the compiler error).


fn timeline_tuple() {
    let events: (&str, &str, &str) = ("morning", "afternoon", "evening");
    let (morning, afternoon, evening) = events; 

    println!("{}, {}, {}", morning, afternoon, evening); 

    // events.0 = "night"; // obviously doesn't work 
}
// trigger_map
// 	•	Use a HashMap<String, String> to map stimuli → emotional responses.
// 	•	Include mappings like "text", "smell", "photo".
// 	•	Add a new mapping.
// 	•	Update an existing one.
// 	•	Print the entire map.

// use std::collections::HashMap;
fn trigger_map() {
    let mut triggers = HashMap::<String, String>::new(); 
    triggers.insert("text".to_string(), "hey".to_string());
    triggers.insert("smell".to_string(), "stinky".to_string());
    triggers.insert("photo".to_string(), "cute".to_string());

    println!("{:?}",triggers);
    triggers.insert("home".to_string(), "benji".to_string(),);

    // ❌  triggers.0 = "hi :)"; // only for tuples not HashMap

    triggers.insert("text".to_string(), "hi :)".to_string());
    println!("{:?}",triggers);
}




//  em_logbook
// 	•	Use a Vec<HashMap<String, String>> to simulate a memory logbook.
// 	•	Add 3 entries, each a HashMap with keys like "time", "state", "trigger".
// 	•	Access and print a specific field from each log entry.


fn em_logbook() {
	// ✅ Instead, create HashMaps and push them:    
    let mut logbook = Vec::new(); 

    let mut entry1 = HashMap::new();
    entry1.insert("time".to_string(), "morning".to_string());

    let mut entry2 = HashMap::new();
    entry2.insert("state".to_string(), "calm".to_string());

    let mut entry3 = HashMap::new();
    entry3.insert("trigger".to_string(), "cat".to_string());

    logbook.push(entry1);
    logbook.push(entry2);
    logbook.push(entry3);

    println!("{:?}", logbook[0].get("time"));
    println!("{:?}", logbook[1].get("state"));
    println!("{:?}", logbook[2].get("trigger"));



    // ❌ pushing a string to a vector of HashMaps
    // let mut logbook = Vec::<HashMap<String, String>> = Vec::new(); 
    // logbook.push("time"); 
    // logbook.push("state");
    // logbook.push("trigger");

    // logbook.0 = "morning";
    // logbook.1 = "calm";
    // logbook.2 = "cat";

    // println!(logbook.to_string());
}

fn exercises() {
    memory_bank();
    scene_set();
    timeline_tuple();
    trigger_map();
    em_logbook();
}

fn main() {
    println!("Hello, world!");
    examples();
    exercises();

}
