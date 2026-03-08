# Chapter 5: Math and Calculations

## Basic Arithmetic

ICTL can do math for you using `Math.Eval()`. This command evaluates (solves) math expressions.

### Addition

```ictl
Program.Main {
    Terminal.Echo(Math.Eval(2 + 3))
}
```

Output:
```
5
```

### Subtraction

```ictl
Terminal.Echo(Math.Eval(10 - 3))
```

Output:
```
7
```

### Multiplication

```ictl
Terminal.Echo(Math.Eval(4 * 5))
```

Output:
```
20
```

### Division

```ictl
Terminal.Echo(Math.Eval(20 / 4))
```

Output:
```
5
```

## Storing Math Results

You usually want to save the result of a calculation in a variable:

```ictl
Program.Main {
    Variables.New(Result)
    Variables.Result = Math.Eval(10 + 5)
    
    Terminal.Echo("10 + 5 = " + Variables.Result)
}
```

Output:
```
10 + 5 = 15
```

## Using Variables in Calculations

You can use the values stored in variables:

```ictl
Program.Main {
    Variables.New(FirstNumber)
    Variables.New(SecondNumber)
    Variables.New(Answer)
    
    Variables.FirstNumber = 7
    Variables.SecondNumber = 3
    
    Variables.Answer = Math.Eval(Variables.FirstNumber + Variables.SecondNumber)
    
    Terminal.Echo(Variables.FirstNumber + " + " + Variables.SecondNumber + " = " + Variables.Answer)
}
```

Output:
```
7 + 3 = 10
```

## Order of Operations (PEMDAS)

Math follows the same order of operations you learned in school!

**P** - Parentheses first
**E** - Exponents (not supported in ICTL yet)
**M** - Multiplication
**D** - Division  
**A** - Addition
**S** - Subtraction

### Example Without Parentheses:

```ictl
Terminal.Echo(Math.Eval(2 + 3 * 4))
```

This calculates:
- First: 3 * 4 = 12
- Then: 2 + 12 = 14

Output:
```
14
```

### Example With Parentheses:

```ictl
Terminal.Echo(Math.Eval((2 + 3) * 4))
```

This calculates:
- First: (2 + 3) = 5
- Then: 5 * 4 = 20

Output:
```
20
```

**Use parentheses if you want to change the order!**

## Decimals in Math

You can work with decimal numbers:

```ictl
Program.Main {
    Variables.New(Price)
    Variables.Price = Math.Eval(19.99 + 5.50)
    
    Terminal.Echo("Total: " + Variables.Price)
}
```

Output:
```
Total: 25.49
```

## Negative Numbers

Negative numbers work fine:

```ictl
Terminal.Echo(Math.Eval(-10 + 5))      # Result: -5
Terminal.Echo(Math.Eval(-3 * -4))      # Result: 12
Terminal.Echo(Math.Eval((-2 + 8) - 5)) # Result: 1
```

## Real-World Example: Calculating a Discount

Let's calculate a discount on a purchase:

```ictl
Program.Main {
    Variables.New(OriginalPrice)
    Variables.New(DiscountPercent)
    Variables.New(DiscountAmount)
    Variables.New(FinalPrice)
    
    Variables.OriginalPrice = 100
    Variables.DiscountPercent = 20
    
    # Calculate 20% of 100
    Variables.DiscountAmount = Math.Eval(Variables.OriginalPrice * Variables.DiscountPercent / 100)
    
    # Subtract discount from original price
    Variables.FinalPrice = Math.Eval(Variables.OriginalPrice - Variables.DiscountAmount)
    
    Terminal.Echo("Original Price: $" + Variables.OriginalPrice)
    Terminal.Echo("Discount: " + Variables.DiscountPercent + "%")
    Terminal.Echo("Discount Amount: $" + Variables.DiscountAmount)
    Terminal.Echo("Final Price: $" + Variables.FinalPrice)
}
```

Output:
```
Original Price: $100
Discount: 20%
Discount Amount: $20
Final Price: $80
```

## Math with User Input

You can take user input and use it in calculations:

```ictl
Program.Main {
    Variables.New(Width)
    Variables.New(Height)
    Variables.New(Area)
    
    Variables.Width = Terminal.Ask("Enter width: ")
    Variables.Height = Terminal.Ask("Enter height: ")
    
    # Calculate area
    Variables.Area = Math.Eval(Variables.Width * Variables.Height)
    
    Terminal.Echo("The area is: " + Variables.Area)
}
```

Sample run:
```
Enter width: 5
Enter height: 3
The area is: 15
```

## Comparing Numbers

Often you need to compare numbers to make decisions. Use `Math.Compare()`:

```ictl
Math.Compare(10, ">", 5)    # Is 10 greater than 5? Yes -> True
Math.Compare(3, "<", 7)     # Is 3 less than 7? Yes -> True
Math.Compare(5, "==", 5)    # Is 5 equal to 5? Yes -> True
```

### Comparison Operators:

- `>` - Greater than
- `<` - Less than
- `>=` - Greater than or equal to
- `<=` - Less than or equal to
- `==` - Equal to
- `!=` - Not equal to

We'll use these more in the next chapter on making decisions!

## Practice Exercise

Write a program that:

1. Asks the user for three test scores
2. Calculates the average
3. Displays the average

**Hint:** Average = (score1 + score2 + score3) / 3

```ictl
Program.Main {
    Variables.New(Score1)
    Variables.New(Score2)
    Variables.New(Score3)
    Variables.New(Average)
    
    Variables.Score1 = Terminal.Ask("Enter first score: ")
    Variables.Score2 = Terminal.Ask("Enter second score: ")
    Variables.Score3 = Terminal.Ask("Enter third score: ")
    
    # Calculate average...
}
```

## Summary

You now know:
- ✅ Basic arithmetic: +, -, *, /
- ✅ How to use `Math.Eval()`
- ✅ Order of operations (parentheses matter!)
- ✅ Working with decimals
- ✅ Working with negative numbers
- ✅ Comparing numbers with `Math.Compare()`

---

**Next Chapter:** Let's make decisions with if statements!
