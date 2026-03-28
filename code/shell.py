# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

"""
Interactive shell for ICTL (Abhinu.Dev Basic Language)

Provides an interactive REPL environment for executing simple ICTL commands.
Note: ICTL is primarily a file-based language. The shell supports single-line
commands only. Use 'load' to execute full .ictl program files.
"""

import sys
from runtime import run_item, run_program
from parser import parse_file
from ictl_builtins.variables import variables
from control import BreakSignal, ContinueSignal
from error_handler import (
    ICTLError, VariableErrorICTL, MathErrorICTL,
    find_variable_position, find_math_position
)


class ICTLShell:
    """Interactive shell for executing ICTL commands."""

    def __init__(self):
        """Initialize the ICTL shell with welcome message and history."""
        self.history = []
        self.running = False
        self._print_welcome()

    def _print_welcome(self):
        """Display welcome message with available commands."""
        print("\nAbhinu.Dev Basic ICTL Interactive Shell")
        print("=" * 50)
        print("Type 'help' for available commands")
        print("Type 'exit' to quit the shell")
        print("=" * 50 + "\n")

    def _print_help(self):
        """Display help information about available commands."""
        help_text = """
═══════════════════════════════════════════════════════════════
                    ICTL SHELL QUICK REFERENCE
═══════════════════════════════════════════════════════════════

SHELL COMMANDS:
  exit              - Exit the shell
  help              - Show this help message
  history           - Show command history
  vars              - Show all variables
  clear             - Clear the screen
  load <file.ictl>  - Load and execute a full ICTL program file

═══════════════════════════════════════════════════════════════
                    DIRECT ICTL COMMANDS (Single Line)
═══════════════════════════════════════════════════════════════

TERMINAL I/O:
  Terminal.Echo(<value>)              - Print text/values
    Examples:
      Terminal.Echo("Hello World")
      Terminal.Echo(Variables.MyVar)
      Terminal.Echo("Count: " + Variables.X)
  
  Terminal.Ask(<prompt>)              - Get user input
    Examples:
      Variables.Name = Terminal.Ask("Your name: ")
  
  Terminal.Style(<color>)             - Set text color
    Colors: "red", "green", "blue", "yellow", "cyan", "magenta"
    Examples:
      Terminal.Style("green")

VARIABLES:
  Variables.New(<name>)               - Create variable
    Example: Variables.New(MyVar)
  
  Variables.<name> = <value>          - Assign value
    Examples:
      Variables.X = 42
      Variables.Name = "Alice"
      Variables.Result = Math.Eval(10 + 5)

MATH & COMPARISON (use in expressions):
  Math.Eval(<arithmetic>)             - Calculate math
    Example: Terminal.Echo(Math.Eval(2 + 2))
  
  Math.Compare(<a>, <op>, <b>)        - Compare numbers
    Example: Terminal.Echo(Math.Compare(10, ">", 5))
  
  Data.Compare(<a>, <b>)              - Compare values
    Example: Terminal.Echo(Data.Compare("hello", "hello"))

═══════════════════════════════════════════════════════════════
                    BLOCK STRUCTURES (use with 'load')
═══════════════════════════════════════════════════════════════

  Program.Main { ... }                - Entry point
  Program.If(<condition>) { ... }     - Conditionals
  Program.Loop(<count>) { ... }       - Repeat N times
  Program.ForeverLoop { ... }         - Infinite loop
  Program.BreakLoop                   - Exit loop
  Program.Continue                    - Next iteration

Use 'load examples/megatest.ictl' to see comprehensive examples!

═══════════════════════════════════════════════════════════════
"""
        print(help_text)

    def _show_history(self):
        """Display command execution history."""
        if not self.history:
            print("No command history yet.")
            return

        print("\nCommand History:")
        print("-" * 40)
        for i, cmd in enumerate(self.history, 1):
            print(f"  {i:2d}. {cmd}")
        print("-" * 40)

    def _show_variables(self):
        """Display all defined variables."""
        if not variables:
            print("No variables defined yet.")
            return

        print("\nDefined Variables:")
        print("-" * 40)
        for name, value in variables.items():
            print(f"  {name} = {repr(value)}")
        print("-" * 40)

    def _execute_command(self, line):
        """
        Execute a single ICTL command.
        
        Args:
            line (str): The command to execute
            
        Returns:
            bool: True if command executed successfully, False otherwise
        """
        try:
            run_item(line)
            return True
        except (BreakSignal, ContinueSignal):
            self._print_error_with_context(line, "Cannot use BreakLoop or Continue outside of a loop")
            return False
        except VariableErrorICTL as e:
            # Find the position of the undefined variable
            var_name = str(e.message).split("'")[1] if "'" in str(e.message) else None
            col = None
            if var_name:
                col = find_variable_position(line, var_name)
            self._print_error_with_context(line, str(e.message), col)
            return False
        except MathErrorICTL as e:
            # Find math function position
            col = find_math_position(line)
            self._print_error_with_context(line, str(e.message), col)
            return False
        except ICTLError as e:
            # Other ICTL errors
            self._print_error_with_context(line, str(e.message))
            return False
        except Exception as e:
            # Catch any other unexpected errors
            self._print_error_with_context(line, str(e))
            return False

    def _print_error_with_context(self, line, message, col=None):
        """
        Print error message with the command line and caret pointer.
        
        Args:
            line (str): The command line that caused the error
            message (str): The error message
            col (int): Column number (1-indexed) where error occurred
        """
        prefix = "  "
        print(f"{prefix}{line}")
        
        if col is not None and col > 0:
            # Account for the prefix when positioning the caret
            pointer = prefix + " " * (col - 1) + "^"
            print(pointer)
        
        print(f"❌ {message}")

    def _prompt_input(self):
        """
        Get user input from prompt.
        
        Returns:
            str: User input or None if EOF reached
        """
        try:
            return input(">>> ").strip()
        except EOFError:
            return None

    def run(self):
        """Start the interactive shell loop."""
        self.running = True
        
        while self.running:
            line = self._prompt_input()
            
            # Handle EOF (Ctrl+D on Unix, Ctrl+Z on Windows)
            if line is None:
                print("\nExit")
                break
            
            # Skip empty lines and comments
            if not line or line.startswith("#"):
                continue
            
            # Handle built-in shell commands
            if self._handle_builtin_command(line):
                continue
            
            # Execute ICTL command
            self._execute_command(line)
            self.history.append(line)

    def _handle_builtin_command(self, line):
        """
        Handle built-in shell commands.
        
        Args:
            line (str): The input line to check
            
        Returns:
            bool: True if a built-in command was executed, False otherwise
        """
        lower_line = line.lower()
        
        if lower_line == "exit":
            print("Goodbye! 👋")
            self.running = False
            return True
        
        if lower_line == "help":
            self._print_help()
            return True
        
        if lower_line == "history":
            self._show_history()
            return True
        
        if lower_line == "vars":
            self._show_variables()
            return True
        
        if lower_line == "clear":
            import os
            os.system("cls" if os.name == "nt" else "clear")
            return True
        
        if lower_line.startswith("load "):
            filename = line[5:].strip()
            self._load_file(filename)
            return True
        
        return False

    def _load_file(self, filename):
        """
        Load and execute an ICTL program file.
        
        Args:
            filename (str): Path to the .ictl file to load
        """
        try:
            program = parse_file(filename)
            print(f"Loading {filename}...")
            run_program(program)
            print(f"✓ {filename} executed successfully")
        except ICTLError as e:
            # ICTL errors are already formatted
            print(str(e))
        except FileNotFoundError:
            print(f"❌ Error: File '{filename}' not found")
        except IOError as e:
            print(f"❌ Error: Cannot read file '{filename}': {str(e)}")
        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")


def main():
    """Entry point for the interactive shell."""
    shell = ICTLShell()
    shell.run()


if __name__ == "__main__":
    main()