# Chapter 4: Variables and Data Types

## What is a Variable?

A **variable** is like a labeled box that holds information. Instead of remembering numbers or words yourself, your program remembers them.

Think of it like this:

```
┌─────────────────┐
│   Name          │  (Label)
│                 │
│  "Alice"        │  (Content)
└─────────────────┘
```

## Creating Variables

To create a variable, use:

```ictl
Variables.New(BoxName)
```

This creates an empty box. The name inside the parentheses is what we call the variable.

### Rules for Variable Names:

- Use letters, numbers, and underscores: `My_Variable`, `Score1`, `PlayerName`
- Cannot start with a number: ✗ `1Score`, ✓ `Score1`
- Cannot have spaces: ✗ `My Score`, ✓ `MyScore`
- Cannot use special characters: ✗ `Score@`, ✓ `Score`
- Upper/lowercase matters: `Score` and `score` are different variables

## Storing Values in Variables

Once you create a variable, you can put information in it:

```ictl
Variables.Name = "Alice"
Variables.Age = 25
```

The `=` means "store this value in the variable".

### Complete Example:

```ictl
Program.Main {
    Variables.New(PlayerName)
    Variables.PlayerName = "Bob"
    
    Terminal.Echo("The player's name is: " + Variables.PlayerName)
}
```

Output:
```
The player's name is: Bob
```

## Data Types

Not all information is the same. ICTL works with different **types** of data:

### 1. Strings (Text)

**Strings** are words or sentences. They always go in quotation marks:

```ictl
Variables.New(Greeting)
Variables.Greeting = "Hello, friend!"
```

Examples of strings:
- `"Hello"`
- `"Alice"`
- `"123"` (this is text, not a number!)
- `"I love programming"`
- `""` (empty string - no text)

### 2. Numbers (Integers)

**Integers** are whole numbers (no decimals):

```ictl
Variables.New(Age)
Variables.Age = 25

Variables.New(Score)
Variables.Score = 100
```

Examples of integers:
- `42`
- `0`
- `-5` (negative numbers)
- `1000`

### 3. Numbers (Floats/Decimals)

**Floats** are numbers with decimals:

```ictl
Variables.New(Price)
Variables.Price = 19.99

Variables.New(Temperature)
Variables.Temperature = -3.5
```

Examples of floats:
- `3.14`
- `0.5`
- `-2.75`
- `99.99`

### 4. Booleans (True/False)

**Booleans** represent yes/no or true/false:

```ictl
Variables.New(IsRaining)
Variables.IsRaining = True

Variables.New(IsLunchTime)
Variables.IsLunchTime = False
```

Boolean values are: `True` or `False` (capitalized!)

## Mixing Data Types

Here's where it gets fun. You can combine different types:

```ictl
Program.Main {
    Variables.New(Name)
    Variables.New(Age)
    Variables.New(Salary)
    
    Variables.Name = "Charlie"
    Variables.Age = 30
    Variables.Salary = 50000.50
    
    Terminal.Echo("Name: " + Variables.Name)
    Terminal.Echo("Age: " + Variables.Age)
    Terminal.Echo("Salary: " + Variables.Salary)
}
```

Output:
```
Name: Charlie
Age: 30
Salary: 50000.50
```

When you use `+` to combine values with text, ICTL automatically converts them to text!

## Updating Variables

You can change what's stored in a variable at any time:

```ictl
Program.Main {
    Variables.New(Score)
    Variables.Score = 0
    
    Terminal.Echo("Starting score: " + Variables.Score)
    
    Variables.Score = 10
    Terminal.Echo("After first round: " + Variables.Score)
    
    Variables.Score = 25
    Terminal.Echo("After second round: " + Variables.Score)
}
```

Output:
```
Starting score: 0
After first round: 10
After second round: 25
```

The variable remembers the new value each time!

## Real-World Example: A Simple Calculator

```ictl
Program.Main {
    Variables.New(FirstNumber)
    Variables.New(SecondNumber)
    Variables.New(Sum)
    
    # Get numbers from user
    Variables.FirstNumber = Terminal.Ask("Enter first number: ")
    Variables.SecondNumber = Terminal.Ask("Enter second number: ")
    
    # Calculate sum
    Variables.Sum = Math.Eval(Variables.FirstNumber + Variables.SecondNumber)
    
    # Display result
    Terminal.Echo("Sum: " + Variables.Sum)
}
```

Sample run:
```
Enter first number: 5
Enter second number: 3
Sum: 8
```

## Common Mistakes

### Mistake 1: Forgetting Quotation Marks

```ictl
Terminal.Echo("Hi") + " Alice"    # Correct - text in quotes
Terminal.Echo(Hi Alice)            # Wrong - missing quotes
```

### Mistake 2: Using Variable Before Creating It

```ictl
Variables.X = 5              # Wrong - X doesn't exist yet
Variables.New(X)
Variables.X = 5              # Correct
```

### Mistake 3: Mixing Up = and Comparison

```ictl
Variables.X = 5              # This stores 5 in X
Variables.X == 5             # This checks if X equals 5
```

## Practice Exercise

Write a program that:

1. Creates three variables: `FirstName`, `LastName`, `Favorite_Food`
2. Asks the user for their first and last name
3. Asks what their favorite food is
4. Displays all three pieces of information in a nice sentence

**Hint:**
```ictl
Program.Main {
    Variables.New(FirstName)
    # Continue from here...
}
```

## Summary

You now understand:
- ✅ How to create variables with `Variables.New()`
- ✅ How to store values with `=`
- ✅ Strings (text in quotes)
- ✅ Integers (whole numbers)
- ✅ Floats (numbers with decimals)
- ✅ Booleans (true/false)
- ✅ How to combine data with `+`
- ✅ How to update variables

---

**Next Chapter:** Let's work with math and calculations!
