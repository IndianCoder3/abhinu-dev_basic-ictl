# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# handlers/MathHandler.py
import re
from ictl_builtins.math import math_eval, math_compare, math_random, math_numpy, math_sympy
from error_handler import MathErrorICTL

def _resolve_nested_ictl_calls(expr, eval_expr):
    """
    Pre-evaluate nested ICTL function calls in an expression.
    
    This allows Math.Eval/NumPy/SymPy to handle expressions containing
    other ICTL commands like Data.ToFloat(), Variables.x, etc.
    
    Example:
        Input: "Data.ToFloat(\"2\") + Data.ToFloat(\"3\")"
        Output: "2.0 + 3.0"
    
    Args:
        expr (str): The expression potentially containing ICTL calls
        eval_expr: Reference to eval_expr for recursive evaluation
        
    Returns:
        str: The expression with all nested ICTL calls evaluated and replaced
    """
    result = expr
    max_iterations = 50  # Prevent infinite loops
    iteration = 0
    
    while iteration < max_iterations:
        iteration += 1
        import re
        pattern = r'([A-Za-z_]\w*)\.([A-Za-z_]\w*)\s*\('
        matches = list(re.finditer(pattern, result))
        
        if not matches:
            break
            
        # Process matches in reverse order to maintain correct positions
        for match in reversed(matches):
            start = match.start()
            
            # Find the balanced closing parenthesis
            paren_count = 1
            i = match.end()
            while i < len(result) and paren_count > 0:
                if result[i] == '(':
                    paren_count += 1
                elif result[i] == ')':
                    paren_count -= 1
                i += 1
            
            if paren_count != 0:
                raise MathErrorICTL(f"Unbalanced parentheses in expression: {result}")
            
            # Extract the complete function call
            func_call = result[start:i]
            
            # Try to evaluate this function call
            try:
                evaluated = str(eval_expr(func_call))
                result = result[:start] + evaluated + result[i:]
            except Exception as e:
                # If evaluation fails, raise error
                raise MathErrorICTL(f"Error evaluating nested call '{func_call}': {str(e)}")
    
    if iteration >= max_iterations:
        raise MathErrorICTL("Too many nested ICTL calls (possible infinite loop)")
    
    return result

def handle(cmd, args, eval_expr):
    """
    Handle Math.* commands.
    
    Args:
        cmd (str): The command name (e.g., "Random", "Eval")
        args (list[str]): Raw string arguments
        eval_expr: Reference to the eval_expr function for recursive evaluation
        
    Returns:
        Any: The result of the command
        
    Raises:
        MathErrorICTL: On math-related errors
    """
    try:
        if cmd == "Eval":
            if not args:
                raise MathErrorICTL("Math.Eval() requires an expression: Math.Eval(2+2)")
            inner = args[0]
            # Pre-evaluate nested ICTL calls, then pass to math engine
            resolved = _resolve_nested_ictl_calls(inner, eval_expr)
            return math_eval(resolved)
            
        elif cmd == "NumPy":
            if not args:
                raise MathErrorICTL("Math.NumPy() requires an expression: Math.NumPy(2+2)")
            inner = args[0]
            # Pre-evaluate nested ICTL calls, then pass to math engine
            resolved = _resolve_nested_ictl_calls(inner, eval_expr)
            return math_numpy(resolved)
            
        elif cmd == "SymPy":
            if not args:
                raise MathErrorICTL("Math.SymPy() requires an expression: Math.SymPy(2+2)")
            inner = args[0]
            # Pre-evaluate nested ICTL calls, then pass to math engine
            resolved = _resolve_nested_ictl_calls(inner, eval_expr)
            return math_sympy(resolved)
            
        elif cmd == "Compare":
            if len(args) != 3:
                raise MathErrorICTL("Math.Compare requires 3 arguments: Math.Compare(a, op, b)")
            a, symbol, b = args
            return math_compare(eval_expr(a), eval_expr(symbol), eval_expr(b))
            
        elif cmd == "Random":
            if len(args) != 2:
                raise MathErrorICTL("Math.Random requires 2 arguments: Math.Random(min, max)")
            min_val, max_val = args
            return math_random(eval_expr(min_val), eval_expr(max_val))
            
        else:
            raise MathErrorICTL(f"Unknown Math command: {cmd}")
            
    except MathErrorICTL:
        raise
    except Exception as e:
        raise MathErrorICTL(f"Math.{cmd} error: {str(e)}")
