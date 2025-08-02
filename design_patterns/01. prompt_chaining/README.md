### 🧩 Prompt Chaining

**Prompt Chaining** breaks down a complex task into a sequence of simpler steps. In this approach, the output of each LLM (Large Language Model) call is passed as the input to the next one in the chain. This enables the model to handle smaller, more manageable tasks at each step.

You can also integrate **programmatic checks** (often called “gates”) between steps to validate intermediate outputs and ensure the workflow remains on track.


![Banner](https://short-link.me/19PnA)


---

#### 📌 When to Use This Pattern:

Use prompt chaining when the task can be **cleanly decomposed** into a series of fixed subtasks.  
This pattern trades off **latency** (due to multiple model calls) in exchange for **higher accuracy and control**, by simplifying what the model is expected to do in each step.
