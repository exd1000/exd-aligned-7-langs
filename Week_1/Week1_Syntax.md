## TS Syntax

### TS Function Types

#### 🧩 1. Basic Function (No Args)

    function helloMemory(): void {
        console.log("👋 Welcome back to the archive.");
    }

    helloMemory();



#### 🧠 2. Function With Parameters

    function greetAgent(agentName: string): void {
        console.log(`Hello, ${agentName}. The emotional log is ready.`);
    }

    greetAgent("Em");




#### 🔁 3. Function With Return Value

    function computeDriftLevel(triggerCount: number): number {
        return triggerCount * 15;  // Each trigger increases drift
    }

    const level = computeDriftLevel(3);
    console.log("Drift Level:", level);



#### ⚠️ 4. Conditional Logic Inside Function

    function interpretSignal(value: number): string {
    if (value > 70) {
        return "🚨 Destabilize and update memory";
    } else if (value >= 40) {
        return "⚠️ Log this";
    } else {
        return "✅ Ignore";
        }
    }
    console.log(interpretSignal(88));




#### 🎛 5. Function With Default Parameter

    function driftReport(state: string = "stable"): void {
        console.log(`🌀 Current memory state: ${state}`);
    }

    driftReport();           // uses default
    driftReport("triggered");


#### 📦 6. Function Returning an Object

    function createEmotionLabel(name: string, intensity: number) {
    return {
        name: name,
        intensity: intensity,
        status: intensity > 50 ? "high" : "low"
        };
    }

    const fear = createEmotionLabel("fear", 72);
    console.log(fear);



#### 🫀 7. Closure (Function Returns a Function)

    function memoryEcho(seed: string): () => void {
    return function echo(): void {
        console.log(`🧠 Echoing trace: ${seed}`);
        };
    }

    const echoFear = memoryEcho("fear of forgetting");
    echoFear();



#### 🧪 8. Random Comfort Message Generator

    function benjiComfort(): string {
    const messages = [
        "You’re doing okay.",
        "No rush to heal.",
        "Benji believes in you."
        ];
    const i = Math.floor(Math.random() * messages.length);
    return messages[i];
    }

    console.log("🐾 Benji says:", benjiComfort());




### 🔍 Why Some Functions Use void, string, or Nothing

In TypeScript, after the function’s parameters, you can (and often should) specify the return type. That’s what goes after the `):`

General pattern:

    function functionName(params): returnType {
        // function body
    }



#### 💡 So What Do the Different Return Types Mean?

1. void – Returns nothing

Use void when the function performs an action (like printing/logging) but doesn’t return a value.

Think: “I just wanted to say it — not save it.”

    function greet(name: string): void {
        console.log(`Hey ${name}`);
    }





2. string, number, etc. – Returns a value of that type

If your function returns something, you should annotate what type it returns.

Think: “I’m handing something back to the calling world.”

    function getEmotion(): string {
        return "hopeful";
    }

    function calculateDrift(intensity: number): number {
        return intensity * 1.5;
    }





3. Nothing written at all – TypeScript will infer it

If you don’t specify a return type, TypeScript tries to guess it — but this isn’t best practice if you’re working on serious projects.

    function whisper(message: string) {
        return "..." + message;
    }

TypeScript will infer the return is string — but it’s clearer to write it explicitly:

    function whisper(message: string): string {
        return "..." + message;
    }




#### 🧪 Examples Side by Side
| Function Type               | Syntax Example                                 | Returns           |
|----------------------------|------------------------------------------------|-------------------|
| Action-only function        | `function logMood(): void`                     | Nothing           |
| Data-returning function     | `function getMood(): string`                   | String            |
| Calculator-style function   | `function driftScore(x: number): number`       | Number            |
| Inferred return (not best)  | `function vibe() { return true; }`            | Inferred → boolean|
| No return at all (can be void) | `function doNothing() {}`                 | void              |




#### 💡 Best Practice Tip
	•	Use void when your function does something (like logging, triggering animations) but doesn’t give anything back.

	•	Use explicit return types like string, number, or even custom types for clarity and safety.

	•	Avoid omitting return types unless it’s a super tiny demo or throwaway script.

