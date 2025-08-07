## Handling Errors in Function Tools

When you create a function tool via `@function_tool`, you can pass a `failure_error_function`. This is a function that provides an error response to the LLM in case the tool call crashes.

### 🔧 Default Behavior
By default (i.e. if you don't pass anything), it runs a `default_tool_error_function` which tells the LLM an error occurred.

### ✨ Custom Error Function
If you pass your own error function, it runs that instead, and sends the response to the LLM.

### 🚫 No Error Handling
If you explicitly pass `None`, then any tool call errors will be **re-raised for you to handle**.  
This could be a `ModelBehaviorError` if the model produced invalid JSON, or a `UserError` if your code crashed, etc.

### 🛠 Manual FunctionTool
If you are manually creating a `FunctionTool` object, then you **must handle errors inside** the `on_invoke_tool` function.

### In simple words

Agar koi error hua, to default error message LLM ko diya jata hai.

- **Example**: "An error occurred while calling the tool."

```sh

def my_custom_error(tool_call, error):
    return "Oops! Something went wrong but I handled it gracefully."

@function_tool(failure_error_function=my_custom_error)
def my_tool(...):
    ...

```
- Aap apna error message LLM ko bhej sakte ho.

- Use-case: Agar aap user ko friendly message dena chahtay ho:
- “Oops! Something went wrong but I handled it gracefully.”

