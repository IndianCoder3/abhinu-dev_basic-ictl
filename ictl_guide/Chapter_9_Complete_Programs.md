# Chapter 9: Complete Programs - Putting It All Together

Now that you've learned the basics, let's build some complete programs that use everything you know!

## Program 1: Personal Info Summary

```ictl
Program.Main {
    # Create variables for user information
    Variables.New(FirstName)
    Variables.New(LastName)
    Variables.New(Age)
    Variables.New(City)
    Variables.New(Job)
    
    # Get information from user
    Terminal.Echo("=== Tell Me About Yourself ===")
    Variables.FirstName = Terminal.Ask("First name: ")
    Variables.LastName = Terminal.Ask("Last name: ")
    Variables.Age = Terminal.Ask("Age: ")
    Variables.City = Terminal.Ask("City: ")
    Variables.Job = Terminal.Ask("Job: ")
    
    # Display summary
    Terminal.Echo("")
    Terminal.Echo("=== YOUR INFORMATION ===")
    Terminal.Echo("Name: " + Variables.FirstName + " " + Variables.LastName)
    Terminal.Echo("Age: " + Variables.Age)
    Terminal.Echo("Location: " + Variables.City)
    Terminal.Echo("Job: " + Variables.Job)
}
```

**What it teaches:** Variables, input, concatenation, output

---

## Program 2: Simple Calculator

```ictl
Program.Main {
    Variables.New(Number1)
    Variables.New(Number2)
    Variables.New(Operation)
    Variables.New(Result)
    
    Terminal.Echo("=== Simple Calculator ===")
    Variables.Number1 = Terminal.Ask("Enter first number: ")
    Variables.Number2 = Terminal.Ask("Enter second number: ")
    Variables.Operation = Terminal.Ask("Operation (+, -, *, /): ")
    
    # Calculate based on operation
    Program.If(Data.Compare(Variables.Operation, "+")) {
        Variables.Result = Math.Eval(Variables.Number1 + Variables.Number2)
        Terminal.Echo(Variables.Number1 + " + " + Variables.Number2 + " = " + Variables.Result)
    }
    
    Program.If(Data.Compare(Variables.Operation, "-")) {
        Variables.Result = Math.Eval(Variables.Number1 - Variables.Number2)
        Terminal.Echo(Variables.Number1 + " - " + Variables.Number2 + " = " + Variables.Result)
    }
    
    Program.If(Data.Compare(Variables.Operation, "*")) {
        Variables.Result = Math.Eval(Variables.Number1 * Variables.Number2)
        Terminal.Echo(Variables.Number1 + " * " + Variables.Number2 + " = " + Variables.Result)
    }
    
    Program.If(Data.Compare(Variables.Operation, "/")) {
        Variables.Result = Math.Eval(Variables.Number1 / Variables.Number2)
        Terminal.Echo(Variables.Number1 + " / " + Variables.Number2 + " = " + Variables.Result)
    }
}
```

**What it teaches:** Variables, input, Math.Eval(), if statements, string comparison

**Sample run:**
```
=== Simple Calculator ===
Enter first number: 15
Enter second number: 3
Operation (+, -, *, /): /
15 / 3 = 5
```

---

## Program 3: Grade Calculator

```ictl
Program.Main {
    Variables.New(Score)
    Variables.New(Grade)
    
    Terminal.Echo("=== Grade Calculator ===")
    Variables.Score = Terminal.Ask("Enter test score (0-100): ")
    
    # Assign grades
    Program.If(Math.Compare(Variables.Score, ">=", 90)) {
        Variables.Grade = "A"
    }
    Program.If(Math.Compare(Variables.Score, ">=", 80)) {
        Program.If(Math.Compare(Variables.Score, "<", 90)) {
            Variables.Grade = "B"
        }
    }
    Program.If(Math.Compare(Variables.Score, ">=", 70)) {
        Program.If(Math.Compare(Variables.Score, "<", 80)) {
            Variables.Grade = "C"
        }
    }
    Program.If(Math.Compare(Variables.Score, ">=", 60)) {
        Program.If(Math.Compare(Variables.Score, "<", 70)) {
            Variables.Grade = "D"
        }
    }
    Program.If(Math.Compare(Variables.Score, "<", 60)) {
        Variables.Grade = "F"
    }
    
    Terminal.Echo("")
    Terminal.Echo("Score: " + Variables.Score)
    Terminal.Echo("Grade: " + Variables.Grade)
    
    # Provide feedback
    Program.If(Data.Compare(Variables.Grade, "A")) {
        Terminal.Echo("Excellent work!")
    }
    Program.If(Data.Compare(Variables.Grade, "F")) {
        Terminal.Echo("You need to study more!")
    }
}
```

**What it teaches:** Nested if statements, multiple conditions

---

## Program 4: Number Guessing Game

```ictl
Program.Main {
    Variables.New(Secret)
    Variables.New(Guess)
    Variables.New(Attempts)
    Variables.New(TooHigh)
    Variables.New(TooLow)
    
    Terminal.Echo("=== Number Guessing Game ===")
    Terminal.Echo("I'm thinking of a number between 1 and 100")
    Terminal.Echo("")
    
    Variables.Secret = 42
    Variables.Attempts = 0
    
    Program.ForeverLoop {
        Variables.Guess = Terminal.Ask("Make a guess: ")
        Variables.Attempts = Math.Eval(Variables.Attempts + 1)
        
        # Check if correct
        Program.If(Math.Compare(Variables.Guess, "==", Variables.Secret)) {
            Terminal.Echo("You got it!")
            Terminal.Echo("It took " + Variables.Attempts + " attempts!")
            Program.BreakLoop
        }
        
        # Check if too low
        Program.If(Math.Compare(Variables.Guess, "<", Variables.Secret)) {
            Terminal.Echo("Too low!")
        }
        
        # Check if too high
        Program.If(Math.Compare(Variables.Guess, ">", Variables.Secret)) {
            Terminal.Echo("Too high!")
        }
    }
}
```

**What it teaches:** ForeverLoop, BreakLoop, if statements

---

## Program 5: Temperature Converter

```ictl
Program.Main {
    Variables.New(Celsius)
    Variables.New(Fahrenheit)
    Variables.New(Choice)
    
    Terminal.Echo("=== Temperature Converter ===")
    Terminal.Echo("1. Celsius to Fahrenheit")
    Terminal.Echo("2. Fahrenheit to Celsius")
    
    Variables.Choice = Terminal.Ask("Choose (1 or 2): ")
    
    Program.If(Data.Compare(Variables.Choice, "1")) {
        Variables.Celsius = Terminal.Ask("Enter temperature in Celsius: ")
        # Formula: F = (C * 9/5) + 32
        Variables.Fahrenheit = Math.Eval((Variables.Celsius * 9 / 5) + 32)
        Terminal.Echo(Variables.Celsius + "°C = " + Variables.Fahrenheit + "°F")
    }
    
    Program.If(Data.Compare(Variables.Choice, "2")) {
        Variables.Fahrenheit = Terminal.Ask("Enter temperature in Fahrenheit: ")
        # Formula: C = (F - 32) * 5/9
        Variables.Celsius = Math.Eval((Variables.Fahrenheit - 32) * 5 / 9)
        Terminal.Echo(Variables.Fahrenheit + "°F = " + Variables.Celsius + "°C")
    }
}
```

**What it teaches:** Math with parentheses, formulas

---

## Program 6: Countdown Timer

```ictl
Program.Main {
    Variables.New(Seconds)
    Variables.New(CurrentSecond)
    
    Terminal.Echo("=== Countdown Timer ===")
    Variables.Seconds = Terminal.Ask("Enter seconds to countdown: ")
    Variables.CurrentSecond = Variables.Seconds
    
    Program.ForeverLoop {
        Terminal.Echo(Variables.CurrentSecond + "...")
        
        Program.If(Math.Compare(Variables.CurrentSecond, "<=", 0)) {
            Terminal.Echo("Time's up!")
            Program.BreakLoop
        }
        
        Variables.CurrentSecond = Math.Eval(Variables.CurrentSecond - 1)
    }
}
```

**What it teaches:** Loops with conditions

---

## Program 7: Multiplication Quiz

```ictl
Program.Main {
    Variables.New(Number1)
    Variables.New(Number2)
    Variables.New(CorrectAnswer)
    Variables.New(UserAnswer)
    Variables.New(Score)
    Variables.New(QuestionNum)
    
    Terminal.Echo("=== Multiplication Quiz ===")
    Terminal.Echo("Answer 5 questions!")
    Terminal.Echo("")
    
    Variables.Score = 0
    Variables.QuestionNum = 1
    
    Program.Loop(5) {
        Variables.Number1 = Math.Eval(Variables.QuestionNum + 2)
        Variables.Number2 = Math.Eval(Variables.QuestionNum * 2)
        Variables.CorrectAnswer = Math.Eval(Variables.Number1 * Variables.Number2)
        
        Terminal.Echo("Question " + Variables.QuestionNum + ":")
        Variables.UserAnswer = Terminal.Ask(Variables.Number1 + " * " + Variables.Number2 + " = ")
        
        Program.If(Math.Compare(Variables.UserAnswer, "==", Variables.CorrectAnswer)) {
            Terminal.Echo("Correct!")
            Variables.Score = Math.Eval(Variables.Score + 1)
        }
        
        Program.If(Math.Compare(Variables.UserAnswer, "!=", Variables.CorrectAnswer)) {
            Terminal.Echo("Wrong! The answer was " + Variables.CorrectAnswer)
        }
        
        Terminal.Echo("")
        Variables.QuestionNum = Math.Eval(Variables.QuestionNum + 1)
    }
    
    Terminal.Echo("=== RESULTS ===")
    Terminal.Echo("You got " + Variables.Score + " out of 5!")
}
```

**What it teaches:** Loops, all concepts combined

---

## Program 8: Menu-Driven Program

```ictl
Program.Main {
    Variables.New(Choice)
    Variables.New(Num1)
    Variables.New(Num2)
    Variables.New(Result)
    
    Program.ForeverLoop {
        Terminal.Echo("")
        Terminal.Echo("=== MENU ===")
        Terminal.Echo("1. Add numbers")
        Terminal.Echo("2. Say hello")
        Terminal.Echo("3. Exit")
        
        Variables.Choice = Terminal.Ask("Choose (1-3): ")
        
        Program.If(Data.Compare(Variables.Choice, "1")) {
            Variables.Num1 = Terminal.Ask("First number: ")
            Variables.Num2 = Terminal.Ask("Second number: ")
            Variables.Result = Math.Eval(Variables.Num1 + Variables.Num2)
            Terminal.Echo("Sum: " + Variables.Result)
        }
        
        Program.If(Data.Compare(Variables.Choice, "2")) {
            Variables.New(Name)
            Variables.Name = Terminal.Ask("What is your name? ")
            Terminal.Echo("Hello, " + Variables.Name + "!")
        }
        
        Program.If(Data.Compare(Variables.Choice, "3")) {
            Terminal.Echo("Goodbye!")
            Program.BreakLoop
        }
    }
}
```

**What it teaches:** Menu systems, interactive loops

---

## Tips for Writing Complete Programs

1. **Plan First:** Sketch out what your program should do

2. **Declare Variables Early:** Create all variables at the start of your program

3. **Comment Your Code:** Explain what each section does

4. **Test Everything:** Try different inputs and edge cases

5. **Name Variables Clearly:** Use `UserAge` instead of `UA`

6. **One Task Per Variable:** Don't reuse variables for different things

7. **Format for Readability:** Use spacing and indentation

---

## Practice Exercise

Create a program that:

1. Asks for 3 test scores
2. Calculates the average
3. Determines if the average is A, B, C, D, or F
4. Displays the results in a nice format

---

**Next Chapter:** Let's learn some common patterns and best practices!
