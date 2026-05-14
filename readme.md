![Python](https://img.shields.io/badge/Python-3.7+-blue)
[![License](https://img.shields.io/badge/License-GPL%20v3-green.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Status](https://img.shields.io/badge/status-in%20development-orange)
![GitHub last commit](https://img.shields.io/github/last-commit/indiancoder3/abhinu-dev_basic-ictl)
![GitHub issues](https://img.shields.io/github/issues/indiancoder3/abhinu-dev_basic-ictl)

<h1 align="center" style="font-family: Comic Sans Ms; color:lightyellow"><b><u>Abhinu.Dev Basic ICTL</u></b></h1>
<p align="center">Everyone Can Code!</p>
<h1 align="center">
  <a href="https://github.com/indiancoder3/abhinu-dev_basic-ictl" target="_blank">
    <img src="ictl_banner.png" alt="Abhinu.Dev Basic ICTL Banner"/>
  </a>
</h1>
<p align="center"><b>A basic programming language made for making the learning journey easy! Each person from age 5 to age 500 should be allowed to code!</b></p>

<p align="center">
    <a href="https://www.python.org">Python (for building the language interpreter)</a> |
    <a href="https://indiancoder3.github.io">IndianCoder3</a> |
    <a href="#command-reference">Command Reference</a> |
    <a href="#building-story">Build Story</a> |
    <a href="https://indiancoder3.github.io/abhinu-dev_basic-ictl/editor">Web Editor</a>
</p>

> [!CAUTION]
> This programming language is **still in development**.
> Some features (such as `Math.Eval()`) **used Python's `eval()` in older versions**, which could **execute arbitrary code**.
>
> ⚠️ **This applies only to ICTL v1.0 and below.**
> Starting from **v1.1.0**, `Math.Eval()` uses a custom math parser instead of `eval()`.

---

## Preface

Nowadays, every kid starts off from **Scratch**, and then are guided to something like **HTML**, or **Python**. While **Scratch** is easy and visual, it mainly teaches flowchart-based logic. **HTML** is for web design. Meanwhile, **Python**, a programming language loved by the world, is actually **powerful** — but it doesn't make the switch easier.

**ICTL** bridges this gap. It offers a **clean, beginner-friendly syntax** that teaches real programming concepts without the overwhelming complexity of Python. Whether you're 5 or 500, ICTL lets you start coding immediately and see results!

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Quick Start](#quick-start)
- [Web Editor](#web-editor)
- [Installation](#installation)
- [Language Basics](#language-basics)
- [Command Reference](#command-reference)
- [VS Code Extension](#vs-code-extension)
- [Examples](#examples)
- [Building from Source](#building-from-source)
- [Building Story](#building-story)
- [Contributing](#contributing)
- [License](#license)

See the [History](HISTORY.md) for full project changes.

---

## About

**Abhinu.Dev Basic ICTL** is a beginner-friendly programming language designed to make the learning journey easy and enjoyable. Whether you're just starting out or teaching others to code, ICTL provides a clean, intuitive syntax that focuses on core programming concepts like variables, loops, conditionals, and basic mathematics.

The language is built on Python and runs as an interpreter, making it easy to execute `.ictl` files directly or use the interactive shell for learning.

### Why ICTL?

- **Simple Syntax**: Clear, readable code that's easy to understand
- **Beginner-Friendly**: Designed specifically for learning programming fundamentals
- **Quick Feedback**: Run code immediately via CLI or interactive mode
- **Educational**: Perfect for teaching programming concepts to students of all ages
- **Active Development**: Regular updates and improvements based on community feedback
- **Community Driven**: Contributions and feedback are welcome!

---

## Features

✨ **Core Language Features:**
- **Variables**: Simple variable declaration and assignment
- **Data Types**: Strings, integers, floats, and booleans
- **Terminal I/O**: Easy input/output operations with styling options
- **Mathematics**: Arithmetic evaluation and numeric comparisons
- **Control Flow**: If/else conditionals with boolean logic
- **Loops**: Counted loops and infinite loops with break/continue support
- **String Operations**: Concatenation and variable interpolation
- **Error Handling**: Clear error messages with line numbers and helpful suggestions
- **Lists**: Dynamic lists with push, pop, and lookup operations
- **Kachua (Turtle Graphics)**: Draw shapes and graphics with turtle commands
- **GUI**: Build simple graphical user interfaces

🛠️ **Developer Tools:**
- **Interactive Shell**: Drop into shell mode for immediate code execution
- **File Execution**: Run `.ictl` script files from command line
- **Syntax Highlighting**: VS Code extension with full language support
- **Code Snippets**: Quick insertion of common patterns
- **Comprehensive Documentation**: Command reference and examples

---

## Quick Start

### 1. Create a Simple Program

Create a file named `hello.ictl`:

```ictl
Program.Main {
    Terminal.Echo("Hello, World!")
}
```

### 2. Run It

**If you installed from Release (Easiest):**
```bash
ictl hello.ictl
# or if using standalone
ICTL-v26.05.01.exe hello.ictl
```

**If you're developing from source:**
```bash
python main.py hello.ictl
```

### 3. Output

```
Hello, World!
```

### Try Interactive Mode

```bash
# From release
ictl

# Or from source
python main.py
```

This drops you into an interactive shell where you can execute ICTL commands line by line.

---

## Web Editor

I've also created a **web editor interface** for testing ICTL without installing it! Simply visit:

🌐 **[https://indiancoder3.github.io/abhinu-dev_basic-ictl/editor](https://indiancoder3.github.io/abhinu-dev_basic-ictl/editor)**

Alternatively: **[https://basic-ictl-web-studio.onrender.com/](https://basic-ictl-web-studio.onrender.com/)**

The web interface features:
- **Monaco Editor** with autocomplete and syntax highlighting
- **Ribbon interface** for easy command access
- **Status bar** showing code information
- **Live execution** results

Perfect for trying ICTL without installation!

---

## Installation

Choose one of the two installation paths below:

### 🚀 Path 1: Recommended - Use Pre-built Release

The easiest way to get started! Each release includes:
- **Cython/Nuitka/PyInstaller Standalone** - Portable executable, no Python required
- **Windows Installer** - System-wide installation for Windows
- **VSIX Extension** - VS Code language support

#### Download from Releases

1. Go to [GitHub Releases](https://github.com/indiancoder3/abhinu-dev_basic-ictl/releases)
2. Download the latest release files for your platform

#### Option A: Standalone Executable (Recommended)

```bash
# Download and run
ICTL.exe your_program.ictl
```

No Python installation required! Portable and ready to use.

#### Option B: System-wide Installation (Windows)

1. Download the Inno Setup installer (e.g., `ICTL-v26.05.01-installer.exe`)
2. Run the installer and follow the prompts
3. ICTL will be added to your system PATH automatically
4. Use `ictl` from any command prompt:

```bash
ictl your_program.ictl
```

#### Option C: Install VS Code Extension

1. Download the `.vsix` file from the release
2. In VS Code, press `Ctrl+Shift+P` and run `Extensions: Install from VSIX...`
3. Select the downloaded VSIX file
4. Enjoy syntax highlighting, autocomplete, and snippets!

---

### 💻 Path 2: Development - From Source Code

For developers who want to modify or contribute to the language.

#### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)
- Git
- Nuitka (optional, for building standalone executables)

#### Installation Steps

1. **Clone the Repository**

```bash
git clone https://github.com/indiancoder3/abhinu-dev_basic-ictl.git
cd abhinu-dev_basic-ictl
```

2. **Navigate to ICTL Directory**

```bash
cd code
```

3. **Install Dependencies**

```bash
pip install -r ../requirements.txt
```

4. **Run Programs**

```bash
# Execute a file
python main.py your_program.ictl

# Or use interactive mode
python main.py
```

5. **Install VS Code Extension (optional)**

See [VS Code Extension](#vs-code-extension) section for setup instructions.

---

## Language Basics

### Variables

Variables store data that you can use throughout your program.

**Assigning a Value:**
```ictl
Variables.Name = "Alice"
Variables.Counter = 42
Variables.Pi = 3.14
```

**Using Variables:**
```ictl
Program.Main {
    Variables.Name = "Alice"
    Terminal.Echo("Hello, " + Variables.Name)
}
```

**Accessing Variables:**
Variables are accessed using `Variables.{name}` syntax:
```ictl
Terminal.Echo(Variables.Name)
Variables.NewValue = Variables.Counter + 10
```

### Data Types

ICTL supports several data types:
- **Strings**: Text in double quotes → `"Hello"`
- **Integers**: Whole numbers → `42`
- **Floats**: Decimal numbers → `3.14`
- **Booleans**: `True` or `False`
- **Lists**: Collections of items → `[1, 2, 3]`

### Lists Commands

Lists allow you to store multiple values in a single variable.

**Creating Lists:**
```ictl
Lists.Numbers = [1, 2, 3, 4, 5]
Lists.Names = ["Alice", "Bob", "Charlie"]
Lists.Create(MyList)
```

**List Operations:**
```ictl
# Get item at index
Variables.First = Lists.Get(Numbers, 0)        # Returns 1

# Add item
Lists.Push(Numbers, 6)

# Remove last item
Variables.Last = Lists.Pop(Numbers)

# Get list length
Variables.Count = Lists.Length(Numbers)

# Check if contains item
Program.If(Lists.Contains(Names, "Alice")) {
    Terminal.Echo("Alice found!")
}

# Clear list
Lists.Clear(Numbers)

# Delete list
Lists.Delete(Numbers)
```

### String Operations

Strings are enclosed in double quotes and can be concatenated with `+`:

```ictl
Program.Main {
    Variables.FirstName = "John"
    Variables.LastName = "Doe"
    
    Terminal.Echo(Variables.FirstName + " " + Variables.LastName)
}
```

### Terminal I/O

**Output (Echo):**
```ictl
Variables.Counter = 67
Terminal.Echo("This is printed to the screen")
Terminal.Echo(Variables.Counter)
```

**Input (Ask):**
```ictl
Program.Main {
    Variables.Name = Terminal.Ask("What is your name? ")
    Terminal.Echo("Nice to meet you, " + Variables.Name)
}
```

**Styling Output:**
```ictl
Terminal.Style("green")
Terminal.Echo("This text is green!")
Terminal.Style("red")
Terminal.Echo("This text is red!")
Terminal.Style("reset")
```

Available styles: `red`, `green`, `blue`, `yellow`, `cyan`, `magenta`, `bold`, `reset`

**Clear Screen:**
```ictl
Terminal.Clear()
```

### Mathematics

**Evaluating Expressions:**
```ictl
Program.Main {
    Variables.Result = Math.Eval(10 + 5)
    Terminal.Echo(Variables.Result)  # Output: 15
    
    Variables.Result = Math.Eval(2 ^ 3)
    Terminal.Echo(Variables.Result)  # Output: 8
}
```

Supported Eval operators: `+`, `-`, `*`, `/`, `^` (power), `()`, `sqrt`, `sin`, `cos`, `tan`, and more.

**Using Python Math Libraries:**
```ictl
Variables.Result = Math.SymPy((2 + 3) * 4)  # Via SymPy
Terminal.Echo(Variables.Result)  # Output: 20

Variables.Result = Math.NumPy(100 / 4)  # Via NumPy
Terminal.Echo(Variables.Result)  # Output: 25.0
```

**Comparing Numbers:**
```ictl
Program.Main {
    Variables.X = 10
    
    Program.If(Math.Compare(Variables.X, ">", 5)) {
        Terminal.Echo("X is greater than 5")
    }
}
```

Operators: `>`, `<`, `>=`, `<=`, `==`, `!=`

**Random Numbers:**
```ictl
Variables.DiceRoll = Math.Random(1, 6)
Terminal.Echo(Variables.DiceRoll)
```

### Conditionals

**If Statement:**
```ictl
Program.Main {
    Variables.Age = 20
    
    Program.If(Math.Compare(Variables.Age, ">=", 18)) {
        Terminal.Echo("You are an adult")
    }
}
```

**If/Else Statement:**
```ictl
Program.Main {
    Variables.Age = Terminal.Ask("How old are you? ")
    
    Program.If(Math.Compare(Variables.Age, ">=", 18)) {
        Terminal.Echo("You are an adult")
    }
    Program.Else {
        Terminal.Echo("You are a kid!")
    }
}
```

**Nested Conditionals:**
```ictl
Program.If(Math.Compare(Variables.Score, ">", 90)) {
    Terminal.Echo("Grade: A")
    
    Program.If(Math.Compare(Variables.Score, "==", 100)) {
        Terminal.Echo("Perfect score!")
    }
}
Program.Else {
    Program.If(Math.Compare(Variables.Score, ">", 80)) {
        Terminal.Echo("Grade: B")
    }
}
```

### Loops

**Counted Loop:**
```ictl
Program.Main {
    Program.Loop(5) {
        Terminal.Echo("This runs 5 times")
    }
}
```

**Infinite Loop with Break:**
```ictl
Program.Main {
    Variables.Counter = 0
    
    Program.ForeverLoop {
        Variables.Counter = Math.Eval(Variables.Counter + 1)
        Terminal.Echo("Count: " + Variables.Counter)
        
        Program.If(Math.Compare(Variables.Counter, ">=", 10)) {
            Program.BreakLoop
        }
    }
}
```

**Continue Statement:**
```ictl
Program.Loop(10) {
    Program.If(Math.Compare(Variables.i, "==", 5)) {
        Program.Continue
    }
    Terminal.Echo(Variables.i)
}
```

### Time Commands

**Get Current Time:**
```ictl
Terminal.Echo(Time.Current("YYYY-MM-DD"))           # 2026-04-07
Terminal.Echo(Time.Current("HH:mm:ss"))             # 14:30:45
Terminal.Echo(Time.Current("MM/DD/YYYY hh:mm tt"))  # 04/07/2026 02:30 PM
```

**Wait/Pause:**
```ictl
Terminal.Echo("Starting...")
Time.Wait(2)
Terminal.Echo("2 seconds later!")
```

### Data Commands

**Type Conversion:**
```ictl
Variables.X = Data.ToInt(3.14)      # Returns 3
Variables.Y = Data.ToFloat("3.14")  # Returns 3.14
Variables.Z = Data.ToString(42)     # Returns "42"
```

**Type Checking:**
```ictl
Terminal.Echo(Data.TypeOf(42))           # "int"
Terminal.Echo(Data.TypeOf("hello"))      # "str"
Terminal.Echo(Data.TypeOf(3.14))         # "float"
Terminal.Echo(Data.TypeOf(True))         # "bool"
```

**Comparisons:**
```ictl
Terminal.Echo(Data.Compare(123, 123))       # True
Terminal.Echo(Data.Compare(123, "123"))     # False (type matters)
Terminal.Echo(Data.LooseCompare(123, "123")) # True (type-insensitive)
```

---

## Command Reference

For a complete command reference with all available commands, see [COMMAND_REFERENCE.md](COMMAND_REFERENCE.md).

### Quick Command Categories

- **Terminal Commands**: `Terminal.Echo()`, `Terminal.Ask()`, `Terminal.Clear()`, `Terminal.Style()`
- **Variables**: `Variables.{name}` assignment and access
- **Lists**: `Lists.Create()`, `Lists.Get()`, `Lists.Push()`, `Lists.Pop()`, etc.
- **Math**: `Math.Eval()`, `Math.Compare()`, `Math.Random()`
- **Data**: `Data.ToInt()`, `Data.ToFloat()`, `Data.ToString()`, `Data.TypeOf()`
- **Time**: `Time.Current()`, `Time.Wait()`
- **Kachua (Graphics)**: `Kachua.Forward()`, `Kachua.Right()`, `Kachua.SetColor()`, etc.
- **GUI**: `GUI.MessageBox()`, `GUI.InputBox()`, `GUI.Window()`, etc.

---

## VS Code Extension

Enhance your coding experience with the official ICTL VS Code extension!

### Features

- 🎨 **Syntax Highlighting** - Color-coded ICTL syntax
- 🤖 **Autocomplete** - Smart suggestions for commands and variables
- ⚡ **Quick Actions** - Run files directly from VS Code
- 📖 **IntelliSense** - Hover help for commands

### Installation

1. Download the `.vsix` file from [Releases](https://github.com/indiancoder3/abhinu-dev_basic-ictl/releases)
2. In VS Code: Press `Ctrl+Shift+P` → `Extensions: Install from VSIX...`
3. Select the downloaded file

---

## Examples

### Example 1: Hello World

```ictl
Program.Main {
    Terminal.Echo("Hello, World!")
}
```

### Example 2: User Input & Variables

```ictl
Program.Main {
    Variables.Name = Terminal.Ask("What is your name? ")
    Variables.Age = Terminal.Ask("How old are you? ")
    
    Terminal.Echo("Hello " + Variables.Name + "!")
    Terminal.Echo("You are " + Variables.Age + " years old.")
}
```

### Example 3: Simple Calculator

```ictl
Program.Main {
    Variables.A = Terminal.Ask("Enter first number: ")
    Variables.B = Terminal.Ask("Enter second number: ")
    
    Variables.Sum = Math.Eval(Variables.A + Variables.B)
    Variables.Product = Math.Eval(Variables.A * Variables.B)
    
    Terminal.Echo("Sum: " + Variables.Sum)
    Terminal.Echo("Product: " + Variables.Product)
}
```

### Example 4: Loops & Conditionals

```ictl
Program.Main {
    Terminal.Echo("Numbers 1 to 10:")
    
    Program.Loop(10) {
        Terminal.Echo("Number: " + Variables.i)
    }
}
```

### Example 5: Drawing with Kachua

```ictl
Program.Main {
    Kachua.SetColor("red")
    Kachua.SetPenWidth(2)
    
    Program.Loop(4) {
        Kachua.Forward(100)
        Kachua.Right(90)
    }
    
    Kachua.Show()
}
```

---

## Building from Source

### Prerequisites

- Python 3.7+
- Nuitka (for standalone executables)
- Inno Setup (for Windows installer)

### Steps

1. **Clone and navigate:**
```bash
git clone https://github.com/indiancoder3/abhinu-dev_basic-ictl.git
cd abhinu-dev_basic-ictl/code
```

2. **Build standalone (Nuitka):**
```bash
python -m nuitka --onefile main.py -o ICTL.exe
```

3. **Build installer (Inno Setup):**
- Edit the `.iss` script with your build paths
- Compile with Inno Setup

---

## Building Story

The journey of ICTL began with a simple question: **"How can we make programming accessible to everyone?"**

### Why ICTL?

**The Problem:**
- Most beginner languages are either too simple (Scratch) or too complex (Python)
- The gap between visual programming and text-based languages is huge
- Students get discouraged by cryptic error messages and complex syntax

**The Solution:**
- A language built from scratch for beginners
- Clean, readable syntax inspired by English
- Immediate feedback and helpful error messages
- Bridge the gap between visual and text-based programming

### Version History

- **v1.0** (Initial Release) - Basic commands, Terminal I/O, Variables, Math
- **v1.1.0** - Lists support, improved Math evaluation, security fixes
- **v26.05.01 (v1.2)** - Kachua graphics, GUI commands, better error handling
- **v26.04.01** - Code reorganization, performance improvements

---

## Contributing

Contributions are welcome! Whether it's bug fixes, new features, or documentation improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## License

This project is licensed under the **GNU General Public License v3.0** - see [LICENSE](LICENSE) file for details.

---

## Support & Community

- 🐛 **Report Bugs**: [Issues](https://github.com/indiancoder3/abhinu-dev_basic-ictl/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/indiancoder3/abhinu-dev_basic-ictl/discussions)
- 📧 **Contact**: Visit [IndianCoder3.github.io](https://indiancoder3.github.io)

---

**Happy Coding! 🎉 Everyone Can Code!**