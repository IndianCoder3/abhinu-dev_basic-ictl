# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# builtins/terminal.py

import os

STYLES = {
    "reset": "\033[0m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "bold": "\033[1m"
}

def terminal_echo(value):
    """Print a value to the terminal."""
    print(value)

def terminal_ask(prompt):
    """Ask the user for input and return the response."""
    return input(prompt)

def terminal_style(style):
    """Set the terminal text style/color."""
    if style not in STYLES:
        raise RuntimeError(f"[Terminal Error] Unknown style '{style}'")
    print(STYLES[style], end="")

def terminal_clear():
    """Clear the terminal screen (cross-platform compatible)."""
    os.system('cls' if os.name == 'nt' else 'clear')
