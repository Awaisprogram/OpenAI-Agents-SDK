# 📘 Markdown Examples and Syntax Guide

---

## 🟦 Headings

### Heading 1  
`# Heading` ← ✅  
`#Heading` ← ❌ (Won’t render properly — missing space)  

### Heading Level 5 (HTML Equivalent):  
```html
<h1>Heading 1</h1>
```

---

## 🟦 Paragraphs

### HTML:
```html
<p>This is the first line. And this is the second line.</p>
```

### Markdown:
This is the first line. And this is the second line.

👉 *If you want to start your paragraph with an empty space, don’t use space or tab. Instead, use `&nbsp;`*

---

## 🟦 Line Breaks

### HTML:
```html
<p>
  This is the first line.<br />
  And this is the second line.
</p>
```

### Markdown (add two spaces at the end of the line):
This is the first line.  
And this is the second line.

---

## 🟦 Bold Text

```markdown
**bold text**
```

**Rendered Output:**  
**bold text**

---

## 🟦 Italic Text

```markdown
_italic_
```

**Rendered Output:**  
_italic_

---

## 🟦 Bold + Italic

```markdown
***bold and italic***
```

**Rendered Output:**  
***bold and italic***

---

## 🟦 Blockquote

```markdown
> This is a blockquote.
```

> This is a blockquote.

---

## 🟦 Lists

### Unordered List:

```markdown
- Item 1
- Item 2
  - Sub-item 2.1
  - Sub-item 2.2
```

- Item 1
- Item 2  
  - Sub-item 2.1  
  - Sub-item 2.2

### Ordered List:

```markdown
1. First
2. Second
3. Third
```

1. First  
2. Second  
3. Third

---

## 🟦 Code

### Inline Code:

```markdown
Use the `print()` function.
```

Use the `print()` function.

### Code Block:

<pre>
```python
def greet():
    print("Hello, world!")
```
</pre>

```python
def greet():
    print("Hello, world!")
```

---

## 🟦 Links

```markdown
[OpenAI](https://www.openai.com/)
```

[OpenAI](https://www.openai.com/)

---

## 🟦 Images

```markdown
![Alt Text](https://example.com/image.png)
```

---

## 🟦 Horizontal Line

```markdown
---
```

---

## 🟦 Tables

```markdown
| Syntax | Description |
|--------|-------------|
| Header | Title       |
| Paragraph | Text     |
```

| Syntax    | Description |
|-----------|-------------|
| Header    | Title       |
| Paragraph | Text        |

---

## 🟦 Escape Characters

Use a backslash `\` to escape Markdown symbols:

```markdown
\*Not italicized\*
```

\*Not italicized\*

---

## 🟦 Emojis

Use emoji shortcodes like `:smile:`

Example: 😄 `:smile:`, 🚀 `:rocket:`, 📘 `:blue_book:`

Full list of GitHub emojis: https://github.com/ikatyang/emoji-cheat-sheet

---

## 🟦 Task Lists

```markdown
- [x] Completed task
- [ ] Incomplete task
```

- [x] Completed task  
- [ ] Incomplete task

---

## 🟦 HTML Tags in Markdown

You can use raw HTML for more control:

```html
<p style="color:red">This is red text</p>
```

<p style="color:red">This is red text</p>
