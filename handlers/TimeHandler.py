# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# handlers/TimeHandler.py
from ictl_builtins.time import time_wait, time_current
from error_handler import RuntimeErrorICTL

def handle(cmd, args, eval_expr):
    """
    Handle Time.* commands.
    
    Args:
        cmd (str): The command name (e.g., "Current", "Wait")
        args (list[str]): Raw string arguments
        eval_expr: Reference to the eval_expr function for recursive evaluation
        
    Returns:
        Any: The result of the command
        
    Raises:
        RuntimeErrorICTL: On errors
    """
    try:
        if cmd == "Current":
            if not args:
                raise RuntimeErrorICTL('Time.Current() requires a format string: Time.Current("HH:mm:ss tt")')
            format_str = eval_expr(args[0])
            return time_current(format_str)
        
        elif cmd == "Wait":
            if not args:
                raise RuntimeErrorICTL('Time.Wait() requires seconds: Time.Wait(1)')
            seconds = eval_expr(args[0])
            time_wait(seconds)
            return None
            
        else:
            raise RuntimeErrorICTL(f"Unknown Time command: {cmd}")
            
    except RuntimeErrorICTL:
        raise
    except RuntimeError as e:
        raise RuntimeErrorICTL(str(e))
    except Exception as e:
        raise RuntimeErrorICTL(f"Time.{cmd} error: {str(e)}")
