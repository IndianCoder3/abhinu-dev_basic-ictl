# Chapter 11: Best Practices and Troubleshooting

## Common Errors and How to Fix Them

### Error 1: "Variable not found"

**Problem:**
```ictl
Program.Main {
    Variables.X = 5         # Error - X doesn't exist yet!
}
```

**Solution:**
```ictl
Program.Main {
    Variables.New(X)        # Create it first
    Variables.X = 5         # Then use it
}
```

**Remember:** Always use `Variables.New()` before assigning a value!

---

### Error 2: "Undefined command"

**Problem:**
```ictl
Program.Main {
    Terminal.Print("Hello")  # Wrong command name
}
```

**Solution:**
```ictl
Program.Main {
    Terminal.Echo("Hello")   # Correct command
}
```

**Check:** Make sure you're using the exact command names from the documentation.

---

### Error 3: Syntax errors (missing braces)

**Problem:**
```ictl
Program.Main
    Terminal.Echo("Hello")   # Missing { }
```

**Solution:**
```ictl
Program.Main {
    Terminal.Echo("Hello")
}
```

**Remember:** Every block needs `{` at the start and `}` at the end.

---

### Error 4: String quotes issues

**Problem:**
```ictl
Terminal.Echo('Hello')      # Wrong - single quotes
Terminal.Echo(Hello)        # Wrong - no quotes
Terminal.Echo("Hello)       # Wrong - mismatched quotes
```

**Solution:**
```ictl
Terminal.Echo("Hello")      # Correct - double quotes
```

**Remember:** Strings always use double quotes: `"text"`

---

### Error 5: Infinite loop crash

**Problem:**
```ictl
Program.ForeverLoop {
    Terminal.Echo("Oops!")
    # Missing Program.BreakLoop - runs forever!
}
```

**Solution:**
```ictl
Program.ForeverLoop {
    Terminal.Echo("Oops!")
    Program.BreakLoop  # Now it stops
}
```

**Remember:** Always have a way to exit infinite loops!

---

## Writing Better Code

### Rule 1: Clear Variable Names

**Bad:**
```ictl
Variables.New(X)
Variables.New(Y)
Variables.New(Z)
```

**Good:**
```ictl
Variables.New(PlayerName)
Variables.New(PlayerScore)
Variables.New(PlayerAge)
```

Clear names make code easier to understand!

---

### Rule 2: Use Comments

**Bad:**
```ictl
Program.Main {
    Variables.New(A)
    Variables.A = Terminal.Ask("Enter value: ")
    Variables.New(B)
    Variables.B = Math.Eval(Variables.A * 2)
}
```

**Good:**
```ictl
Program.Main {
    # Get the user's input
    Variables.New(UserInput)
    Variables.UserInput = Terminal.Ask("Enter a number: ")
    
    # Calculate double the input
    Variables.New(DoubleValue)
    Variables.DoubleValue = Math.Eval(Variables.UserInput * 2)
}
```

Comments help future you understand current you!

---

### Rule 3: Organize Your Code

**Bad:**
```ictl
Program.Main {
    Terminal.Echo("Hello")
    Variables.New(X)
    Terminal.Echo("Enter number")
    Variables.X = Terminal.Ask("Number: ")
    Variables.New(Y)
    Variables.Y = Math.Eval(Variables.X * 2)
    Terminal.Echo(Variables.Y)
}
```

**Good:**
```ictl
Program.Main {
    # 1. Declare all variables
    Variables.New(Input)
    Variables.New(Result)
    
    # 2. Display welcome message
    Terminal.Echo("Welcome to My Program")
    
    # 3. Get user input
    Variables.Input = Terminal.Ask("Enter a number: ")
    
    # 4. Process the input
    Variables.Result = Math.Eval(Variables.Input * 2)
    
    # 5. Display results
    Terminal.Echo("Double: " + Variables.Result)
}
```

Organized code is easier to read and debug!

---

### Rule 4: Test Edge Cases

When writing conditionals, test all paths:

```ictl
Program.Main {
    Variables.New(Age)
    Variables.Age = Terminal.Ask("Age: ")
    
    # Test: Age = 0
    # Test: Age = 18 (exact boundary)
    # Test: Age = 100
    
    Program.If(Math.Compare(Variables.Age, ">=", 18)) {
        Terminal.Echo("Adult")
    }
    Program.If(Math.Compare(Variables.Age, "<", 18)) {
        Terminal.Echo("Minor")
    }
}
```

Test your code with:
- Minimum values
- Maximum values
- Boundary values (like exactly 18)
- Invalid input if possible

---

## Debugging Tips

### Tip 1: Add Debug Output

Add `Terminal.Echo()` statements to see what's happening:

```ictl
Program.Main {
    Variables.New(X)
    Variables.X = Terminal.Ask("Enter number: ")
    
    # Debug: show what we got
    Terminal.Echo("DEBUG: X = " + Variables.X)
    
    Variables.New(Y)
    Variables.Y = Math.Eval(Variables.X * 2)
    
    # Debug: show the calculation
    Terminal.Echo("DEBUG: Y = " + Variables.Y)
    
    Terminal.Echo("Final result: " + Variables.Y)
}
```

---

### Tip 2: Simplify the Problem

If your 50-line program isn't working, test just the problematic part:

```ictl
# Instead of running the whole program, test just this:
Program.Main {
    Variables.New(Test)
    Test = Terminal.Ask("Test input: ")
    Terminal.Echo("You entered: " + Test)
}
```

Once this works, add more pieces.

---

### Tip 3: Check Variable Types

Remember that `"5"` (text) is different from `5` (number):

```ictl
Program.Main {
    Variables.New(A)
    Variables.New(B)
    
    Variables.A = "5"                    # Text
    Variables.B = Math.Eval(5)          # Number
    
    # This might not work as expected
    Terminal.Echo(Variables.A + Variables.B)  # "5" + 5
}
```

---

## Performance Tips

### Tip 1: Declare Variables Once

**Bad:**
```ictl
Program.Loop(10) {
    Variables.New(Score)  # Creating it 10 times!
    Variables.Score = Math.Eval(Variables.Score + 1)
}
```

**Good:**
```ictl
Variables.New(Score)
Variables.Score = 0

Program.Loop(10) {
    Variables.Score = Math.Eval(Variables.Score + 1)
}
```

---

### Tip 2: Avoid Unnecessary Loops

**Bad:**
```ictl
Program.Loop(5) {
    Terminal.Echo("Hello!")
    Program.Loop(5) {
        Terminal.Echo("Hi!")
    }
}
# Total output: 25 "Hi!" messages
```

**Good:**
```ictl
Program.Loop(25) {
    Terminal.Echo("Hi!")
}
```

---

## Best Practices Summary

### DO:
✅ Use clear, descriptive variable names
✅ Write comments explaining what your code does
✅ Organize code logically
✅ Test your code with different inputs
✅ Use indentation to make code readable
✅ Reset terminal styles after using them
✅ Create variables before using them

### DON'T:
❌ Use unclear variable names like `X`, `Y`, `temp`
❌ Write code without comments if it's complex
❌ Mix different tasks in one code block
❌ Assume your code works - test it!
❌ Forget closing braces `}`
❌ Use variables before creating them
❌ Leave infinite loops without breaks

---

## Real-World Example: Well-Written Program

Here's a program that follows all best practices:

```ictl
Program.Main {
    # ===== VARIABLES =====
    Variables.New(PlayerName)
    Variables.New(PlayerScore)
    Variables.New(NumberOfQuestions)
    Variables.New(CurrentQuestion)
    Variables.New(UserAnswer)
    Variables.New(CorrectAnswer)
    
    # ===== WELCOME =====
    Terminal.Style("bold")
    Terminal.Echo("=== QUIZ GAME ===")
    Terminal.Style("reset")
    Terminal.Echo("Test your knowledge!")
    Terminal.Echo("")
    
    # ===== GET PLAYER INFO =====
    Variables.PlayerName = Terminal.Ask("What is your name? ")
    Variables.PlayerScore = 0
    Variables.NumberOfQuestions = 3
    Variables.CurrentQuestion = 1
    
    # ===== QUIZ LOOP =====
    Program.Loop(3) {
        Terminal.Echo("Question " + Variables.CurrentQuestion + ":")
        
        # Question 1
        Program.If(Math.Compare(Variables.CurrentQuestion, "==", 1)) {
            Variables.CorrectAnswer = "Paris"
            Variables.UserAnswer = Terminal.Ask("What is the capital of France? ")
        }
        
        # Question 2
        Program.If(Math.Compare(Variables.CurrentQuestion, "==", 2)) {
            Variables.CorrectAnswer = "4"
            Variables.UserAnswer = Terminal.Ask("What is 2 + 2? ")
        }
        
        # Question 3
        Program.If(Math.Compare(Variables.CurrentQuestion, "==", 3)) {
            Variables.CorrectAnswer = "Shakespeare"
            Variables.UserAnswer = Terminal.Ask("Who wrote Romeo and Juliet? ")
        }
        
        # ===== CHECK ANSWER =====
        Program.If(Data.Compare(Variables.UserAnswer, Variables.CorrectAnswer)) {
            Terminal.Style("green")
            Terminal.Echo("Correct!")
            Terminal.Style("reset")
            Variables.PlayerScore = Math.Eval(Variables.PlayerScore + 1)
        }
        Program.If(Data.Compare(Variables.UserAnswer, Variables.CorrectAnswer)) {
        }
        Program.If(Math.Compare(Variables.PlayerScore, "==", Math.Eval(Variables.PlayerScore + 1))) {
        }
        
        Terminal.Echo("")
        Variables.CurrentQuestion = Math.Eval(Variables.CurrentQuestion + 1)
    }
    
    # ===== RESULTS =====
    Terminal.Style("bold")
    Terminal.Echo("=== RESULTS ===")
    Terminal.Style("reset")
    Terminal.Echo("Player: " + Variables.PlayerName)
    Terminal.Echo("Score: " + Variables.PlayerScore + "/" + Variables.NumberOfQuestions)
}
```

Notice:
- Clear section headers
- Descriptive variable names
- Comments explaining each section
- Proper spacing and indentation
- Error handling concepts

---

## Practice Exercise

Take one of your earlier programs and improve it:

1. Add better variable names
2. Add helpful comments
3. Test it with edge cases
4. Format it nicely with spacing

---

## Summary

You now know:
- ✅ Common ICTL errors and how to fix them
- ✅ How to write clear, readable code
- ✅ How to debug problems
- ✅ Best practices for organizing code
- ✅ How to optimize performance
- ✅ The DON'Ts to avoid

---

**Final Chapter:** Additional resources and what you can do next!
