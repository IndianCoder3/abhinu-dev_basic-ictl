# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

"""
Error handling and formatting for ICTL interpreter.
Provides friendly error messages with visual pointers to problem locations.
"""


class ICTLError(Exception):
    """Base exception for ICTL errors."""
    
    def __init__(self, message, line=None, col=None, context=None):
        """
        Initialize ICTL error.
        
        Args:
            message (str): Error description
            line (int): Line number (1-indexed)
            col (int): Column number (1-indexed) of error location
            context (str): The actual line content
        """
        self.message = message
        self.line = line
        self.col = col
        self.context = context
        super().__init__(self.message)
    
    def format_error(self, show_context=True):
        """
        Format error message with visual pointer.
        
        Args:
            show_context (bool): Whether to show the line and pointer
            
        Returns:
            str: Formatted error message
        """
        if not show_context or self.context is None:
            return f"❌ {self.message}"
        
        output = f"  {self.context}\n"
        
        if self.col is not None and self.col > 0:
            # Create caret pointer
            pointer = " " * (self.col - 1) + "^"
            output += pointer + "\n"
        
        output += f"❌ {self.message}"
        return output


class SyntaxErrorICTL(ICTLError):
    """ICTL syntax error."""
    pass


class RuntimeErrorICTL(ICTLError):
    """ICTL runtime error."""
    pass


class VariableErrorICTL(ICTLError):
    """ICTL variable error."""
    pass


class MathErrorICTL(ICTLError):
    """ICTL math/expression error."""
    pass


def find_variable_position(line, var_name):
    """
    Find the position of a variable reference in a line.
    
    Args:
        line (str): The full command line
        var_name (str): The variable name to find
        
    Returns:
        int: Column number (1-indexed) or None if not found
    """
    # Look for Variables.var_name pattern
    search_str = f"Variables.{var_name}"
    pos = line.find(search_str)
    if pos >= 0:
        return pos + 1  # Convert to 1-indexed
    return None


def find_math_position(line, func_name="Math"):
    """
    Find the position of a math function call.
    
    Args:
        line (str): The full command line
        func_name (str): The function name to find
        
    Returns:
        int: Column number (1-indexed) or None if not found
    """
    pos = line.find(func_name)
    if pos >= 0:
        return pos + 1  # Convert to 1-indexed
    return None


def format_command_help(command):
    """
    Provide help text for common command errors.
    
    Args:
        command (str): The command that failed
        
    Returns:
        str: Helpful suggestion
    """
    suggestions = {
        "Math.Eval": "Math.Eval() is an expression. Use: Terminal.Echo(Math.Eval(...))",
        "Math.Compare": "Math.Compare() is an expression. Use in: Variable = Math.Compare(...)",
        "Data.Compare": "Data.Compare() is an expression. Use in: Variable = Data.Compare(...)",
        "Variables.New": "Syntax: Variables.New(MyVar)  # No quotes around variable name",
        "Terminal.Echo": "Syntax: Terminal.Echo(\"text\") or Terminal.Echo(Variables.MyVar)",
        "Terminal.Ask": "Syntax: Variables.Name = Terminal.Ask(\"Prompt: \")",
        "Terminal.Style": "Syntax: Terminal.Style(\"red\")  # Colors: red, green, blue, yellow, cyan, magenta",
    }
    
    for cmd, help_text in suggestions.items():
        if cmd in command:
            return f"💡 Hint: {help_text}"
    
    return None
