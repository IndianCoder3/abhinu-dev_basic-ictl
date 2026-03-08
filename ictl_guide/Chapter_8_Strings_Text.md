# Chapter 8: Working with Strings and Text

## What is a String?

A **string** is text - words, sentences, or even just a single character. In ICTL, strings always go in quotation marks:

```ictl
"Hello"
"Alice"
"The quick brown fox"
"123"
"!"
""
```

Even numbers in quotes are strings:
- `"123"` is the text "one-two-three" (text)
- `123` is the number one hundred twenty-three (number)

This matters for what you can do with them!

## Creating String Variables

```ictl
Program.Main {
    Variables.New(Greeting)
    Variables.Greeting = "Hello, World!"
    
    Terminal.Echo(Variables.Greeting)
}
```

Output:
```
Hello, World!
```

## String Concatenation (Joining Strings)

Use the `+` operator to join (concatenate) strings together:

```ictl
Program.Main {
    Variables.New(FirstName)
    Variables.New(LastName)
    Variables.New(FullName)
    
    Variables.FirstName = "Alice"
    Variables.LastName = "Smith"
    
    Variables.FullName = Variables.FirstName + " " + Variables.LastName
    
    Terminal.Echo(Variables.FullName)
}
```

Output:
```
Alice Smith
```

Notice the space `" "` between the names - without it, you'd get "AliceSmith"!

## Combining Text and Numbers

You can mix strings and numbers:

```ictl
Program.Main {
    Variables.New(Age)
    Variables.Age = 25
    
    Terminal.Echo("My age is " + Variables.Age)
}
```

Output:
```
My age is 25
```

ICTL automatically converts the number to text when concatenating!

## Real-World Example: Friendly Greeting

```ictl
Program.Main {
    Variables.New(Name)
    Variables.New(Hobby)
    Variables.New(Age)
    
    Variables.Name = Terminal.Ask("What is your name? ")
    Variables.Hobby = Terminal.Ask("What is your hobby? ")
    Variables.Age = Terminal.Ask("How old are you? ")
    
    Terminal.Echo("Nice to meet you, " + Variables.Name + "!")
    Terminal.Echo("So you like " + Variables.Hobby + " and you're " + Variables.Age + "?")
    Terminal.Echo("That's awesome!")
}
```

Sample run:
```
What is your name? Bob
What is your hobby? coding
How old are you? 30
Nice to meet you, Bob!
So you like coding and you're 30?
That's awesome!
```

## String Comparison

Use `Data.Compare()` to check if strings are equal:

```ictl
Program.Main {
    Variables.New(Username)
    Variables.New(CorrectPassword)
    Variables.New(EnteredPassword)
    
    Variables.CorrectPassword = "secret123"
    
    Variables.EnteredPassword = Terminal.Ask("Enter password: ")
    
    Program.If(Data.Compare(Variables.EnteredPassword, Variables.CorrectPassword)) {
        Terminal.Echo("Password correct!")
    }
    
    Program.If(Data.Compare(Variables.EnteredPassword, "secret123")) {
        Terminal.Echo("Welcome!")
    }
}
```

## Empty Strings

An empty string is a string with no content:

```ictl
Program.Main {
    Variables.New(Message)
    Variables.Message = ""
    
    Program.If(Data.Compare(Variables.Message, "")) {
        Terminal.Echo("The message is empty!")
    }
}
```

## Strings with Special Characters

You can use special characters inside strings:

```ictl
Variables.New(Text)
Variables.Text = "Hello! How are you?"

Terminal.Echo(Variables.Text)
```

Output:
```
Hello! How are you?
```

### Common Characters:

```ictl
"!"      # Exclamation mark
"?"      # Question mark
"-"      # Dash
"..."    # Ellipsis
"@"      # At symbol
"#"      # Hash
"$"      # Dollar sign
" "      # Space (important!)
","      # Comma
"."      # Period
```

## Real-World Example: Mad Libs Game

Mad Libs is a fun game where you ask for random words and put them in a story:

```ictl
Program.Main {
    Variables.New(Name)
    Variables.New(Color)
    Variables.New(Animal)
    Variables.New(Food)
    
    Variables.Name = Terminal.Ask("Enter a name: ")
    Variables.Color = Terminal.Ask("Enter a color: ")
    Variables.Animal = Terminal.Ask("Enter an animal: ")
    Variables.Food = Terminal.Ask("Enter a food: ")
    
    Terminal.Echo("")
    Terminal.Echo("=== YOUR STORY ===")
    Terminal.Echo("")
    Terminal.Echo("Once upon a time, there was a " + Variables.Color + " " + Variables.Animal + ".")
    Terminal.Echo("The " + Variables.Animal + " belonged to a person named " + Variables.Name + ".")
    Terminal.Echo("One day, " + Variables.Name + " gave the " + Variables.Animal + " some " + Variables.Food + ".")
    Terminal.Echo("The " + Variables.Animal + " was very happy!")
}
```

Sample run:
```
Enter a name: Charlie
Enter a color: purple
Enter an animal: elephant
Enter a food: pizza

=== YOUR STORY ===

Once upon a time, there was a purple elephant.
The elephant belonged to a person named Charlie.
One day, Charlie gave the elephant some pizza.
The elephant was very happy!
```

## Real-World Example: Simple Story Generator

```ictl
Program.Main {
    Variables.New(Hero)
    Variables.New(Villain)
    Variables.New(Magic)
    
    Variables.Hero = Terminal.Ask("Hero name: ")
    Variables.Villain = Terminal.Ask("Villain name: ")
    Variables.Magic = Terminal.Ask("Magic power: ")
    
    Terminal.Echo("")
    Terminal.Echo(Variables.Hero + " discovered a hidden power: " + Variables.Magic + "!")
    Terminal.Echo("With this power, " + Variables.Hero + " knew they could defeat " + Variables.Villain + ".")
    Terminal.Echo("The battle was epic. " + Variables.Hero + " won!")
    Terminal.Echo("The world was safe. " + Variables.Villain + " was defeated.")
}
```

## Combining Strings and Math

You can combine mathematical results with text:

```ictl
Program.Main {
    Variables.New(A)
    Variables.New(B)
    Variables.New(Sum)
    
    Variables.A = Terminal.Ask("First number: ")
    Variables.B = Terminal.Ask("Second number: ")
    Variables.Sum = Math.Eval(Variables.A + Variables.B)
    
    Terminal.Echo(Variables.A + " + " + Variables.B + " = " + Variables.Sum)
}
```

Sample run:
```
First number: 7
Second number: 3
7 + 3 = 10
```

## Common Mistakes

### Mistake 1: Forgetting Quotes

```ictl
Terminal.Echo("Hello")    # Correct - in quotes
Terminal.Echo(Hello)      # Wrong - missing quotes
```

### Mistake 2: Quotes at the Wrong Place

```ictl
Variables.Text = "Hello"  # Correct
"Variables.Text" = "Hello"  # Wrong - the variable name shouldn't be in quotes
```

### Mistake 3: Spaces Matter

```ictl
Variables.FirstName + Variables.LastName  # Output: "AliceSmith"
Variables.FirstName + " " + Variables.LastName  # Output: "Alice Smith"
```

Notice the difference!

## Practice Exercise

Write a program that:

1. Asks the user for their favorite book, movie, and sport
2. Creates a message that says they like all three things
3. Example: "I love reading [Book], watching [Movie], and playing [Sport]!"

**Hint:**
```ictl
Program.Main {
    Variables.New(Book)
    Variables.New(Movie)
    Variables.New(Sport)
    
    Variables.Book = Terminal.Ask("Favorite book: ")
    # Continue from here...
}
```

## Summary

You now know:
- ✅ What strings are (text in quotes)
- ✅ How to create string variables
- ✅ How to concatenate strings with `+`
- ✅ How to mix strings and numbers
- ✅ How to compare strings with `Data.Compare()`
- ✅ How to use special characters in strings

---

**Next Chapter:** Let's put it all together with some complete programs!
