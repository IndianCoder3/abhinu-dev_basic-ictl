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
    print(value)

def terminal_ask(prompt):
    return input(prompt)

def terminal_style(style):
    if style not in STYLES:
        raise RuntimeError(f"[Terminal Error] Unknown style '{style}'")
    print(STYLES[style], end="")

def terminal_clear():
    """Clear the terminal screen (cross-platform compatible)."""
    os.system('cls' if os.name == 'nt' else 'clear')

