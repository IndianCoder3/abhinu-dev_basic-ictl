# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# handlers/TerminalHandler.py
from ictl_builtins.terminal import terminal_clear, terminal_echo, terminal_ask, terminal_style
from error_handler import RuntimeErrorICTL

def handle(cmd, args, eval_expr):
    """
    Handle Terminal.* commands in expressions.
    
    Note: Most Terminal commands (Echo, Ask, Clear, Style) are executed from 
    execute_line() rather than eval_expr(). This handler provides support if 
    these commands are needed in expression contexts.
    
    Args:
        cmd (str): The command name (e.g., "Echo", "Ask")
        args (list[str]): Raw string arguments
        eval_expr: Reference to the eval_expr function for recursive evaluation
        
    Returns:
        Any: The result of the command
        
    Raises:
        RuntimeErrorICTL: On errors
    """
    try:
        if cmd == "Echo":
            if not args:
                raise RuntimeErrorICTL("Terminal.Echo requires 1 argument: Terminal.Echo(value)")
            value = eval_expr(args[0])
            terminal_echo(value)
            return value
            
        elif cmd == "Ask":
            if not args:
                raise RuntimeErrorICTL("Terminal.Ask requires 1 argument: Terminal.Ask(prompt)")
            prompt = eval_expr(args[0])
            return terminal_ask(prompt)
            
        else:
            raise RuntimeErrorICTL(f"Unknown Terminal command: {cmd}")
            
    except RuntimeErrorICTL:
        raise
    except Exception as e:
        raise RuntimeErrorICTL(f"Terminal.{cmd} error: {str(e)}")
