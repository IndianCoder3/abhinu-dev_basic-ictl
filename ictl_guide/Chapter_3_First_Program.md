# Chapter 3: Your First ICTL Program

## The Simplest Program Ever

Let's start with the absolute simplest program you can write in ICTL:

```ictl
Program.Main {
    Terminal.Echo("Hello, World!")
}
```

### Let's break this down:

- **`Program.Main { ... }`** - This is your program's starting point. Every program needs this!
- **`Terminal.Echo()`** - This command displays text on the screen
- **`"Hello, World!"`** - This is the text we want to display (notice the quotation marks)

### How to run it:

1. **Create a new file** called `hello.ictl` in a text editor
2. **Copy the code above** into it
3. **Save the file**
4. **Open your terminal** in the same folder
5. **Type:** `ICTL-v1.0s.exe hello.ictl`

You should see:
```
Hello, World!
```

**Congratulations! You just wrote your first program!** 🎉

## Making It Interactive

Let's make your program more interesting by asking for the user's name:

```ictl
Program.Main {
    Terminal.Echo("What is your name?")
}
```

Run this and you'll see the question, but we can't actually get the answer yet. Let's learn how to ask for input!

## Getting Input from the User

Use `Terminal.Ask()` to ask questions:

```ictl
Program.Main {
    Terminal.Ask("What is your name? ")
}
```

This asks the question, but we need to **store** the answer somewhere. That's where variables come in!

## Your First Variable

A **variable** is like a storage box that remembers information.

```ictl
Program.Main {
    Variables.New(Name)
}
```

This creates an empty storage box labeled "Name".

Now let's store the user's answer in this box:

```ictl
Program.Main {
    Variables.New(Name)
    Variables.Name = Terminal.Ask("What is your name? ")
}
```

This says: "Create a variable called Name, then ask the user for their name and store their answer in the Name variable."

The `=` means "store" or "remember this value".

## Combining Everything

Now let's display the name back to the user:

```ictl
Program.Main {
    Variables.New(Name)
    Variables.Name = Terminal.Ask("What is your name? ")
    Terminal.Echo("Nice to meet you, " + Variables.Name)
}
```

Let me explain the last line:
- **`"Nice to meet you, "`** - This is the first piece of text
- **`+`** - This combines (concatenates) two pieces of text together
- **`Variables.Name`** - This is what we stored earlier

So if the user types "Alice", the program will display: `Nice to meet you, Alice`

### Full Example:

Here's a complete, working program:

```ictl
Program.Main {
    Variables.New(Name)
    Variables.New(Age)
    
    Variables.Name = Terminal.Ask("What is your name? ")
    Variables.Age = Terminal.Ask("How old are you? ")
    
    Terminal.Echo("Hello, " + Variables.Name + "!")
    Terminal.Echo("You are " + Variables.Age + " years old.")
}
```

When you run this, it might look like:
```
What is your name? Alice
How old are you? 25
Hello, Alice!
You are 25 years old.
```

## Understanding the Order

**Important:** ICTL reads your code from top to bottom, one line at a time.

```ictl
Program.Main {
    Terminal.Echo("First, this prints")
    Terminal.Echo("Then, this prints")
    Terminal.Echo("Finally, this prints")
}
```

This will print:
```
First, this prints
Then, this prints
Finally, this prints
```

Not in any other order!

## Using Comments

Comments are notes you write for yourself. ICTL ignores them, but they help explain your code:

```ictl
Program.Main {
    # This is a comment
    Terminal.Echo("Hello!")  # You can also add comments at the end of lines
    
    # Create a variable for the user's name
    Variables.New(Name)
    Variables.Name = Terminal.Ask("What is your name? ")
    
    # Greet the user
    Terminal.Echo("Hello, " + Variables.Name)
}
```

Comments start with `#` and go until the end of the line.

## Practice Exercise

Try writing a program that:

1. Asks for the user's favorite food
2. Asks for their favorite color
3. Displays both answers back to them

**Hint:** Here's the structure to get you started:

```ictl
Program.Main {
    Variables.New(Food)
    Variables.New(Color)
    
    # Your code here...
    
    Terminal.Echo("Your favorite food is " + Variables.Food)
    Terminal.Echo("Your favorite color is " + Variables.Color)
}
```

## Summary

You now know:
- ✅ How to create a basic program
- ✅ How to display text with `Terminal.Echo()`
- ✅ How to ask questions with `Terminal.Ask()`
- ✅ How to create variables with `Variables.New()`
- ✅ How to store values with `=`
- ✅ How to combine text with `+`
- ✅ How to write comments with `#`

---

**Next Chapter:** Let's learn more about different types of data you can work with!
