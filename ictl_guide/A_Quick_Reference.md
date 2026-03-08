# Quick Reference Guide - ICTL Commands and Syntax

## Program Structure

Every ICTL program needs:
```ictl
Program.Main {
    # Your code here
}
```

---

## Variables

### Create a Variable
```ictl
Variables.New(VariableName)
```

### Assign a Value
```ictl
Variables.VariableName = Value
```

### Read a Variable
```ictl
Variables.VariableName
```

### Examples
```ictl
Variables.New(Name)
Variables.Name = "Alice"
Terminal.Echo(Variables.Name)
```

---

## Terminal Input/Output

### Display Text
```ictl
Terminal.Echo("Your text here")
```

### Get User Input
```ictl
Terminal.Ask("Your question: ")
Variables.Name = Terminal.Ask("What is your name? ")
```

### Change Text Color
```ictl
Terminal.Style("red")       # Red text
Terminal.Style("green")     # Green text
Terminal.Style("blue")      # Blue text
Terminal.Style("yellow")    # Yellow text
Terminal.Style("cyan")      # Cyan text
Terminal.Style("magenta")   # Magenta text
Terminal.Style("bold")      # Bold text
Terminal.Style("reset")     # Back to normal
```

---

## Math Operations

### Basic Arithmetic
```ictl
Math.Eval(10 + 5)      # Addition
Math.Eval(10 - 5)      # Subtraction
Math.Eval(10 * 5)      # Multiplication
Math.Eval(10 / 5)      # Division
Math.Eval((2 + 3) * 4) # With parentheses
```

### Store Math Results
```ictl
Variables.Result = Math.Eval(10 + 5)
Terminal.Echo(Variables.Result)  # Shows: 15
```

---

## Comparisons

### Compare Two Numbers
```ictl
Math.Compare(10, ">", 5)       # Greater than
Math.Compare(3, "<", 5)        # Less than
Math.Compare(5, ">=", 5)       # Greater than or equal
Math.Compare(5, "<=", 5)       # Less than or equal
Math.Compare(5, "==", 5)       # Equal to
Math.Compare(5, "!=", 3)       # Not equal to
```

### Compare Two Strings
```ictl
Data.Compare("hello", "hello")     # Equal?
Data.Compare("hello", "world")     # Not equal
```

---

## Conditional Statements

### If Statement
```ictl
Program.If(condition) {
    # Code here runs if condition is true
}
```

### With Comparison
```ictl
Program.If(Math.Compare(Age, ">=", 18)) {
    Terminal.Echo("You are an adult")
}
```

### Nested If
```ictl
Program.If(Math.Compare(Age, ">=", 18)) {
    Program.If(Math.Compare(Score, ">", 90)) {
        Terminal.Echo("Adult with high score!")
    }
}
```

---

## Loops

### Count Loop (Repeat N times)
```ictl
Program.Loop(5) {
    Terminal.Echo("Hello!")  # Prints 5 times
}
```

### Infinite Loop
```ictl
Program.ForeverLoop {
    Terminal.Echo("Running forever...")
    Program.BreakLoop  # Exit the loop
}
```

### Exit a Loop
```ictl
Program.BreakLoop
```

---

## String Operations

### Combine Strings
```ictl
"Hello" + " " + "World"
Variables.FirstName + " " + Variables.LastName
```

### Mix Strings and Numbers
```ictl
"Your age is: " + Variables.Age
"Result: " + Math.Eval(10 + 5)
```

---

## Data Types

### String (Text)
```ictl
"Hello"
"Alice"
"123"  # This is text, not a number!
```

### Number (Integer)
```ictl
42
0
-5
1000
```

### Number (Decimal/Float)
```ictl
3.14
99.99
-2.5
```

### Boolean (True/False)
```ictl
True   # Capital T
False  # Capital F
```

---

## Comments

```ictl
# This is a comment - ICTL ignores this line
Terminal.Echo("Code here")  # Comment at end of line
```

---

## Complete Program Template

```ictl
Program.Main {
    # ===== SETUP =====
    Variables.New(Name)
    Variables.New(Score)
    Variables.New(Result)
    
    # ===== GET INPUT =====
    Variables.Name = Terminal.Ask("Enter name: ")
    Variables.Score = Terminal.Ask("Enter score: ")
    
    # ===== PROCESS =====
    Variables.Result = Math.Eval(Variables.Score * 2)
    
    # ===== DISPLAY OUTPUT =====
    Terminal.Echo("Hello, " + Variables.Name)
    Terminal.Echo("Your score times 2: " + Variables.Result)
}
```

---

## Common Patterns

### Menu System
```ictl
Program.ForeverLoop {
    Terminal.Echo("1. Option A")
    Terminal.Echo("2. Option B")
    Variables.Choice = Terminal.Ask("Choose: ")
    
    Program.If(Data.Compare(Variables.Choice, "1")) {
        # Do something
    }
    
    Program.If(Data.Compare(Variables.Choice, "2")) {
        # Do something else
    }
}
```

### Counter Loop with Condition
```ictl
Variables.New(Counter)
Variables.Counter = 0

Program.ForeverLoop {
    Variables.Counter = Math.Eval(Variables.Counter + 1)
    Terminal.Echo(Variables.Counter)
    
    Program.If(Math.Compare(Variables.Counter, ">=", 10)) {
        Program.BreakLoop
    }
}
```

### Input Validation
```ictl
Program.If(Math.Compare(Age, ">", 0)) {
    Program.If(Math.Compare(Age, "<", 150)) {
        Terminal.Echo("Valid age")
    }
}
```

---

## Syntax Rules

| Rule | Example |
|------|---------|
| Commands need parentheses | ✓ `Terminal.Echo("text")` |
| Strings in double quotes | ✓ `"hello"` |
| Variables created before use | ✓ `Variables.New(X)` then `Variables.X = 5` |
| Code blocks need braces | ✓ `Program.If(...) { }` |
| Commands end with ) or } | ✓ `Terminal.Echo()` |

---

## Keyboard Shortcuts

| Action | Key |
|--------|-----|
| Run program | Depends on editor (usually F5 or Ctrl+Shift+B) |
| Save file | Ctrl+S |
| New line | Enter |
| Comment whole line | Ctrl+/ (in VS Code) |

---

## Troubleshooting Quick Fixes

| Problem | Solution |
|---------|----------|
| "Variable not found" | Use `Variables.New()` first |
| "Undefined command" | Check spelling of command name |
| Syntax error | Check for missing `{` `}` or quotes |
| Infinite loop | Add `Program.BreakLoop` |
| Text looks wrong | Check quotation marks are double quotes |

---

## When to Use What

| Need | Use |
|------|-----|
| Display text | `Terminal.Echo()` |
| Get user input | `Terminal.Ask()` |
| Do math | `Math.Eval()` |
| Compare numbers | `Math.Compare()` |
| Compare text | `Data.Compare()` |
| Make decisions | `Program.If()` |
| Repeat code N times | `Program.Loop()` |
| Repeat until condition | `Program.ForeverLoop` |
| Change text color | `Terminal.Style()` |
| Store a value | `Variables.New()` and `=` |

---

## Example Programs by Use Case

### "Hello World"
```ictl
Program.Main {
    Terminal.Echo("Hello, World!")
}
```

### Get User Info
```ictl
Program.Main {
    Variables.New(Name)
    Variables.Name = Terminal.Ask("Name: ")
    Terminal.Echo("Hello, " + Variables.Name)
}
```

### Simple Math
```ictl
Program.Main {
    Terminal.Echo(Math.Eval(5 + 3))
}
```

### Conditional
```ictl
Program.Main {
    Program.If(Math.Compare(5, ">", 3)) {
        Terminal.Echo("5 is greater than 3")
    }
}
```

### Simple Loop
```ictl
Program.Main {
    Program.Loop(5) {
        Terminal.Echo("Hello!")
    }
}
```

---

## Tips for Success

✅ **DO:**
- Use clear variable names
- Add comments to explain code
- Test your programs
- Use proper indentation
- Create variables before using them

❌ **DON'T:**
- Use confusing variable names
- Write code without comments
- Assume code works without testing
- Forget braces `{}`
- Forget quotation marks for strings

---

**Print this page and keep it handy while you code!**
