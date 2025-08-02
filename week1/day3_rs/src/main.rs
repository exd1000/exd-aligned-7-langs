// 🦀 Week 1 Day 3: Rust – Syntax & Core Logic

// Rust is strict but rewarding — think of it like the emotionally secure partner who always checks if you’re okay (and won’t let you use null).

// Variables - Immutable by default 🔒
//     let, mut
// Conditionals - Just like Python, but with {}
//     if, else if, else
// Loops - Iteration across memory space
//     for, while, loop
// Functions - With explicit parameter & return types
//     fn
// Scope - No globals without static
//     Block-level via {}

// create new cargo project > `cargo new PROJECT_FOLDER_NAME`
// init rust project > `cargo init --bin`
// Cargo.toml > add dependencies (to use ANY dependencies MUST use cargo)
// build & run > `cargo run'



fn main() {

    // 1. Variables & Types
    let name = "Em";                  // immutable
    let mut mood = "curious";         // mutable
    let drift_level: i32 = 42;        // typed
    let confidence: f64 = 0.87;
    let is_stable: bool = true;

    // 2. Conditionals

    if drift_level > 70 {
        println!("🔺 Destabilization imminent.");
    } else if drift_level > 40 {
        println!("⚠️ Moderate drift.");
    } else {
        println!("✅ Stable.");
    }

    // 3. Loops
    let memories = vec!["sunset", "laughing", "his text", "our song", "the goodbye"];

    for memory in &memories {
        println!("🔁 Recalling: {}", memory);
    }

    let mut i = 0;
    while i < 3 {
        println!("💭 Thinking...");
        i += 1;
    }

    // 4. Functions
    fn greet(name: &str) {
        println!("Hey {}, you’re safe. 💖", name);
    }

    fn drift_status(score: i32) -> &'static str {
        if score > 70 {
            "Destabilizing"
        } else {
            "Stable"
        }
    }

    // 5. Scope
    let mood = "neutral";

    {
        let mood = "hopeful";
        println!("Inside scope: {}", mood);
    }

    println!("Outside scope: {}", mood);



    // Exercise 1: identity_glimmer
    // Create a function called who_am_i() that prints out:
    // 	•	your current emotion
    // 	•	your name
    // 	•	your memory state (just a fake label like “stable”, “fragmented”, “drifting”)
    // Practice: variables, string output, function definition
    // EXD twist: make your program greet you like a little memory mirror
    
    
    fn who_am_i(curr_emo: &str, name: &str, mem_state: &str) {
        println!("Hi {}, nice to meet you!", name);
        println!("Starting user analysis..");
        std::thread::sleep(std::time::Duration::from_secs(3)); // non-async version
        println!("User {} is currently {}. Memory state is {}.", name, curr_emo, mem_state);
    }


    who_am_i("happy","em","stable");

    // ❌ async fn not allowed in Rust 2015
        // use tokio::time::{sleep,Duration};
        // #[tokio::main]
        // async


    // Exercise 2: ex_memory_loop
    // Create a loop that simulates 5 memory recalls from a list like:
    // memories = ["beach", "fight", "apology", "walk", "brunch", "benji", "end"]
    // Each recall should print something like:
    // "🔁 Recalling: beach"
    // Practice: loops, arrays/lists, printing
    // EXD twist: make your bot react differently to "end"
    let memories = vec!["beach", "fight", "apology", "walk", "brunch", "benji", "end"];

    for mem in &memories {
        println!("Recalling: {}", mem);
        if ["beach","walk","brunch"].contains(mem) {
            println!("Sounds nice");
        } else if ["fight","apology","end"].contains(mem) {
            println!("Oh there my silly brain goes again");
        } else {
            println!("My entire heart 🥺");
        }
    }

    // ❌ Rust syntax uses .contains() not if.. in


    // Exercise 3: destabilize_check
    // Write a function check_drift(state) that prints:
    // 	•	“Stable” if the state is "baseline"
    // 	•	“Destabilizing…” if the state is "triggered"
    // 	•	“Drifting” for anything else
    // Practice: conditionals, branching logic
    // EXD twist: simulate a memory destabilization trigger

    fn check_drift(state: &str) {
        if state == "baseline" {
            println!("Stable");
        } else if state == "triggered" {
            println!("Destabilized");
        } else {
            println!("Drifting..");
        }
    }

    check_drift("baseline");
    check_drift("triggered");
    check_drift("NaN");

    // Exercise 4: threshold_response
    // Take a “signal” (numeric value between 0–100).
    // Write a function that:
    // 	•	returns “Ignore” if < 40
    // 	•	returns “Log this” if 40–70
    // 	•	returns “Destabilize & update” if > 70
    // Practice: numeric variables, comparison logic, return values
    // EXD twist: this simulates an internal memory threshold being breached


    fn signal(num: i32) {
        if num < 40 {
            println!("{}: ignore", num);
        } else if num <= 70 { 
            println!("{}: log this", num);
        } else {
            println!("{}: destabilize & update", num);
        }
    }

    signal(22);
    signal(44);
    signal(77);


    // Exercise 5: benji_agent_v0
    // Make a tiny agent function benji_says() that:
    // 	•	picks a random message from a list like:
    // ["You’re safe.", "It’s okay to let go.", "I’m still with you."]
    // 	•	and prints it with a timestamp
    // Practice: functions, randomization, time handling (basic)
    // EXD twist: build a comfort bot. This is EXD-support in code form 🐶


// Moved `msgs`, `rng` inside function
// Had to add `rand` crate to Cargo.toml → had to init a cargo project 🥹
// Also added `chrono` crate bc the timestamp was ugly lmao 

    use rand::seq::SliceRandom;
    use rand::thread_rng; 
    use chrono::Local;

    fn benji_says() {
        let msgs = vec!["You’re safe.", "It’s okay to let go.", "I’m still with you."];
        let mut rng = thread_rng(); 
        let now = Local::now().format("%Y-%m-%d %H:%M:%S").to_string();

        if let Some(rand_msg) = msgs.choose(&mut rng) {
            println!("[{:?}]. Benji says: {}", now, rand_msg);
        }
    }

    benji_says();

}