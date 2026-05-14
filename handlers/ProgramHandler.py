# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# handlers/ProgramHandler.py
from error_handler import RuntimeErrorICTL

def handle(cmd, args, eval_expr):
    """
    Handle Program.* commands that are expressions (not blocks).
    
    Args:
        cmd (str): The command name (e.g., "Not")
        args (list[str]): Raw string arguments
        eval_expr: Reference to the eval_expr function for recursive evaluation
        
    Returns:
        Any: The result of the command (e.g., boolean for Not)
        
    Raises:
        RuntimeErrorICTL: On errors
    """
    try:
        if cmd == "Not":
            if len(args) != 1:
                raise RuntimeErrorICTL("Program.Not requires 1 argument: Program.Not(condition)")
            inner = args[0]
            result = eval_expr(inner)
            # Convert result to boolean and negate
            return not bool(result)
            
        else:
            raise RuntimeErrorICTL(f"Unknown Program command: {cmd}. Note: Program.Main, If, Else, Loop, ForeverLoop, BreakLoop, Continue are block structures.")
            
    except RuntimeErrorICTL:
        raise
    except Exception as e:
        raise RuntimeErrorICTL(f"Program.{cmd} error: {str(e)}")
