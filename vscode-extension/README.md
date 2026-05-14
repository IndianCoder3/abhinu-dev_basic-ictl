# Abhinu.Dev Basic ICTL Language Support for VS Code

This VS Code extension provides comprehensive language support for the Abhinu.Dev Basic ICTL programming language, including **IntelliSense**, **syntax highlighting**, **intelligent code completion**, **hover documentation**, and **integrated file execution**.

## Features

### ✨ Core Features
- **Syntax Highlighting**: Proper highlighting for all ICTL language constructs
- **IntelliSense with Hover Documentation**: Hover over commands to see their documentation
- **Intelligent Code Completion**: Context-aware autocomplete for all 60+ commands
- **F5 Run Button**: Execute ICTL files directly from the editor (like Python extension)
- **ICTL Path Configuration**: Automatically configure your ICTL installation directory
- **Integrated Terminal**: Run output appears in a dedicated ICTL terminal
- **Keyboard Shortcuts**: F5 to run, Ctrl+Shift+P for command palette access

### 🎨 Language Support
- **Terminal I/O**: Echo, Ask, Clear, Style commands
- **Variables**: Simple variable creation and assignment
- **Data Types**: Strings, numbers, floats, booleans, lists
- **Lists & Arrays**: Create, access, modify lists with push/pop/get operations
- **Math Operations**: Eval, Compare, Random, SymPy, NumPy
- **Control Flow**: If/Else, Loops, Break, Continue
- **Time & Date**: Get current time, pause execution
- **Kachua (Turtle Graphics)**: Full graphics support with shapes, colors, and positioning
- **GUI Commands**: Create windows, buttons, dialogs, and more
- **Comments**: Full line and block comment support

## Installation

### Option 1: Install from VS Code Extension Marketplace (Easiest)

1. Open VS Code and open the Extensions Panel (`Ctrl+Shift+X`)
2. Search for `Abhinu.Dev Basic ICTL Language`
3. Click Install

### Option 2: Install from VSIX

1. Download the `.vsix` file from the [GitHub repository](https://github.com/indiancoder3/abhinu-dev_basic-ictl)
2. In VS Code, open the Command Palette (`Ctrl+Shift+P`)
3. Run `Extensions: Install from VSIX...`
4. Select the downloaded `.vsix` file

### Option 3: Manual Installation

1. Copy the extension folder to your VS Code extensions directory:
   - **Windows**: `%USERPROFILE%\.vscode\extensions\ictl-language-1.2.0\`
   - **macOS**: `~/.vscode/extensions/ictl-language-1.2.0/`
   - **Linux**: `~/.vscode/extensions/ictl-language-1.2.0/`

2. Restart VS Code

## Quick Start

### 1. Configure ICTL Installation Path

When you first run an ICTL file, VS Code will prompt you to select your ICTL installation directory (where `ictl.exe` or `ictl` executable is located).

Alternatively, use the command palette:
- Press `Ctrl+Shift+P`
- Type "Configure ICTL" 
- Select the ICTL installation folder

### 2. Create an ICTL File

Create a new file with `.ictl` extension:

```ictl
Program.Main {
    Terminal.Echo("Hello, World!")
}
```

### 3. Run Your Program

- Press **F5** to run the current file
- Or use `Ctrl+Shift+F5` as an alternative
- Or use the **Run** button in the editor's title bar
- Or right-click and select "Run ICTL File"

Output will appear in the ICTL terminal at the bottom of VS Code.

## Usage & Features

### IntelliSense & Hover Documentation

Hover your mouse over any ICTL command to see its documentation:

```ictl
Terminal.Echo("test")  ← Hover over "Echo" to see documentation
```

This works for all 60+ ICTL commands including:
- Terminal commands (Echo, Ask, Style, Clear)
- Math operations (Eval, Compare, Random, SymPy, NumPy)
- List operations (Get, Push, Pop, Create, Clear, etc.)
- Data conversions (ToInt, ToFloat, ToString, TypeOf)
- Kachua graphics (Forward, Left, SetColor, etc.)
- GUI commands (MessageBox, InputBox, Window, etc.)

### Code Completion

Start typing any command prefix and get intelligent suggestions:

```ictl
Terminal.    ← Press . to see all Terminal commands (Echo, Ask, Clear, Style)
Math.        ← Math operations (Eval, Compare, Random, SymPy, NumPy)
Program.     ← Program blocks (Main, If, Else, Loop, ForeverLoop, etc.)
Lists.       ← List operations (Get, Push, Pop, Create, Clear, Delete, etc.)
Variables.   ← Variable operations
Kachua.      ← Graphics commands
GUI.         ← GUI commands
```

### Syntax Highlighting

All ICTL keywords are properly highlighted for easy reading:

```ictl
Program.Main {                    # Keywords highlighted
    Variables.Name = "Alice"      # Strings in color
    Terminal.Echo(Variables.Name) # Commands with color
    
    Program.If(Math.Compare(42, ">", 0)) {
        Terminal.Echo("Success!")
    }
}
```

## Configuration

Access ICTL settings via `File → Preferences → Settings` (or `Ctrl+,`):

```json
{
    "ictl.installationPath": "/path/to/ictl",
    "ictl.showRunButton": true,
    "ictl.terminalWidth": 80
}
```

### Available Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `ictl.installationPath` | string | (empty) | Path to ICTL installation directory |
| `ictl.showRunButton` | boolean | `true` | Show run button in editor title |
| `ictl.terminalWidth` | number | `80` | Terminal output width |

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| **F5** | Run current ICTL file |
| **Ctrl+Shift+F5** | Run current ICTL file (alternative) |
| **Ctrl+Shift+P** | Open command palette (find ICTL commands) |
| **Ctrl+/** | Toggle line comments |
| **Ctrl+H** | Find and replace |

## Command Palette Commands

Press `Ctrl+Shift+P` to open the command palette and search for:

- **ICTL: Run** - Run the current ICTL file
- **ICTL: Configure ICTL Installation Path** - Set up your ICTL installation directory

## Example Programs

### Hello World
```ictl
Program.Main {
    Terminal.Echo("Hello, World!")
}
```

### User Input
```ictl
Program.Main {
    Variables.Name = Terminal.Ask("What is your name? ")
    Terminal.Echo("Nice to meet you, " + Variables.Name)
}
```

### Simple Calculator
```ictl
Program.Main {
    Variables.A = Data.ToInt(Terminal.Ask("Enter first number: "))
    Variables.B = Data.ToInt(Terminal.Ask("Enter second number: "))
    
    Variables.Sum = Math.Eval(Variables.A + Variables.B)
    Terminal.Echo("Sum: " + Variables.Sum)
}
```

### Drawing with Graphics
```ictl
Program.Main {
    Kachua.SetColor("red")
    Kachua.SetPenWidth(3)
    
    Program.Loop(4) {
        Kachua.Forward(100)
        Kachua.Right(90)
    }
    
    Kachua.Show()
}
```

### List Operations
```ictl
Program.Main {
    Lists.Numbers = [1, 2, 3, 4, 5]
    
    Terminal.Echo("First number: " + Lists.Get(Numbers, 0))
    Lists.Push(Numbers, 6)
    Terminal.Echo("List length: " + Lists.Length(Numbers))
}
```

## Troubleshooting

### "ICTL installation path not found"
- Make sure you have ICTL installed on your system
- Use `ICTL: Configure ICTL Installation Path` command to set the correct path
- The path should point to the directory containing the `ictl` executable

### "Language not recognized"
- Make sure your file has `.ictl` extension
- Restart VS Code if needed

### No autocomplete suggestions
- Make sure you have the extension properly installed
- Try reloading the window (Ctrl+R)
- Check that you're using the correct command syntax

### Terminal not appearing
- Check the bottom of VS Code - the ICTL terminal should appear automatically
- If it's closed, use View → Terminal or Ctrl+` to reopen it

## Support & Documentation

- 📖 **Full Documentation**: [ICTL README](https://github.com/indiancoder3/abhinu-dev_basic-ictl)
- 🐛 **Report Bugs**: [GitHub Issues](https://github.com/indiancoder3/abhinu-dev_basic-ictl/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/indiancoder3/abhinu-dev_basic-ictl/discussions)
- 🌐 **Web Editor**: [Try ICTL Online](https://indiancoder3.github.io/abhinu-dev_basic-ictl/editor)

## License

This extension is licensed under the [GNU General Public License v3.0](LICENSE)

---

**Happy Coding! Everyone Can Code!**
```

### Math & Logic
```ictl
Math.Eval(2 + 3 * 4)                    # Arithmetic
Math.Compare(10, ">", 5)                # Comparisons
Math.Random(1, 100)                     # Random numbers
Data.Compare("hello", "hello")          # String comparison
```

### Data Conversions
```ictl
Data.ToInt("42")                # String to integer
Data.ToFloat("3.14")            # String to float
Data.ToString(42)               # Number to string
```

### Time & Date
```ictl
Time.Current("hh:mm tt")        # Get current time
Time.Wait(1000)                 # Pause (milliseconds)
```

### Control Flow
```ictl
Program.If(condition) { ... }       # Conditional execution
Program.Else { ... }                # Else block
Program.Loop(5) { ... }             # Repeat 5 times
Program.ForeverLoop { ... }         # Infinite loop
Program.Not(condition)              # Logical NOT
Program.BreakLoop                   # Exit loop
Program.Continue                    # Next iteration
```

### Custom Functions (Kheers)
```ictl
# Define a custom function
Program.Kheer(greet) {
    Terminal.Echo("Hello!")
}

# Execute the custom function
Program.ExecuteKheer("greet")
```

### Kachua - Turtle Graphics
```ictl
# Create drawings with turtle graphics
Kachua.Forward(100)              # Move forward
Kachua.Backward(50)              # Move backward
Kachua.Right(90)                 # Turn right
Kachua.Left(45)                  # Turn left

Kachua.PenUp()                   # Stop drawing
Kachua.PenDown()                 # Start drawing
Kachua.SetColor("red")           # Set pen color
Kachua.SetPenWidth(3)            # Set pen thickness

Kachua.Circle(50)                # Draw circle
Kachua.GoTo(0, 0)                # Move to position
Kachua.Home()                     # Return to origin

Kachua.FillStart()               # Begin fill region
# ... draw shape ...
Kachua.FillEnd()                 # End fill region

Kachua.Clear()                   # Clear all drawings
Kachua.Show()                     # Display graphics
Kachua.Hide()                     # Hide turtle cursor
```

## Complete Examples

### Example 1: Basic Program with Variables and Lists

```ictl
Program.Main {
    # Variables and input
    Variables.Name = Terminal.Ask("What's your name? ")
    Variables.Age = Terminal.Ask("What's your age? ")
    
    # Mathematical operations
    Variables.NextAge = Math.Eval(Variables.Age + 1)
    
    # Lists
    Lists.Hobbies = ["reading", "gaming", "coding"]
    
    # Output
    Terminal.Echo("Hello, " + Variables.Name + "!")
    Terminal.Echo("Your hobbies: " + Lists.Get(Hobbies, 0))
    
    # Conditionals
    Program.If(Math.Compare(Variables.Age, ">=", 18)) {
        Terminal.Echo("You are an adult!")
    }
    Program.Else {
        Terminal.Echo("You are a minor")
    }
    
    # Loops
    Program.Loop(3) {
        Terminal.Echo("Let's go!")
    }
}
```

### Example 2: Drawing with Kachua (Turtle Graphics)

```ictl
Program.Main {
    Terminal.Echo("Drawing a square...")
    
    Program.Loop(4) {
        Kachua.Forward(100)
        Kachua.Right(90)
    }
    
    Terminal.Echo("Square drawn! Press window close to exit.")
    Kachua.Show()
}
```

### Example 3: Using Custom Functions (Kheers)

```ictl
Program.Kheer(drawSquare) {
    Program.Loop(4) {
        Kachua.Forward(100)
        Kachua.Right(90)
    }
}

Program.Kheer(drawTriangle) {
    Program.Loop(3) {
        Kachua.Forward(100)
        Kachua.Right(120)
    }
}

Program.Main {
    Kachua.SetColor("blue")
    Program.ExecuteKheer("drawSquare")
    
    Kachua.GoTo(0, -150)
    Kachua.SetColor("red")
    Program.ExecuteKheer("drawTriangle")
    
    Kachua.Show()
}
```

## Keyboard Shortcuts

- **Ctrl+Space** - Trigger IntelliSense
- **Ctrl+Shift+L** - Select all occurrences
- **F1** - Open Help
- **Ctrl+/** - Toggle line comment

## Settings

The extension respects VS Code's default formatting and indentation settings:

```json
{
    "[ictl]": {
        "editor.tabSize": 4,
        "editor.insertSpaces": true,
        "editor.formatOnSave": false
    }
}
```

## Troubleshooting

### Syntax highlighting not working
- Ensure the file has `.ictl` extension
- Reload VS Code window (Ctrl+R)
- Check that the extension is enabled in Extensions panel

### Autocomplete not appearing
- Try pressing `Ctrl+Space` to manually trigger it
- Check that you're typing after a category dot (e.g., `Terminal.`)
- Verify the extension is enabled

### Still having issues?
- Check the [GitHub repository](https://github.com/indiancoder3/abhinu-dev_basic-ictl) for known issues
- Create a new issue with details about your problem

## Contributing

This extension is part of the ICTL interpreter project. Contributions are welcome!

- **Repository**: https://github.com/indiancoder3/abhinu-dev_basic-ictl
- **Issues**: https://github.com/indiancoder3/abhinu-dev_basic-ictl/issues
- **Discussions**: https://github.com/indiancoder3/abhinu-dev_basic-ictl/discussions

## License

GNU General Public License v3.0 (GPL-3.0)

See LICENSE file or https://www.gnu.org/licenses/gpl-3.0.html

## Support

For more information about ICTL and to learn the language:
- Visit: https://abhinu.dev
- Check: The official ICTL documentation
- Try: The online editor at https://abhinu.dev/editor

---

**Made with ❤️ by IndianCoder3**