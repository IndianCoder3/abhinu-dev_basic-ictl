# Abhinu.Dev Basic ICTL Language Support for VS Code

This VS Code extension provides language support for the Abhinu.Dev Basic ICTL programming language, including syntax highlighting, code snippets, and language configuration.

## Features

- **Syntax Highlighting**: Proper highlighting for all ICTL language constructs
- **Code Snippets**: Quick insertion of common ICTL code patterns
- **Language Configuration**: Auto-closing brackets, comments, and proper indentation

## Installation

### Option 1: Install from VS Code Extension Marketplace (easiest)

1. Open VS Code and open the Extensions Panel (`Ctrl+Shift+X`)
2. Search for `Abhinu.Dev Basic ICTL Language`
3. Install it.

### Option 2: Install from VSIX

1. Download the `.vsix` file for this extension from the GitHub repository (github.com/indiancoder3/abhinu-dev_basic-ictl)
2. In VS Code, open the Command Palette (`Ctrl+Shift+P`)
3. Run `Extensions: Install from VSIX...`
4. Select the downloaded `.vsix` file

### Option 3: Manual Installation

1. Copy the extension files to your VS Code extensions directory:
   - Windows: `%USERPROFILE%\.vscode\extensions\ictl-language-support-0.1.0`
   - macOS: `~/.vscode/extensions/ictl-language-support-0.1.0`
   - Linux: `~/.vscode/extensions/ictl-language-support-0.1.0`

2. Reload VS Code

## Usage

Once installed, VS Code will automatically recognize `.ictl` files and provide:

- Syntax highlighting for:
  - Terminal commands (Terminal.Echo, Terminal.Ask, etc.)
  - Variable operations (Variables.New, Variables.X = ...)
  - Math operations (Math.Eval, Math.Compare)
  - Control flow (Program.If, Program.Loop, etc.)
  - Data types (strings, numbers, booleans)
  - Comments (# and //)

- Code snippets accessible via IntelliSense:
  - `main` - Main program block
  - `echo` - Terminal.Echo statement
  - `ask` - Terminal.Ask input
  - `var` - Variable declaration
  - `if` - If statement
  - `loop` - Loop statement
  - And many more...

## Language Features Supported

### Terminal I/O
- `Terminal.Echo(expression)` - Output to console
- `Terminal.Ask(prompt)` - Get user input
- `Terminal.Style(color)` - Set text color/style

### Variables
- `Variables.New(name)` - Declare variable
- `Variables.name = value` - Assign value
- `Variables.name` - Read variable

### Math & Logic
- `Math.Eval(expression)` - Arithmetic evaluation
- `Math.Compare(a, op, b)` - Numeric comparison
- `Data.Compare(a, b)` - Data comparison

### Control Flow
- `Program.If(condition) { ... }` - Conditional execution
- `Program.Loop(count) { ... }` - Counted loop
- `Program.ForeverLoop { ... }` - Infinite loop
- `Program.BreakLoop` - Exit loop
- `Program.Continue` - Skip iteration

### Program Structure
- `Program.Main { ... }` - Main entry point

## Example

```ictl
Program.Main {
    # Declare variables
    Variables.New(Name)
    Variables.New(Age)

    # Get user input
    Variables.Name = Terminal.Ask("What's your name? ")
    Variables.Age = Terminal.Ask("What's your age? ")

    # Process with math
    Variables.New(NextAge)
    Variables.NextAge = Math.Eval(Variables.Age + 1)

    # Output with conditionals
    Terminal.Echo("Hello, " + Variables.Name + "!")

    Program.If(Math.Compare(Variables.Age, ">", 18)) {
        Terminal.Echo("You are an adult!")
    }

    Terminal.Echo("Next year you'll be " + Variables.NextAge)

    # Loops
    Program.Loop(3) {
        Terminal.Echo("Counting!")
    }
}
```

## Contributing

This extension is part of the ICTL interpreter project. For issues or contributions, please visit the main repository.

## License

Same as the ICTL interpreter project.