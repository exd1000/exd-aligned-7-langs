// Data Structures in TypeScript

// 1. Lists / Arrays
// 📝 Basic array of strings
const memories: string[] = ["beach", "fight", "brunch"];

// ✅ Accessing items
console.log(memories[0]);  // "beach"

// ✨ Adding a new memory
memories.push("goodbye");

// 🔁 Looping
for (let mem of memories) {
  console.log("Recalling:", mem);
}

// 2. Dictionaries / Maps (aka Record<string, string>)
// 🧠 Mapping memory → emotion
const memoryMap: Record<string, string> = {
  "brunch": "yum",
  "benji": "cutie",
  "fight": "tense"
};

// ✅ Access
console.log(memoryMap["brunch"]);  // "yum"

// ✨ Add/update
memoryMap["walk"] = "calm";
memoryMap["fight"] = "ugh";

// 3. Sets
// 🎬 Filter out duplicates
const scenes = new Set<string>();

scenes.add("beach");
scenes.add("beach");  // Won’t duplicate
scenes.add("brunch");

console.log(scenes);  // Set { 'beach', 'brunch' }

// 🔁 Looping over Set
for (let scene of scenes) {
  console.log("Scene:", scene);
}

// 4. Tuples / Immutable Collections
// 🕰️ Ordered, fixed-length values
const timeline: [string, string, string] = ["beach", "fight", "goodbye"];

// ✅ Access by index
console.log(timeline[1]);  // "fight"

// ❌ TypeScript enforces tuple types & order
// timeline[0] = 5;  // Error: type mismatch

// You *can* technically mutate tuples (they're just arrays under the hood),
// but types will restrict you. Consider using `readonly`:
const lockedTimeline: readonly [string, string, string] = ["start", "middle", "end"];
// lockedTimeline[0] = "oops" // ❌ Error: Readonly


// Exercises

// memory_bank
// Use a dictionary (Record<string, string>) to store memory-emotion pairs.
// 	•	Add at least 4 unique memory → emotion mappings.
// 	•	Print the emotional tone associated with "brunch".
// 	•	Update the value of an existing memory.
const memoryBank: Record<string, string> = {
  "beach": "nice",
  "benji": "cute", 
  "picnic":"fun",
  "brunch": "yum"
};

console.log(memoryBank["brunch"]);

memoryBank["mornings"] = "peaceful";
memoryBank["kdramas"] = "silly";



// scene_set
// Use a Set<string> to store unique scene labels.
// 	•	Add 5 scenes, with at least one intentional duplicate.
// 	•	Show that duplicates are removed.
// 	•	Loop through the set and print each scene with an emoji reaction.
const sceneSet = new Set(["beach","night","movie","home","home"]);
const emojis = ["🤪","👾", "🌸", '❤️'];

console.log(sceneSet);

for (let s of sceneSet) {
  const randomEmoji = emojis[Math.floor(Math.random() * emojis.length)];
    console.log(`${s}: ${randomEmoji}`);
}


// timeline_tuple
// Use a tuple to represent 3 key emotional events in order.
// 	•	Define a tuple of [string, string, string] with distinct moments.
// 	•	Try to mutate one of the tuple elements.
// 	•	Mark it as readonly and observe what happens when you try to change it.
const timelineTuple: [string, string, string] = ["movie", "park", "walk"];
timelineTuple[0] = "brunch";
console.log(timelineTuple);

const timelineLocked: readonly [string, string,string] = ["eli", "em", "benj"]
console.log(timelineLocked);
// timelineLocked[0] = "not here yet";

// trigger_map
// Create a Record<string, string> to map external stimuli → emotional responses.
// 	•	Include mappings like "text", "smell", "photo", etc.
// 	•	Add a new mapping dynamically.
// 	•	Update the response of an existing one.
// 	•	Log the final mapping.
const triggerMap: Record <string, string> = {
  "text": "🤨", 
  "smell": "🤢", 
  "photo": "🖼️"
}

console.log(triggerMap);
triggerMap["taste"] = "🥗";
triggerMap["photo"] = "🌌";

console.log(triggerMap);



// em_logbook
// Use an array of dictionaries to simulate a memory logbook.
// 	•	Each entry should be a dict with keys like "time", "state", "trigger", etc.
// 	•	Add at least 3 entries to the logbook.
// 	•	Access and print a specific field from each log entry (e.g., time or state).

// explicitly typed but TS can also infer the type
const emLogbook: {[key: string]: string}[] = 
    [{
        "memory": "beach", 
        "company": "benji"
    }, 
    {
        "time": "morning", 
        "weather": "cool", 
        "environment": "peaceful"
    }, 
    {
        "state": "ease", 
        "feeling": "happy "
    }]; 

console.log(emLogbook[0]["company"]);
console.log(emLogbook[1]["time"]);
console.log(emLogbook[2]["feeling"]);
