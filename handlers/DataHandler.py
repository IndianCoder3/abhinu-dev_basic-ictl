# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# handlers/DataHandler.py
from ictl_builtins.data import (
    data_loose_compare, data_compare, data_int, data_float, data_string, data_typeof
)
from error_handler import RuntimeErrorICTL

def handle(cmd, args, eval_expr):
    """
    Handle Data.* commands.
    
    Args:
        cmd (str): The command name (e.g., "ToInt", "Compare")
        args (list[str]): Raw string arguments
        eval_expr: Reference to the eval_expr function for recursive evaluation
        
    Returns:
        Any: The result of the command
        
    Raises:
        RuntimeErrorICTL: On errors
    """
    try:
        if cmd == "LooseCompare":
            if len(args) != 2:
                raise RuntimeErrorICTL("Data.LooseCompare requires 2 arguments: Data.LooseCompare(a, b)")
            a, b = args
            return data_loose_compare(eval_expr(a), eval_expr(b))
            
        elif cmd == "Compare":
            if len(args) != 2:
                raise RuntimeErrorICTL("Data.Compare requires 2 arguments: Data.Compare(a, b)")
            a, b = args
            return data_compare(eval_expr(a), eval_expr(b))
            
        elif cmd == "ToInt":
            if not args:
                raise RuntimeErrorICTL("Data.ToInt requires 1 argument: Data.ToInt(value)")
            val = args[0]
            result = data_int(eval_expr(val))
            return int(result)
            
        elif cmd == "ToFloat":
            if not args:
                raise RuntimeErrorICTL("Data.ToFloat requires 1 argument: Data.ToFloat(value)")
            val = args[0]
            result = data_float(eval_expr(val))
            return float(result)
            
        elif cmd == "ToString":
            if not args:
                raise RuntimeErrorICTL("Data.ToString requires 1 argument: Data.ToString(value)")
            val = args[0]
            return data_string(eval_expr(val))
            
        elif cmd == "TypeOf":
            if not args:
                raise RuntimeErrorICTL("Data.TypeOf requires 1 argument: Data.TypeOf(value)")
            val = args[0]
            return data_typeof(eval_expr(val))
            
        else:
            raise RuntimeErrorICTL(f"Unknown Data command: {cmd}")
            
    except RuntimeErrorICTL:
        raise
    except Exception as e:
        raise RuntimeErrorICTL(f"Data.{cmd} error: {str(e)}")
