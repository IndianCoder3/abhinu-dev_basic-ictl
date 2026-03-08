# Chapter 6: Making Decisions with If Statements

## What is an If Statement?

An **if statement** lets your program make decisions. It's like saying: "If something is true, do this."

### Real-World Example:

- "**If** it's raining, take an umbrella"
- "**If** your score is above 90, you got an A"
- "**If** you have enough money, buy the game"

## Basic If Statement

```ictl
Program.If(condition) {
    # Code here runs only if condition is true
}
```

### Simple Example:

```ictl
Program.Main {
    Program.If(True) {
        Terminal.Echo("This will always print!")
    }
}
```

Output:
```
This will always print!
```

The `True` is the **condition**. Since it's always true, the code inside always runs.

## Using Conditions with Comparisons

Let's make it more useful with actual comparisons:

```ictl
Program.Main {
    Variables.New(Age)
    Variables.Age = 16
    
    Program.If(Math.Compare(Variables.Age, ">=", 18)) {
        Terminal.Echo("You are an adult!")
    }
}
```

This checks: "Is Age greater than or equal to 18?"

If yes, it prints "You are an adult!"
If no, it prints nothing.

Run this with Age = 16, and nothing prints.
Change Age = 25, and you'll see the message.

## The If-Else Pattern

Often you want to do something **if** a condition is true, and something **else** if it's false:

```ictl
Program.Main {
    Variables.New(Score)
    Variables.Score = 85
    
    Program.If(Math.Compare(Variables.Score, ">=", 90)) {
        Terminal.Echo("You got an A!")
    }
    # If we add more code here, it runs regardless
}
```

We need a way to say "otherwise, do this". We'll need to use another If statement:

```ictl
Program.Main {
    Variables.New(Score)
    Variables.Score = 85
    
    Program.If(Math.Compare(Variables.Score, ">=", 90)) {
        Terminal.Echo("You got an A!")
    }
    
    Program.If(Math.Compare(Variables.Score, "<", 90)) {
        Terminal.Echo("You got less than an A")
    }
}
```

This works, but it's repetitive. A better way is to use a nested if:

```ictl
Program.Main {
    Variables.New(Score)
    Variables.Score = 85
    
    Program.If(Math.Compare(Variables.Score, ">=", 90)) {
        Terminal.Echo("You got an A!")
    }
    Program.If(Math.Compare(Variables.Score, "<", 90)) {
        Terminal.Echo("You did not get an A")
    }
}
```

## Comparison Operators

All the ways you can compare:

```ictl
Math.Compare(A, ">", B)      # Is A greater than B?
Math.Compare(A, "<", B)      # Is A less than B?
Math.Compare(A, ">=", B)     # Is A greater than or equal to B?
Math.Compare(A, "<=", B)     # Is A less than or equal to B?
Math.Compare(A, "==", B)     # Is A equal to B?
Math.Compare(A, "!=", B)     # Is A not equal to B?
```

## String Comparison

For comparing text (strings), use `Data.Compare()`:

```ictl
Program.Main {
    Variables.New(Name)
    Variables.Name = "Alice"
    
    Program.If(Data.Compare(Variables.Name, "Alice")) {
        Terminal.Echo("Welcome, Alice!")
    }
}
```

Output:
```
Welcome, Alice!
```

### How Data.Compare Works:

```ictl
Data.Compare(Value1, Value2)
```

It returns `True` if Value1 equals Value2, and `False` if they're different.

## Real-World Example: Age Checker

```ictl
Program.Main {
    Variables.New(Age)
    Variables.Age = Terminal.Ask("Enter your age: ")
    
    Program.If(Math.Compare(Variables.Age, ">=", 18)) {
        Terminal.Echo("You are an adult!")
    }
    
    Program.If(Math.Compare(Variables.Age, "<", 18)) {
        Terminal.Echo("You are a minor!")
    }
    
    Program.If(Math.Compare(Variables.Age, ">=", 65)) {
        Terminal.Echo("You qualify for senior discounts!")
    }
}
```

Sample runs:

**Run 1:**
```
Enter your age: 25
You are an adult!
```

**Run 2:**
```
Enter your age: 10
You are a minor!
```

**Run 3:**
```
Enter your age: 70
You are an adult!
You qualify for senior discounts!
```

Notice that multiple if statements can all be true!

## Nested If Statements

You can put if statements inside other if statements:

```ictl
Program.Main {
    Variables.New(Age)
    Variables.New(GPA)
    
    Variables.Age = 20
    Variables.GPA = 3.8
    
    Program.If(Math.Compare(Variables.Age, ">=", 18)) {
        Terminal.Echo("You are old enough")
        
        Program.If(Math.Compare(Variables.GPA, ">=", 3.5)) {
            Terminal.Echo("Your GPA is great!")
            Terminal.Echo("You qualify for honors!")
        }
    }
}
```

Output:
```
You are old enough
Your GPA is great!
You qualify for honors!
```

This is useful for checking multiple conditions!

## Real-World Example: Simple Grade Calculator

```ictl
Program.Main {
    Variables.New(Score)
    Variables.Score = Terminal.Ask("Enter your score (0-100): ")
    
    Program.If(Math.Compare(Variables.Score, ">=", 90)) {
        Terminal.Echo("Grade: A")
    }
    Program.If(Math.Compare(Variables.Score, ">=", 80)) {
        Program.If(Math.Compare(Variables.Score, "<", 90)) {
            Terminal.Echo("Grade: B")
        }
    }
    Program.If(Math.Compare(Variables.Score, ">=", 70)) {
        Program.If(Math.Compare(Variables.Score, "<", 80)) {
            Terminal.Echo("Grade: C")
        }
    }
    Program.If(Math.Compare(Variables.Score, ">=", 60)) {
        Program.If(Math.Compare(Variables.Score, "<", 70)) {
            Terminal.Echo("Grade: D")
        }
    }
    Program.If(Math.Compare(Variables.Score, "<", 60)) {
        Terminal.Echo("Grade: F")
    }
}
```

Sample run:
```
Enter your score (0-100): 85
Grade: B
```

## Common Mistakes

### Mistake 1: Using = instead of ==

```ictl
Program.If(Math.Compare(Score, "=", 100))   # Wrong - use "=="
Program.If(Math.Compare(Score, "==", 100))  # Correct
```

### Mistake 2: Forgetting the condition

```ictl
Program.If {                                  # Wrong - missing condition
    Terminal.Echo("Hello")
}

Program.If(True) {                            # Correct
    Terminal.Echo("Hello")
}
```

### Mistake 3: Indentation doesn't matter, but it helps!

```ictl
# These do the same thing, but the second is easier to read
Program.If(True) { Terminal.Echo("A") }

Program.If(True) {
    Terminal.Echo("A")
}
```

## Practice Exercise

Write a program that:

1. Asks the user for a temperature in Fahrenheit
2. If the temperature is below 32°F, say "It's freezing!"
3. If it's between 32°F and 60°F, say "It's cold"
4. If it's between 60°F and 80°F, say "It's nice!"
5. If it's above 80°F, say "It's hot!"

**Hint:** Use multiple if statements with Math.Compare()

## Summary

You now know:
- ✅ How to use if statements with `Program.If()`
- ✅ How to compare numbers with `Math.Compare()`
- ✅ How to compare strings with `Data.Compare()`
- ✅ Comparison operators: >, <, >=, <=, ==, !=
- ✅ How to nest if statements

---

**Next Chapter:** Let's learn about loops - repeating code!
