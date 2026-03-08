# Chapter 7: Loops - Repeating Code

## What is a Loop?

A **loop** is code that repeats. Instead of writing the same line 10 times, you can tell it to repeat 10 times!

### Real-World Example:

Instead of:
```ictl
Terminal.Echo("I will not be late")
Terminal.Echo("I will not be late")
Terminal.Echo("I will not be late")
Terminal.Echo("I will not be late")
Terminal.Echo("I will not be late")
```

You can say:
```ictl
Program.Loop(5) {
    Terminal.Echo("I will not be late")
}
```

Much cleaner!

## Counted Loops

A **counted loop** runs a specific number of times.

### Basic Syntax:

```ictl
Program.Loop(count) {
    # Code here repeats 'count' times
}
```

### Example 1: Print Numbers 1 to 5

```ictl
Program.Main {
    Program.Loop(5) {
        Terminal.Echo("Hello!")
    }
}
```

Output:
```
Hello!
Hello!
Hello!
Hello!
Hello!
```

### Example 2: Print Numbers

```ictl
Program.Main {
    Variables.New(Counter)
    Variables.Counter = 1
    
    Program.Loop(5) {
        Terminal.Echo(Variables.Counter)
        Variables.Counter = Math.Eval(Variables.Counter + 1)
    }
}
```

Output:
```
1
2
3
4
5
```

Notice how we:
1. Create a counter variable
2. Use it to keep track of the iteration
3. Increase it each time through the loop

## Infinite Loops (ForeverLoop)

Sometimes you want to repeat until something happens. Use `Program.ForeverLoop`:

```ictl
Program.ForeverLoop {
    # Code here repeats forever
    # You must use Program.BreakLoop to exit
}
```

### Example: Count Until You Hit 10

```ictl
Program.Main {
    Variables.New(Counter)
    Variables.Counter = 0
    
    Program.ForeverLoop {
        Variables.Counter = Math.Eval(Variables.Counter + 1)
        Terminal.Echo(Variables.Counter)
        
        Program.If(Math.Compare(Variables.Counter, ">=", 10)) {
            Program.BreakLoop
        }
    }
}
```

Output:
```
1
2
3
4
5
6
7
8
9
10
```

### How BreakLoop Works:

`Program.BreakLoop` immediately stops the loop and continues with the code after it:

```ictl
Program.Main {
    Variables.New(Counter)
    Variables.Counter = 0
    
    Program.ForeverLoop {
        Variables.Counter = Math.Eval(Variables.Counter + 1)
        Terminal.Echo("Count: " + Variables.Counter)
        
        Program.If(Math.Compare(Variables.Counter, "==", 5)) {
            Terminal.Echo("Breaking!")
            Program.BreakLoop
        }
    }
    
    Terminal.Echo("Loop ended!")
}
```

Output:
```
Count: 1
Count: 2
Count: Count: 3
Count: 4
Count: 5
Breaking!
Loop ended!
```

## Real-World Example: Guessing Game

```ictl
Program.Main {
    Variables.New(Secret)
    Variables.New(Guess)
    Variables.New(Attempts)
    
    Variables.Secret = 42
    Variables.Attempts = 0
    
    Program.ForeverLoop {
        Variables.Guess = Terminal.Ask("Guess a number (1-100): ")
        Variables.Attempts = Math.Eval(Variables.Attempts + 1)
        
        Program.If(Math.Compare(Variables.Guess, "==", Variables.Secret)) {
            Terminal.Echo("Correct! You got it in " + Variables.Attempts + " attempts!")
            Program.BreakLoop
        }
        
        Program.If(Math.Compare(Variables.Guess, "<", Variables.Secret)) {
            Terminal.Echo("Too low, try again!")
        }
        
        Program.If(Math.Compare(Variables.Guess, ">", Variables.Secret)) {
            Terminal.Echo("Too high, try again!")
        }
    }
}
```

Sample run:
```
Guess a number (1-100): 50
Too low, try again!
Guess a number (1-100): 75
Too high, try again!
Guess a number (1-100): 60
Too low, try again!
Guess a number (1-100): 70
Too high, try again!
Guess a number (1-100): 65
Too high, try again!
Guess a number (1-100): 42
Correct! You got it in 5 attempts!
```

## Nesting Loops

You can put loops inside loops:

```ictl
Program.Main {
    Program.Loop(3) {
        Terminal.Echo("Outer loop")
        
        Program.Loop(2) {
            Terminal.Echo("  Inner loop")
        }
    }
}
```

Output:
```
Outer loop
  Inner loop
  Inner loop
Outer loop
  Inner loop
  Inner loop
Outer loop
  Inner loop
  Inner loop
```

### Example: Multiplication Table

```ictl
Program.Main {
    Variables.New(Row)
    Variables.New(Col)
    Variables.New(Product)
    
    Variables.Row = 1
    
    Program.Loop(3) {
        Variables.Col = 1
        
        Program.Loop(3) {
            Variables.Product = Math.Eval(Variables.Row * Variables.Col)
            Terminal.Echo(Variables.Row + " x " + Variables.Col + " = " + Variables.Product)
            
            Variables.Col = Math.Eval(Variables.Col + 1)
        }
        
        Variables.Row = Math.Eval(Variables.Row + 1)
    }
}
```

Output:
```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
```

## Real-World Example: Menu System

```ictl
Program.Main {
    Variables.New(Choice)
    
    Program.ForeverLoop {
        Terminal.Echo("=== Main Menu ===")
        Terminal.Echo("1. Say Hello")
        Terminal.Echo("2. Add Numbers")
        Terminal.Echo("3. Exit")
        
        Variables.Choice = Terminal.Ask("Choose (1-3): ")
        
        Program.If(Data.Compare(Variables.Choice, "1")) {
            Terminal.Echo("Hello, friend!")
        }
        
        Program.If(Data.Compare(Variables.Choice, "2")) {
            Variables.New(A)
            Variables.New(B)
            Variables.New(Sum)
            
            Variables.A = Terminal.Ask("First number: ")
            Variables.B = Terminal.Ask("Second number: ")
            Variables.Sum = Math.Eval(Variables.A + Variables.B)
            
            Terminal.Echo("Sum: " + Variables.Sum)
        }
        
        Program.If(Data.Compare(Variables.Choice, "3")) {
            Terminal.Echo("Goodbye!")
            Program.BreakLoop
        }
    }
}
```

This creates a menu that keeps running until the user chooses to exit!

## Loops vs If Statements

**If:** Runs code 0 or 1 times (depending on condition)
**Loop:** Runs code multiple times

## Common Mistakes

### Mistake 1: Infinite Loop

```ictl
Program.ForeverLoop {
    Terminal.Echo("Help!")
    # Missing Program.BreakLoop - runs forever!
}
```

### Mistake 2: Variables Not Resetting

```ictl
Program.Loop(5) {
    Variables.New(Score)  # Don't do this every iteration!
    Variables.Score = 10
}

# Better:
Variables.New(Score)
Program.Loop(5) {
    Variables.Score = Math.Eval(Variables.Score + 1)
}
```

## Practice Exercise

Write a program that:

1. Asks the user for a number
2. Prints the multiplication table for that number (up to 10)
3. Example: If user enters 5, print "5 x 1 = 5", "5 x 2 = 10", etc.

**Hint:**
```ictl
Program.Main {
    Variables.New(Number)
    Variables.New(Multiplier)
    Variables.New(Result)
    
    Variables.Number = Terminal.Ask("Enter a number: ")
    Variables.Multiplier = 1
    
    Program.Loop(10) {
        # Your code here...
    }
}
```

## Summary

You now know:
- ✅ How to use `Program.Loop()` for counted loops
- ✅ How to use `Program.ForeverLoop` for infinite loops
- ✅ How to use `Program.BreakLoop` to exit loops
- ✅ How to nest loops inside each other
- ✅ How to create counter variables

---

**Next Chapter:** Let's work with strings and text operations!
