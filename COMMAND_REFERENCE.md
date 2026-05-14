# ICTL Complete Command Reference

**Last Updated:** May 2, 2026  
**Version:** Basic ICTL v26.05.01 (v1.2 scheme)  

---

## Table of Contents
1. [Terminal Commands](#terminal-commands)
2. [Variables Commands](#variables-commands)
3. [Data Commands](#data-commands)
4. [Math Commands](#math-commands)
5. [Time Commands](#time-commands)
6. [Lists Commands](#lists-commands)
7. [Kachua (Turtle Graphics) Commands](#kachua-turtle-graphics-commands)
8. [GUI Commands](#gui-commands)
9. [Program Block Structures](#program-block-structures)
10. [Program Expression Commands](#program-expression-commands)

---

> [!CAUTION]
> Kachua and GUI commands are still in Beta, heavy contribution is needed here! If you are an end user, remember that there can be bugs. Exploits are possible, although we have no seen any, but beware.

---

## Terminal Commands

### Terminal.Echo()
**Description:** Print a value to the terminal output.  
**Syntax:** `Terminal.Echo(value)`  
**Parameters:**
- `value` - Any value to print (string, number, variable, expression)

**Examples:**
```ictl
Terminal.Echo("Hello World")
Terminal.Echo(42)
Terminal.Echo(Variables.MyVar)
Terminal.Echo("Result: " + Variables.X)
```

---

### Terminal.Ask()
**Description:** Ask user for input and return the response as a string.  
**Syntax:** `Terminal.Ask(prompt)`  
**Parameters:**
- `prompt` - The question to display to the user

**Return:** String input from user

**Examples:**
```ictl
Variables.Name = Terminal.Ask("What is your name? ")
Variables.Age = Terminal.Ask("Enter your age: ")
```

---

### Terminal.Clear()
**Description:** Clear the terminal screen (cross-platform compatible).  
**Syntax:** `Terminal.Clear()`  
**Parameters:** None

**Examples:**
```ictl
Terminal.Clear()
```

---

### Terminal.Style()
**Description:** Set the terminal text color/style.  
**Syntax:** `Terminal.Style(color)`  
**Parameters:**
- `color` - Color name string

**Supported Colors:**
- `"red"` - Red text
- `"green"` - Green text
- `"blue"` - Blue text
- `"yellow"` - Yellow text
- `"cyan"` - Cyan text
- `"magenta"` - Magenta text
- `"bold"` - Bold text
- `"reset"` - Reset to default

**Examples:**
```ictl
Terminal.Style("red")
Terminal.Echo("This is red!")
Terminal.Style("reset")
Terminal.Echo("Back to normal")
```

---

## Variables Commands

### Variables Assignment
**Description:** Create and assign a value to a variable.  
**Syntax:** `Variables.{name} = value`  
**Parameters:**
- `name` - Variable name (must be valid identifier)
- `value` - Any value (number, string, expression result, function return)

**Examples:**
```ictl
Variables.X = 42
Variables.Name = "Alice"
Variables.Result = Math.Eval(10 + 5)
Variables.Input = Terminal.Ask("Enter value: ")
```

---

### Variables Access
**Description:** Access a variable's value in expressions.  
**Syntax:** `Variables.{name}`  
**Return:** The variable's value

**Examples:**
```ictl
Terminal.Echo(Variables.X)
Variables.Y = Variables.X + 10
```

---

### Variables.New() [DEPRECATED]
**Description:** (Deprecated) Variables are now auto-created on assignment.  
**Syntax:** `Variables.New(name)`  
**Note:** Use direct assignment instead.

---

## Data Commands

### Data.Compare()
**Description:** Compare two values for strict equality (type matters).  
**Syntax:** `Data.Compare(a, b)`  
**Parameters:**
- `a` - First value
- `b` - Second value

**Return:** `True` or `False`

**Examples:**
```ictl
Terminal.Echo(Data.Compare(123, 123))           # True
Terminal.Echo(Data.Compare(123, "123"))         # False (different types)
Terminal.Echo(Data.Compare("hello", "hello"))   # True
```

---

### Data.LooseCompare()
**Description:** Compare two values for equality (type-insensitive).  
**Syntax:** `Data.LooseCompare(a, b)`  
**Parameters:**
- `a` - First value
- `b` - Second value

**Return:** `True` or `False`

**Examples:**
```ictl
Terminal.Echo(Data.LooseCompare(123, "123"))  # True (both convert to "123")
Terminal.Echo(Data.LooseCompare(42, 42))      # True
```

---

### Data.ToInt()
**Description:** Convert a value to an integer.  
**Syntax:** `Data.ToInt(value)`  
**Parameters:**
- `value` - Value to convert (number or numeric string)

**Return:** Integer value

**Examples:**
```ictl
Variables.X = Data.ToInt(3.14)      # Returns 3
Variables.Y = Data.ToInt("42")      # Returns 42
```

---

### Data.ToFloat()
**Description:** Convert a value to a floating-point number.  
**Syntax:** `Data.ToFloat(value)`  
**Parameters:**
- `value` - Value to convert (number or numeric string)

**Return:** Float value

**Examples:**
```ictl
Variables.X = Data.ToFloat(42)      # Returns 42.0
Variables.Y = Data.ToFloat("3.14")  # Returns 3.14
```

---

### Data.ToString()
**Description:** Convert a value to a string.  
**Syntax:** `Data.ToString(value)`  
**Parameters:**
- `value` - Any value to convert

**Return:** String representation

**Examples:**
```ictl
Variables.Text = Data.ToString(42)  # Returns "42"
Variables.Text = Data.ToString(True) # Returns "True"
```

---

### Data.TypeOf()
**Description:** Get the data type of a value as a string.  
**Syntax:** `Data.TypeOf(value)`  
**Parameters:**
- `value` - Any value

**Return:** Type name (e.g., "int", "float", "str", "bool", "list")

**Examples:**
```ictl
Terminal.Echo(Data.TypeOf(42))           # "int"
Terminal.Echo(Data.TypeOf(3.14))         # "float"
Terminal.Echo(Data.TypeOf("hello"))      # "str"
Terminal.Echo(Data.TypeOf(True))         # "bool"
```

---

## Math Commands

### Math.Eval()
**Description:** Evaluate a mathematical expression.  
**Syntax:** `Math.Eval(expression)`  
**Parameters:**
- `expression` - Mathematical expression string

**Return:** Numeric result (int or float)

**Supported Operators:** `+`, `-`, `*`, `/`, `^` (power)  
**Supported Functions:** `sqrt`, `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `sinh`, `cosh`, `tanh`, `log`, `log10`, `exp`, `abs`, `floor`, `ceil`, `round`, `degrees`, `radians`

**Examples:**
```ictl
Terminal.Echo(Math.Eval(2 + 2))           # 4
Terminal.Echo(Math.Eval(10 * 5))          # 50
Terminal.Echo(Math.Eval(sqrt(16)))        # 4
Terminal.Echo(Math.Eval(2 ^ 3))           # 8 (2 to the power of 3)
Terminal.Echo(Math.Eval(sin(0)))          # 0
Terminal.Echo(Math.Eval(Variables.X + 10)) # X + 10
```

---

### Math.Compare()
**Description:** Compare two numeric values using a comparison operator.  
**Syntax:** `Math.Compare(a, operator, b)`  
**Parameters:**
- `a` - First number
- `operator` - Comparison operator: `"=="`, `"!="`, `">"`, `"<"`, `">="`, `"<="`
- `b` - Second number

**Return:** `True` or `False`

**Examples:**
```ictl
Terminal.Echo(Math.Compare(10, ">", 5))    # True
Terminal.Echo(Math.Compare(3, "<", 3))     # False
Terminal.Echo(Math.Compare(5, "==", 5))    # True
Terminal.Echo(Math.Compare(10, "!=", 20))  # True
```

---

### Math.Random()
**Description:** Generate a random integer between min and max (inclusive).  
**Syntax:** `Math.Random(min, max)`  
**Parameters:**
- `min` - Minimum value (inclusive)
- `max` - Maximum value (inclusive)

**Return:** Random integer

**Examples:**
```ictl
Variables.DiceRoll = Math.Random(1, 6)      # Random number 1-6
Variables.Coin = Math.Random(0, 1)          # Random 0 or 1
Terminal.Echo(Math.Random(100, 999))        # Random 3-digit number
```

---

### Math.NumPy()
**Description:** Evaluate expression using NumPy numerical library.  
**Syntax:** `Math.NumPy(expression)`  
**Parameters:**
- `expression` - Mathematical expression for NumPy

**Return:** Numeric result

**Examples:**
```ictl
Terminal.Echo(Math.NumPy(2 ^ 10))
Terminal.Echo(Math.NumPy(sqrt(2)))
```

---

### Math.SymPy()
**Description:** Evaluate expression using SymPy symbolic math library.  
**Syntax:** `Math.SymPy(expression)`  
**Parameters:**
- `expression` - Mathematical/symbolic expression

**Return:** Result (numeric or simplified)

**Examples:**
```ictl
Terminal.Echo(Math.SymPy(sqrt(4)))
Terminal.Echo(Math.SymPy(sqrt(2)))
```

---

## Time Commands

### Time.Current()
**Description:** Get the current date/time in specified format.  
**Syntax:** `Time.Current(format)`  
**Parameters:**
- `format` - Format string with placeholders

**Format Placeholders:**
- `YYYY` - 4-digit year
- `YY` - 2-digit year
- `MM` - 2-digit month
- `DD` - 2-digit day
- `HH` - Hour (24-hour)
- `hh` - Hour (12-hour)
- `mm` - Minutes
- `ss` - Seconds
- `tt` - AM/PM

**Return:** Formatted date/time string

**Examples:**
```ictl
Terminal.Echo(Time.Current("YYYY-MM-DD"))           # 2026-04-07
Terminal.Echo(Time.Current("HH:mm:ss"))             # 14:30:45
Terminal.Echo(Time.Current("MM/DD/YYYY hh:mm tt"))  # 04/07/2026 02:30 PM
Variables.Now = Time.Current("YYYY-MM-DD")
```

---

### Time.Wait()
**Description:** Pause execution for specified number of seconds.  
**Syntax:** `Time.Wait(seconds)`  
**Parameters:**
- `seconds` - Number of seconds to wait (int or float)

**Examples:**
```ictl
Terminal.Echo("Starting...")
Time.Wait(2)
Terminal.Echo("2 seconds later!")
Time.Wait(0.5)  # Wait half a second
```

---

## Lists Commands

### Lists.Create()
**Description:** Create a new list.  
**Syntax:** `Lists.Create(name)` or `Lists.Create(name, [items])`  
**Parameters:**
- `name` - List name
- `items` (optional) - Initial list items

**Examples:**
```ictl
Lists.Create(MyList)
Lists.Create(Numbers, [1, 2, 3, 4, 5])
Lists.Create(Names, ["Alice", "Bob", "Charlie"])
```

---

### Lists Assignment
**Description:** Initialize a list with items using assignment.  
**Syntax:** `Lists.{name} = [item1, item2, ...]`  
**Parameters:**
- `name` - List name
- `item1, item2, ...` - Items (can be values, variables, expressions)

**Examples:**
```ictl
Lists.Numbers = [1, 2, 3, 4, 5]
Lists.Names = ["Alice", "Bob"]
Lists.Mixed = [1, "text", Math.Eval(2 + 2)]
Lists.FromVariables = [Variables.X, Variables.Y]
```

---

### Lists.Get()
**Description:** Get an item from a list by index (0-based).  
**Syntax:** `Lists.Get(name, index)`  
**Parameters:**
- `name` - List name
- `index` - Item index (0-based)

**Return:** Item at that index

**Examples:**
```ictl
Variables.First = Lists.Get(MyList, 0)
Terminal.Echo(Lists.Get(Numbers, 2))     # Get 3rd item
```

---

### Lists.Push()
**Description:** Add an item to the end of a list.  
**Syntax:** `Lists.Push(name, item)`  
**Parameters:**
- `name` - List name
- `item` - Item to add

**Examples:**
```ictl
Lists.Push(MyList, 42)
Lists.Push(Names, "Diana")
Lists.Push(MyList, Variables.X)
```

---

### Lists.Pop()
**Description:** Remove and return the last item from a list.  
**Syntax:** `Lists.Pop(name)`  
**Parameters:**
- `name` - List name

**Return:** The removed item

**Examples:**
```ictl
Variables.Last = Lists.Pop(MyList)
Terminal.Echo(Lists.Pop(Numbers))
```

---

### Lists.Length()
**Description:** Get the number of items in a list.  
**Syntax:** `Lists.Length(name)`  
**Parameters:**
- `name` - List name

**Return:** Number of items (int)

**Examples:**
```ictl
Variables.Count = Lists.Length(MyList)
Terminal.Echo(Lists.Length(Numbers))
Program.If(Math.Compare(Lists.Length(MyList), ">", 0)) {
    Terminal.Echo("List is not empty")
}
```

---

### Lists.Clear()
**Description:** Remove all items from a list.  
**Syntax:** `Lists.Clear(name)`  
**Parameters:**
- `name` - List name

**Examples:**
```ictl
Lists.Clear(MyList)
```

---

### Lists.Delete()
**Description:** Delete an entire list.  
**Syntax:** `Lists.Delete(name)`  
**Parameters:**
- `name` - List name

**Examples:**
```ictl
Lists.Delete(MyList)
```

---

### Lists.Contains()
**Description:** Check if a list contains a specific item.  
**Syntax:** `Lists.Contains(name, item)`  
**Parameters:**
- `name` - List name
- `item` - Item to search for

**Return:** `True` or `False`

**Examples:**
```ictl
Program.If(Lists.Contains(Names, "Alice")) {
    Terminal.Echo("Alice is in the list")
}
```

---

### Lists.Set()
**Description:** Set list contents directly.  
**Syntax:** `Lists.Set(name, item1, item2, ...)`  
**Parameters:**
- `name` - List name
- `items...` - Items to set

**Examples:**
```ictl
Lists.Set(MyList, 10, 20, 30)
```

---

## Kachua (Turtle Graphics) Commands

### Kachua.Forward()
**Description:** Move turtle forward by specified distance.  
**Syntax:** `Kachua.Forward(distance)`  
**Parameters:**
- `distance` - Distance in pixels

**Examples:**
```ictl
Kachua.Forward(100)
Kachua.Forward(Variables.StepSize)
```

---

### Kachua.Backward()
**Description:** Move turtle backward by specified distance.  
**Syntax:** `Kachua.Backward(distance)`  
**Parameters:**
- `distance` - Distance in pixels

**Examples:**
```ictl
Kachua.Backward(50)
```

---

### Kachua.Right()
**Description:** Turn turtle right by specified angle.  
**Syntax:** `Kachua.Right(angle)`  
**Parameters:**
- `angle` - Angle in degrees

**Examples:**
```ictl
Kachua.Right(90)    # 90-degree right turn
```

---

### Kachua.Left()
**Description:** Turn turtle left by specified angle.  
**Syntax:** `Kachua.Left(angle)`  
**Parameters:**
- `angle` - Angle in degrees

**Examples:**
```ictl
Kachua.Left(45)     # 45-degree left turn
```

---

### Kachua.PenUp()
**Description:** Lift the pen (don't draw).  
**Syntax:** `Kachua.PenUp()`  
**Parameters:** None

**Examples:**
```ictl
Kachua.PenUp()
Kachua.Forward(100)  # Moves without drawing
```

---

### Kachua.PenDown()
**Description:** Put the pen down (start drawing).  
**Syntax:** `Kachua.PenDown()`  
**Parameters:** None

**Examples:**
```ictl
Kachua.PenDown()
Kachua.Forward(100)  # Draws a line
```

---

### Kachua.SetColor()
**Description:** Set the pen color.  
**Syntax:** `Kachua.SetColor(color)`  
**Parameters:**
- `color` - Color name (e.g., "red", "blue", "green")

**Examples:**
```ictl
Kachua.SetColor("red")
Kachua.Forward(100)
```

---

### Kachua.SetPenWidth()
**Description:** Set the pen line width/thickness.  
**Syntax:** `Kachua.SetPenWidth(width)`  
**Parameters:**
- `width` - Width in pixels

**Examples:**
```ictl
Kachua.SetPenWidth(3)
Kachua.Forward(100)
```

---

### Kachua.SetSpeed()
**Description:** Set drawing speed (0=fastest, higher=slower).  
**Syntax:** `Kachua.SetSpeed(speed)`  
**Parameters:**
- `speed` - Speed value (0-10)

**Examples:**
```ictl
Kachua.SetSpeed(1)   # Slow
Kachua.SetSpeed(5)   # Medium
Kachua.SetSpeed(10)  # Fast
```

---

### Kachua.GoTo()
**Description:** Move turtle to absolute position.  
**Syntax:** `Kachua.GoTo(x, y)`  
**Parameters:**
- `x` - X coordinate
- `y` - Y coordinate

**Examples:**
```ictl
Kachua.GoTo(0, 0)      # Center
Kachua.GoTo(100, 150)
```

---

### Kachua.Home()
**Description:** Move turtle back to home position (0, 0).  
**Syntax:** `Kachua.Home()`  
**Parameters:** None

**Examples:**
```ictl
Kachua.Home()
```

---

### Kachua.Clear()
**Description:** Clear all drawings from the screen.  
**Syntax:** `Kachua.Clear()`  
**Parameters:** None

**Examples:**
```ictl
Kachua.Clear()
```

---

### Kachua.Reset()
**Description:** Reset turtle to default state.  
**Syntax:** `Kachua.Reset()`  
**Parameters:** None

**Examples:**
```ictl
Kachua.Reset()
```

---

### Kachua.Show()
**Description:** Display the graphics window.  
**Syntax:** `Kachua.Show()`  
**Parameters:** None

**Examples:**
```ictl
Kachua.Show()
```

---

### Kachua.Hide()
**Description:** Hide the turtle cursor.  
**Syntax:** `Kachua.Hide()`  
**Parameters:** None

**Examples:**
```ictl
Kachua.Hide()
```

---

### Kachua.Stamp()
**Description:** Stamp a copy of the turtle at current position.  
**Syntax:** `Kachua.Stamp()`  
**Parameters:** None

**Return:** Stamp ID

**Examples:**
```ictl
Kachua.Stamp()
```

---

### Kachua.FillStart()
**Description:** Begin a fill region.  
**Syntax:** `Kachua.FillStart()`  
**Parameters:** None

**Examples:**
```ictl
Kachua.FillStart()
Kachua.Forward(100)
Kachua.Right(90)
Kachua.Forward(100)
Kachua.Right(90)
Kachua.Forward(100)
Kachua.Right(90)
Kachua.Forward(100)
Kachua.FillEnd()
```

---

### Kachua.FillEnd()
**Description:** End and fill the current region.  
**Syntax:** `Kachua.FillEnd()`  
**Parameters:** None

**Examples:**
```ictl
Kachua.FillStart()
# Draw shape
Kachua.FillEnd()
```

---

### Kachua.Circle()
**Description:** Draw a circle with given radius.  
**Syntax:** `Kachua.Circle(radius)`  
**Parameters:**
- `radius` - Circle radius in pixels

**Examples:**
```ictl
Kachua.Circle(50)
Kachua.Circle(100)
```

---

### Kachua.Heading()
**Description:** Get current heading direction.  
**Syntax:** `Kachua.Heading()`  
**Parameters:** None

**Return:** Angle in degrees

**Examples:**
```ictl
Variables.Direction = Kachua.Heading()
Terminal.Echo(Kachua.Heading())
```

---

### Kachua.SetHeading()
**Description:** Set heading direction.  
**Syntax:** `Kachua.SetHeading(angle)`  
**Parameters:**
- `angle` - Angle in degrees

**Examples:**
```ictl
Kachua.SetHeading(0)    # East
Kachua.SetHeading(90)   # North
Kachua.SetHeading(180)  # West
Kachua.SetHeading(270)  # South
```

---

## GUI Commands

### GUI.MessageBox()
**Description:** Display a simple message box.  
**Syntax:** `GUI.MessageBox(title, message)`  
**Parameters:**
- `title` - Window title
- `message` - Message text

**Examples:**
```ictl
GUI.MessageBox("Hello", "This is a message")
GUI.MessageBox("Welcome", "Program started")
```

---

### GUI.NewDialogBox()
**Description:** Display a dialog box.  
**Syntax:** `GUI.NewDialogBox(title, message)`  
**Parameters:**
- `title` - Window title
- `message` - Message text

**Examples:**
```ictl
GUI.NewDialogBox("Confirm", "Do you want to continue?")
```

---

### GUI.InputBox()
**Description:** Get user text input in a dialog.  
**Syntax:** `GUI.InputBox(prompt)`  
**Parameters:**
- `prompt` - Prompt text

**Return:** User input text

**Examples:**
```ictl
Variables.Name = GUI.InputBox("Enter your name: ")
```

---

### GUI.ChoiceBox()
**Description:** Display dialog with multiple choice options.  
**Syntax:** `GUI.ChoiceBox(title, message, option1, option2, ...)`  
**Parameters:**
- `title` - Window title
- `message` - Message text
- `options...` - Choice options

**Return:** Selected option

**Examples:**
```ictl
Variables.Choice = GUI.ChoiceBox("Select", "Pick one:", "Option A", "Option B", "Option C")
```

---

### GUI.Window()
**Description:** Create a new GUI window.  
**Syntax:** `GUI.Window(title, width, height)`  
**Parameters:**
- `title` - Window title
- `width` - Width in pixels
- `height` - Height in pixels

**Examples:**
```ictl
GUI.Window("My App", 600, 400)
```

---

### GUI.Button()
**Description:** Add a button to the window.  
**Syntax:** `GUI.Button(label, kheer_name)`  
**Parameters:**
- `label` - Button text
- `kheer_name` - Function to call when clicked

**Examples:**
```ictl
GUI.Button("Click Me", "OnButtonClick")
Program.Kheer(OnButtonClick) {
    Terminal.Echo("Button clicked!")
}
```

---

### GUI.Label()
**Description:** Add a text label to the window.  
**Syntax:** `GUI.Label(text)`  
**Parameters:**
- `text` - Label text

**Examples:**
```ictl
GUI.Label("Enter your name:")
```

---

### GUI.Image()
**Description:** Display an image in the window.  
**Syntax:** `GUI.Image(url_or_path)`  
**Parameters:**
- `url_or_path` - Image URL or file path

**Examples:**
```ictl
GUI.Image("https://example.com/image.png")
GUI.Image("C:/images/photo.jpg")
```

---

### GUI.ShowWindow()
**Description:** Display the GUI window and run event loop.  
**Syntax:** `GUI.ShowWindow()`  
**Parameters:** None

**Examples:**
```ictl
GUI.Window("My App", 600, 400)
GUI.Label("Hello!")
GUI.ShowWindow()
```

---

### GUI.Spacing()
**Description:** Add vertical spacing to the window.  
**Syntax:** `GUI.Spacing(height)`  
**Parameters:**
- `height` - Height in pixels (default: 10)

**Examples:**
```ictl
GUI.Spacing(20)
```

---

### GUI.Separator()
**Description:** Add a visual separator line.  
**Syntax:** `GUI.Separator()`  
**Parameters:** None

**Examples:**
```ictl
GUI.Separator()
```

---

### GUI.SetTheme()
**Description:** Set application theme.  
**Syntax:** `GUI.SetTheme(theme)`  
**Parameters:**
- `theme` - "Dark" or "Light"

**Examples:**
```ictl
GUI.SetTheme("Dark")
```

---

### GUI.TextField()
**Description:** Add a text input field to the window.  
**Syntax:** `GUI.TextField(placeholder, label)`  
**Parameters:**
- `placeholder` - Placeholder text
- `label` - Field label

**Return:** Field ID for retrieval

**Examples:**
```ictl
Variables.FieldID = GUI.TextField("Type here", "Name:")
```

---

### GUI.GetTextField()
**Description:** Get text from a text field.  
**Syntax:** `GUI.GetTextField(field_id)`  
**Parameters:**
- `field_id` - ID from TextField()

**Return:** Text content

**Examples:**
```ictl
Variables.Text = GUI.GetTextField(Variables.FieldID)
```

---

### GUI.ColorPicker()
**Description:** Show color picker dialog.  
**Syntax:** `GUI.ColorPicker()`  
**Parameters:** None

**Return:** Selected color (hex code)

**Examples:**
```ictl
Variables.Color = GUI.ColorPicker()
```

---

### GUI.ColorPalette()
**Description:** Show custom color palette.  
**Syntax:** `GUI.ColorPalette(color1, color2, ...)`  
**Parameters:**
- `colors...` - Color options

**Return:** Selected color

**Examples:**
```ictl
Variables.Color = GUI.ColorPalette("Red", "Green", "Blue", "Yellow")
```

---

### GUI.DatePicker()
**Description:** Show calendar date picker.  
**Syntax:** `GUI.DatePicker(label)`  
**Parameters:**
- `label` - Dialog label

**Return:** Selected date

**Examples:**
```ictl
Variables.Date = GUI.DatePicker("Select a date:")
```

---

### GUI.ColorMap()
**Description:** Display comprehensive color map.  
**Syntax:** `GUI.ColorMap()`  
**Parameters:** None

**Return:** Selected color (hex code)

**Examples:**
```ictl
Variables.SelectedColor = GUI.ColorMap()
```

---

### GUI.InfoDialog()
**Description:** Display information dialog.  
**Syntax:** `GUI.InfoDialog(title, message)`  
**Parameters:**
- `title` - Dialog title
- `message` - Info message

**Examples:**
```ictl
GUI.InfoDialog("Info", "Operation completed successfully")
```

---

### GUI.WarningDialog()
**Description:** Display warning dialog.  
**Syntax:** `GUI.WarningDialog(title, message)`  
**Parameters:**
- `title` - Dialog title
- `message` - Warning message

**Examples:**
```ictl
GUI.WarningDialog("Warning", "This action cannot be undone")
```

---

### GUI.ErrorDialog()
**Description:** Display error dialog.  
**Syntax:** `GUI.ErrorDialog(title, message)`  
**Parameters:**
- `title` - Dialog title
- `message` - Error message

**Examples:**
```ictl
GUI.ErrorDialog("Error", "File not found")
```

---

### GUI.ConfirmDialog()
**Description:** Display Yes/No confirmation dialog.  
**Syntax:** `GUI.ConfirmDialog(title, message)`  
**Parameters:**
- `title` - Dialog title
- `message` - Confirmation message

**Return:** "Yes" or "No"

**Examples:**
```ictl
Variables.Answer = GUI.ConfirmDialog("Confirm", "Continue?")
```

---

### GUI.FileOpenDialog()
**Description:** File open dialog.  
**Syntax:** `GUI.FileOpenDialog(title, filter)`  
**Parameters:**
- `title` - Dialog title
- `filter` - File filter (e.g., "*.txt")

**Return:** File path

**Examples:**
```ictl
Variables.FilePath = GUI.FileOpenDialog("Open File", "All Files (*)")
```

---

### GUI.FileSaveDialog()
**Description:** File save dialog.  
**Syntax:** `GUI.FileSaveDialog(title, filter)`  
**Parameters:**
- `title` - Dialog title
- `filter` - File filter

**Return:** File path

**Examples:**
```ictl
Variables.SavePath = GUI.FileSaveDialog("Save File", "*.txt")
```

---

### GUI.FolderDialog()
**Description:** Folder selection dialog.  
**Syntax:** `GUI.FolderDialog(title)`  
**Parameters:**
- `title` - Dialog title

**Return:** Folder path

**Examples:**
```ictl
Variables.Folder = GUI.FolderDialog("Select Folder")
```

---

### GUI.InputDialog()
**Description:** Simple text input dialog.  
**Syntax:** `GUI.InputDialog(title, message, default)`  
**Parameters:**
- `title` - Dialog title
- `message` - Prompt message
- `default` - Default value

**Return:** User input

**Examples:**
```ictl
Variables.Input = GUI.InputDialog("Name", "Enter your name:", "John")
```

---

### GUI.MultiChoiceDialog()
**Description:** Multiple choice selection dialog.  
**Syntax:** `GUI.MultiChoiceDialog(title, message, choice1, choice2, ...)`  
**Parameters:**
- `title` - Dialog title
- `message` - Message
- `choices...` - Available choices

**Return:** List of selected choices

**Examples:**
```ictl
Variables.Choices = GUI.MultiChoiceDialog("Select Items", "Pick multiple:", "Item1", "Item2", "Item3")
```

---

### GUI.NumberDialog()
**Description:** Numeric input dialog with up/down spinner.  
**Syntax:** `GUI.NumberDialog(title, message, default, min, max)`  
**Parameters:**
- `title` - Dialog title
- `message` - Prompt message
- `default` - Default value
- `min` - Minimum value
- `max` - Maximum value

**Return:** Selected number

**Examples:**
```ictl
Variables.Age = GUI.NumberDialog("Age", "Enter your age:", 20, 1, 120)
```

---

### GUI.OkCancelDialog()
**Description:** OK/Cancel confirmation dialog.  
**Syntax:** `GUI.OkCancelDialog(title, message)`  
**Parameters:**
- `title` - Dialog title
- `message` - Message

**Return:** "OK" or "Cancel"

**Examples:**
```ictl
Variables.Result = GUI.OkCancelDialog("Confirm", "Are you sure?")
```

---

## Program Block Structures

### Program.Main
**Description:** Main program entry point.  
**Syntax:**
```ictl
Program.Main {
    # Code here runs when program starts
}
```

**Examples:**
```ictl
Program.Main {
    Terminal.Echo("Program started!")
    Variables.X = 42
    Terminal.Echo(Variables.X)
}
```

---

### Program.If
**Description:** Conditional block (if condition is true).  
**Syntax:**
```ictl
Program.If(condition) {
    # Code runs if condition is true
}
```

**Examples:**
```ictl
Program.If(Math.Compare(Variables.X, ">", 10)) {
    Terminal.Echo("X is greater than 10")
}

Program.If(Data.Compare(Variables.Name, "Alice")) {
    Terminal.Echo("Hello Alice!")
}
```

---

### Program.Else
**Description:** Else block (runs if preceding If is false).  
**Syntax:**
```ictl
Program.If(condition) {
    # Code if true
}
Program.Else {
    # Code if false
}
```

**Examples:**
```ictl
Program.If(Math.Compare(Variables.Age, ">=", 18)) {
    Terminal.Echo("Adult")
}
Program.Else {
    Terminal.Echo("Minor")
}
```

---

### Program.Loop
**Description:** Repeat a block N times.  
**Syntax:**
```ictl
Program.Loop(count) {
    # Code repeats 'count' times
}
```

**Examples:**
```ictl
Program.Loop(5) {
    Terminal.Echo("Hello!")
}

Program.Loop(Variables.Iterations) {
    Variables.X = Math.Random(1, 100)
    Terminal.Echo(Variables.X)
}
```

---

### Program.ForeverLoop
**Description:** Infinite loop (use Break to exit).  
**Syntax:**
```ictl
Program.ForeverLoop {
    # Code repeats infinitely until BreakLoop
}
```

**Examples:**
```ictl
Program.ForeverLoop {
    Variables.Input = Terminal.Ask("Enter 'quit' to exit: ")
    Program.If(Data.Compare(Variables.Input, "quit")) {
        Program.BreakLoop
    }
}
```

---

### Program.BreakLoop
**Description:** Exit/break out of current loop.  
**Syntax:** `Program.BreakLoop`  
**Parameters:** None

**Examples:**
```ictl
Program.Loop(100) {
    Program.If(Math.Compare(Variables.Counter, "==", 50)) {
        Program.BreakLoop
    }
}
```

---

### Program.Continue
**Description:** Skip to next loop iteration.  
**Syntax:** `Program.Continue`  
**Parameters:** None

**Examples:**
```ictl
Program.Loop(10) {
    Program.If(Math.Compare(Variables.Counter, "==", 5)) {
        Program.Continue
    }
    Terminal.Echo(Variables.Counter)
}
```

---

### Program.Kheer
**Description:** Define a reusable function (like procedures/scripts).  
**Syntax:**
```ictl
Program.Kheer(function_name) {
    # Function code
}
```

**Examples:**
```ictl
Program.Kheer(Greet) {
    Terminal.Echo("Hello!")
}

Program.Kheer(SquareNumber) {
    Variables.Result = Math.Eval(Variables.Input ^ 2)
    Terminal.Echo(Variables.Result)
}
```

---

### Program.ExecuteKheer
**Description:** Call/execute a defined Kheer function.  
**Syntax:** `Program.ExecuteKheer(function_name)`  
**Parameters:**
- `function_name` - Name of Kheer function to execute

**Examples:**
```ictl
Program.ExecuteKheer(Greet)

Program.Kheer(MyFunction) {
    Terminal.Echo("Function executed!")
}
Program.ExecuteKheer(MyFunction)
```

---

## Program Expression Commands

### Program.Not()
**Description:** Logical NOT - negate a boolean condition.  
**Syntax:** `Program.Not(condition)`  
**Parameters:**
- `condition` - Boolean expression

**Return:** Opposite boolean value

**Examples:**
```ictl
Program.If(Program.Not(Math.Compare(Variables.X, ">", 10))) {
    Terminal.Echo("X is not greater than 10")
}

Variables.IsTrue = Program.Not(False)  # True
```

---

# Command Usage Patterns

## Pattern: Variable Operations
```ictl
Variables.X = 42
Variables.Y = Variables.X + 10
Terminal.Echo(Variables.Y)
```

## Pattern: Lists
```ictl
Lists.Numbers = [1, 2, 3, 4, 5]
Program.Loop(Lists.Length(Numbers)) {
    Terminal.Echo(Lists.Get(Numbers, Variables.Index))
}
```

## Pattern: Conditional Logic
```ictl
Program.If(Math.Compare(Variables.X, ">", 10)) {
    Terminal.Echo("Greater")
}
Program.Else {
    Terminal.Echo("Less or equal")
}
```

## Pattern: Loop with Break
```ictl
Variables.Counter = 0
Program.ForeverLoop {
    Variables.Counter = Math.Eval(Variables.Counter + 1)
    Program.If(Math.Compare(Variables.Counter, "==", 10)) {
        Program.BreakLoop
    }
    Terminal.Echo(Variables.Counter)
}
```

## Pattern: Functions (Kheer)
```ictl
Program.Kheer(PrintDouble) {
    Variables.Result = Math.Eval(Variables.Input * 2)
    Terminal.Echo(Variables.Result)
}

Variables.Input = 5
Program.ExecuteKheer(PrintDouble)
```

---

# Quick Reference Table

| Category | Command | Syntax |
|----------|---------|--------|
| Terminal | Echo | Terminal.Echo(value) |
| Terminal | Ask | Terminal.Ask(prompt) |
| Terminal | Clear | Terminal.Clear() |
| Terminal | Style | Terminal.Style(color) |
| Variables | Assign | Variables.name = value |
| Variables | Access | Variables.name |
| Data | Compare | Data.Compare(a, b) |
| Data | LooseCompare | Data.LooseCompare(a, b) |
| Data | ToInt | Data.ToInt(value) |
| Data | ToFloat | Data.ToFloat(value) |
| Data | ToString | Data.ToString(value) |
| Data | TypeOf | Data.TypeOf(value) |
| Math | Eval | Math.Eval(expr) |
| Math | Compare | Math.Compare(a, op, b) |
| Math | Random | Math.Random(min, max) |
| Math | NumPy | Math.NumPy(expr) |
| Math | SymPy | Math.SymPy(expr) |
| Time | Current | Time.Current(format) |
| Time | Wait | Time.Wait(seconds) |
| Lists | Create | Lists.Create(name) |
| Lists | Get | Lists.Get(name, index) |
| Lists | Push | Lists.Push(name, item) |
| Lists | Pop | Lists.Pop(name) |
| Lists | Length | Lists.Length(name) |
| Lists | Clear | Lists.Clear(name) |
| Lists | Contains | Lists.Contains(name, item) |
| Kachua | Forward | Kachua.Forward(distance) |
| Kachua | Backward | Kachua.Backward(distance) |
| Kachua | Right | Kachua.Right(angle) |
| Kachua | Left | Kachua.Left(angle) |
| Kachua | SetColor | Kachua.SetColor(color) |
| Kachua | GoTo | Kachua.GoTo(x, y) |
| Kachua | Circle | Kachua.Circle(radius) |
| GUI | MessageBox | GUI.MessageBox(title, msg) |
| GUI | Window | GUI.Window(title, w, h) |
| GUI | Label | GUI.Label(text) |
| GUI | Button | GUI.Button(label, func) |
| GUI | ShowWindow | GUI.ShowWindow() |
| Program | Main | Program.Main { ... } |
| Program | If | Program.If(cond) { ... } |
| Program | Else | Program.Else { ... } |
| Program | Loop | Program.Loop(count) { ... } |
| Program | ForeverLoop | Program.ForeverLoop { ... } |
| Program | BreakLoop | Program.BreakLoop |
| Program | Continue | Program.Continue |
| Program | Kheer | Program.Kheer(name) { ... } |
| Program | ExecuteKheer | Program.ExecuteKheer(name) |
| Program | Not | Program.Not(condition) |

---

**End of Command Reference**  
*For latest updates and examples, visit the ICTL documentation.*
