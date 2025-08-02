// 🌀 TypeScript – Core Concepts Overview 

// TypeScript uses explicit typing:
// 	string, number, boolean, void, any, string[], etc.

	// Variables – typed labels for emotional states
	// Conditionals – branching internal logic
	// Loops – iterate through memory traces
	// Functions – reusable emotional routines
	// Scope – inner vs outer memory influence


// 1. Variables & Types
// TypeScript is statically typed — you must (or should) declare your types.
// Tip: use const if the value won’t change, let if it might.
let myName: string = "Em";
let emotion: string = "curious";
let driftLevel: number = 42;
let confidence: number = 0.87;
let isStable: boolean = true;


// 2. Conditionals
// Decision branches for internal state.
// if / else if / else just like Python, but wrapped in curly braces {}.

// ❌ Problem: You’re referencing state outside of a function without defining it.
// ✅ Fix: Wrap it in a function or define state as a variable before using it.
  // if (state === "baseline") {
  //   console.log("Stable");
  // } else if (state === "triggered") {
  //   console.log("Destabilizing...");
  // } else {
  //   console.log("Drifting");
  // }


// 3. Loops
// For replaying memory traces or internal iterations.
// for...of for iterables, while for condition loops.
const memories: string[] = ["sunset", "laughing", "his text", "our song", "the goodbye"];

for (let memory of memories) {
  console.log("🔁 Recalling:", memory);
}

for (let i = 0; i < 5; i++) {
  console.log("Looping memory...");
}


// 4. Functions
// Modular behavior, emotion processors, and helpers.
// Declare input/output types (name: string, score: number, : void, : string).

  // function functionName(params): returnType {
  //   // function body
  // }

function greet(name: string): void {
  console.log("Hello, " + name);
}

greet("Em");

function driftStatus(score: number): string {
  if (score > 70) {
    return "Destabilizing";
  } else {
    return "Stable";
  }
}

console.log(driftStatus(42));


// 5. Scope (Local vs Global)
// What state is remembered inside vs outside functions?
// Use let/const for block scope. Re-declaring inside functions won’t change outer values unless passed or returned.
let memory_state = "fragmented"; // global

function simulate_scope(): void {
  let memory_state = "stable"; // local
  console.log("Inside function:", memory_state); // stable
}

simulate_scope();
console.log("Outside function:", memory_state); // fragmented

// 6. Random + Time 
const messages = ["You're safe", "Let go", "Still with you"];
const msg = messages[Math.floor(Math.random() * messages.length)];

const now = new Date();
console.log(`[${now.toLocaleTimeString()}] ${msg}`);





// 🧪 Exercise 1: identity_glimmer
// Create a function called who_am_i() that prints out:
// 	•	your current emotion
// 	•	your name
// 	•	your memory state (just a fake label like “stable”, “fragmented”, “drifting”)
// Practice: variables, string output, function definition
// EXD twist: make your program greet you like a little memory mirror

const comfts = ['Want a hug?', 'Wanna get a matcha latte?', 'How about we watch an episode of a silly show?'];
const randomComft = comfts[Math.floor(Math.random() * comfts.length)];

function who_am_i(name: string, emot: string, memState: string): void {
  console.log(`hey ${name}, i see you're currently ${emot} and ${memState}`);
  console.log(randomComft);
}

who_am_i('em','stresed','distributed');

// 🔁 Exercise 2: ex_memory_loop
// Create a loop that simulates 5 memory recalls from a list like:
// memories = ["beach", "fight", "apology", "walk", "brunch", "benji", "end"]
// Each recall should print something like:
// "🔁 Recalling: beach"
// Practice: loops, arrays/lists, printing
// EXD twist: make your bot react differently to "end"

const mems = ["beach", "fight", "apology", "walk", "brunch", "benji", "end"]

// ✅ Fix: Use .includes() instead:
for (let mem of mems) {
  if (['beach','walk','brunch'].includes(mem)) {
    console.log(`recalling: ${mem}`)
    console.log('ahh sounds nice rn');
  } else if (['fight','apology','end'].includes(mem)) {
    console.log(`recalling: ${mem}`)
    console.log('yikes sounds like the past is haunting me again');
  } else {
    console.log(`recalling: ${mem}`)
    console.log('oh it\'s benji boy');
  }
}


// ❌ This won’t do what you expect:
  // for (let mem of mems) {
  //   console.log('recalling:', mem);
  //   if (mem in ['beach', 'walk', 'brunch']) {
  //     console.log('ahh sounds nice rn');
  //   } else if (mem in ['fight','apology','end']) {
  //     console.log('ah yikes the past is haunting me again');
  //   } else {
  //     console.log('oh benji my sweet baby');
  //   }
  // }

  // 📝 sigh i'm thinking python lmao 




// 🔍 Exercise 3: destabilize_check
// Write a function check_drift(state) that prints:
// 	•	“Stable” if the state is "baseline"
// 	•	“Destabilizing…” if the state is "triggered"
// 	•	“Drifting” for anything else
// Practice: conditionals, branching logic
// EXD twist: simulate a memory destabilization trigger

let state: string = 'triggered';

function checkDrift(state: string) {
  if (state == 'baseline') {
    return 'stable';
  } else if (state == 'triggered') {
    return 'destable';
  } else {
    return 'drifting';
  }
}

console.log(checkDrift('triggered'));


// 🧠 Exercise 4: threshold_response
// Take a “signal” (numeric value between 0–100).
// Write a function that:
// 	•	returns “Ignore” if < 40
// 	•	returns “Log this” if 40–70
// 	•	returns “Destabilize & update” if > 70
// Practice: numeric variables, comparison logic, return values
// EXD twist: this simulates an internal memory threshold being breached



function signal(num: number) {
  if (num < 40) {
    return `${num}, ignore`;
  } else if (num <= 70) {
    return `${num}, log this`;
  } else {
    return `${num}, destabilize & update`;
  }
}

console.log(signal(22));
console.log(signal(44));
console.log(signal(77));

// 🫂 Exercise 5: benji_agent_v0
// Make a tiny agent function benji_says() that:
// 	•	picks a random message from a list like:
// ["You’re safe.", "It’s okay to let go.", "I’m still with you."]
// 	•	and prints it with a timestamp
// Practice: functions, randomization, time handling (basic)
// EXD twist: build a comfort bot. This is EXD-support in code form 🐶

const benjiMsgs = ["You’re safe.", "It’s okay to let go.", "I’m still with you."];
const randomBenjiMsg = benjiMsgs[Math.floor(Math.random() * benjiMsgs.length)];

function benjiSays(): void {
  const timestamp = new Date().toLocaleTimeString();
  console.log(`[${timestamp}]: Benji says: ${randomBenjiMsg}`);
}

benjiSays();