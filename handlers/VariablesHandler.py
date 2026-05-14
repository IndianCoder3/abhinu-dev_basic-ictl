# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# handlers/VariablesHandler.py
from ictl_builtins.variables import variables, new_variable
from error_handler import VariableErrorICTL, RuntimeErrorICTL

def handle(cmd, args, eval_expr):
    """
    Handle Variables.* commands in expressions.
    
    Note: Simple variable access (e.g., Variables.x) is handled directly in eval_expr()
    before routing to handlers. This handler is for command-style Variables operations.
    
    Args:
        cmd (str): The command name
        args (list[str]): Raw string arguments
        eval_expr: Reference to the eval_expr function for recursive evaluation
        
    Returns:
        Any: The result of the command
        
    Raises:
        VariableErrorICTL: On variable-related errors
    """
    try:
        # Currently no command-style Variables.* expressions are defined
        # This handler is provided for future expansion (e.g., Variables.Get, Variables.Set, etc.)
        raise RuntimeErrorICTL(f"Unknown Variables command: {cmd}")
            
    except (VariableErrorICTL, RuntimeErrorICTL):
        raise
    except Exception as e:
        raise RuntimeErrorICTL(f"Variables.{cmd} error: {str(e)}")
