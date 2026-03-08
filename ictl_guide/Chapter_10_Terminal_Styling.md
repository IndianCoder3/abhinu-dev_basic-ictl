# Chapter 10: Making Your Programs Look Good - Terminal Styling

## What is Terminal Styling?

Terminal styling lets you change the color and appearance of your text output. This makes your programs look more professional and helps guide users.

## Basic Terminal Styles

Use `Terminal.Style()` to change colors:

```ictl
Terminal.Style("color_name")
```

### Available Colors:

```ictl
Terminal.Style("red")        # Red text
Terminal.Style("green")      # Green text
Terminal.Style("blue")       # Blue text
Terminal.Style("yellow")     # Yellow text
Terminal.Style("cyan")       # Cyan/Light blue text
Terminal.Style("magenta")    # Purple/Magenta text
Terminal.Style("bold")       # Bold/Bright text
Terminal.Style("reset")      # Back to normal
```

## Simple Example

```ictl
Program.Main {
    Terminal.Style("green")
    Terminal.Echo("Success!")
    
    Terminal.Style("red")
    Terminal.Echo("Error!")
    
    Terminal.Style("reset")
    Terminal.Echo("Back to normal")
}
```

Output:
```
Success!              (in green)
Error!               (in red)
Back to normal       (in normal color)
```

## Using Styles Strategically

### Style 1: Important Messages

```ictl
Program.Main {
    Terminal.Style("bold")
    Terminal.Echo("=== WELCOME ===")
    Terminal.Style("reset")
    
    Terminal.Echo("Type 'help' for assistance")
}
```

### Style 2: Messages of Different Importance

```ictl
Program.Main {
    Variables.New(Score)
    Variables.Score = Terminal.Ask("Enter your score: ")
    
    Program.If(Math.Compare(Variables.Score, ">=", 90)) {
        Terminal.Style("green")
        Terminal.Echo("Excellent!")
    }
    
    Program.If(Math.Compare(Variables.Score, ">=", 70)) {
        Program.If(Math.Compare(Variables.Score, "<", 90)) {
            Terminal.Style("yellow")
            Terminal.Echo("Good work!")
        }
    }
    
    Program.If(Math.Compare(Variables.Score, "<", 70)) {
        Terminal.Style("red")
        Terminal.Echo("Study more!")
    }
    
    Terminal.Style("reset")
}
```

## Real-World Example: Status Report

```ictl
Program.Main {
    Terminal.Style("bold")
    Terminal.Echo("=== SYSTEM STATUS ===")
    Terminal.Style("reset")
    
    Terminal.Style("green")
    Terminal.Echo("[✓] Database: Connected")
    
    Terminal.Style("green")
    Terminal.Echo("[✓] Server: Running")
    
    Terminal.Style("yellow")
    Terminal.Echo("[!] Memory: 85%")
    
    Terminal.Style("reset")
    
    Terminal.Echo("")
    Terminal.Echo("Status last updated: 2024")
}
```

## Real-World Example: Interactive Menu with Styles

```ictl
Program.Main {
    Variables.New(Choice)
    
    Program.ForeverLoop {
        Terminal.Style("bold")
        Terminal.Echo("=== MAIN MENU ===")
        Terminal.Style("reset")
        
        Terminal.Echo("1. New Game")
        Terminal.Echo("2. Load Game")
        Terminal.Echo("3. Settings")
        Terminal.Echo("4. Quit")
        
        Terminal.Style("cyan")
        Variables.Choice = Terminal.Ask("Select option (1-4): ")
        Terminal.Style("reset")
        
        Program.If(Data.Compare(Variables.Choice, "1")) {
            Terminal.Style("green")
            Terminal.Echo("Starting new game...")
            Terminal.Style("reset")
        }
        
        Program.If(Data.Compare(Variables.Choice, "2")) {
            Terminal.Style("blue")
            Terminal.Echo("Loading saved game...")
            Terminal.Style("reset")
        }
        
        Program.If(Data.Compare(Variables.Choice, "3")) {
            Terminal.Style("yellow")
            Terminal.Echo("Opening settings...")
            Terminal.Style("reset")
        }
        
        Program.If(Data.Compare(Variables.Choice, "4")) {
            Terminal.Style("red")
            Terminal.Echo("Thanks for playing!")
            Terminal.Style("reset")
            Program.BreakLoop
        }
    }
}
```

## Real-World Example: Login System with Styles

```ictl
Program.Main {
    Variables.New(Username)
    Variables.New(Password)
    Variables.New(CorrectPassword)
    Variables.New(Attempts)
    
    Terminal.Style("bold")
    Terminal.Echo("=== LOGIN SYSTEM ===")
    Terminal.Style("reset")
    
    Variables.CorrectPassword = "secret123"
    Variables.Attempts = 0
    
    Program.ForeverLoop {
        Variables.Username = Terminal.Ask("Username: ")
        Variables.Password = Terminal.Ask("Password: ")
        Variables.Attempts = Math.Eval(Variables.Attempts + 1)
        
        Program.If(Data.Compare(Variables.Password, Variables.CorrectPassword)) {
            Terminal.Style("green")
            Terminal.Echo("Login successful!")
            Terminal.Style("reset")
            Program.BreakLoop
        }
        
        Program.If(Math.Compare(Variables.Attempts, "<", 3)) {
            Terminal.Style("yellow")
            Terminal.Echo("Incorrect password. Try again.")
            Terminal.Style("reset")
        }
        
        Program.If(Math.Compare(Variables.Attempts, ">=", 3)) {
            Terminal.Style("red")
            Terminal.Echo("Too many failed attempts!")
            Terminal.Style("reset")
            Program.BreakLoop
        }
    }
}
```

## Best Practices for Styling

### 1. Don't Overuse Colors

```ictl
# Too much - hard to read
Terminal.Style("red")
Terminal.Echo("This")
Terminal.Style("blue")
Terminal.Echo("is")
Terminal.Style("green")
Terminal.Echo("hard")
Terminal.Style("yellow")
Terminal.Echo("to")
Terminal.Style("magenta")
Terminal.Echo("read!")
```

### 2. Use Colors to Guide Users

```ictl
# Good - clear guidance
Terminal.Style("green")
Terminal.Echo("✓ This worked")

Terminal.Style("red")
Terminal.Echo("✗ This failed")

Terminal.Style("yellow")
Terminal.Echo("⚠ Warning!")

Terminal.Style("reset")
```

### 3. Always Reset After Using Styles

```ictl
Terminal.Style("bold")
Terminal.Echo("Important!")
Terminal.Style("reset")  # Don't forget this!
```

Without reset, all following text might stay bold.

## Real-World Example: Game Status Display

```ictl
Program.Main {
    Variables.New(Health)
    Variables.New(Mana)
    Variables.New(Level)
    
    Variables.Health = 100
    Variables.Mana = 50
    Variables.Level = 5
    
    Terminal.Style("bold")
    Terminal.Echo("=== PLAYER STATUS ===")
    Terminal.Style("reset")
    
    Terminal.Style("red")
    Terminal.Echo("Health: " + Variables.Health)
    Terminal.Style("reset")
    
    Terminal.Style("blue")
    Terminal.Echo("Mana: " + Variables.Mana)
    Terminal.Style("reset")
    
    Terminal.Style("yellow")
    Terminal.Echo("Level: " + Variables.Level)
    Terminal.Style("reset")
}
```

## Real-World Example: Progress Report

```ictl
Program.Main {
    Variables.New(Progress)
    Variables.New(Step)
    
    Terminal.Style("bold")
    Terminal.Echo("=== PROCESSING ===")
    Terminal.Style("reset")
    
    Variables.Step = 1
    
    Program.Loop(5) {
        Terminal.Style("cyan")
        Terminal.Echo("Step " + Variables.Step + ": Running...")
        Terminal.Style("reset")
        
        Variables.Step = Math.Eval(Variables.Step + 1)
    }
    
    Terminal.Style("green")
    Terminal.Echo("")
    Terminal.Echo("All steps completed!")
    Terminal.Style("reset")
}
```

## Color Guide for Different Purposes

| Purpose | Color | Example |
|---------|-------|---------|
| Success | green | "Operation completed!" |
| Error | red | "Something went wrong!" |
| Warning | yellow | "Be careful!" |
| Info | cyan/blue | "Loading..." |
| Important | bold | "=== TITLE ===" |
| Headers | bold + color | Important headings |

## Practice Exercise

Write a program that:

1. Creates a "To-Do List" interface
2. Shows different items in different colors
3. Shows completed items in green
4. Shows pending items in yellow
5. Shows urgent items in red

**Hint:**
```ictl
Program.Main {
    Terminal.Style("bold")
    Terminal.Echo("=== TO-DO LIST ===")
    Terminal.Style("reset")
    
    Terminal.Style("green")
    Terminal.Echo("[✓] Buy groceries")
    
    Terminal.Style("yellow")
    Terminal.Echo("[~] Call mom")
    
    Terminal.Style("red")
    Terminal.Echo("[✗] Finish project - DUE TODAY")
    
    Terminal.Style("reset")
}
```

## Summary

You now know:
- ✅ How to use `Terminal.Style()` to change colors
- ✅ Available color options
- ✅ When and why to use colors
- ✅ Best practices for styling
- ✅ How to reset styles

---

**Next Chapter:** Troubleshooting and tips for writing better programs!
