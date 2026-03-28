# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# runtime.py
from ictl_builtins.terminal import terminal_clear, terminal_echo, terminal_ask, terminal_style
from ictl_builtins.variables import variables, new_variable
from ictl_builtins.math import math_eval, math_compare, math_random
from ictl_builtins.data import data_compare
from ictl_builtins.time import time_wait, time_current
from control import BreakSignal, ContinueSignal
from error_handler import (
    RuntimeErrorICTL, VariableErrorICTL, MathErrorICTL, format_command_help
)

# Global state to track if the last If condition was executed
_last_if_executed = False

def run_program(program):
    for item in program:
        run_item(item)

def run_item(item):
    if isinstance(item, str):
        execute_line(item)
    elif isinstance(item, dict):
        run_block(item)

def run_block(block):
    global _last_if_executed
    
    header = block["header"]
    lines = block["lines"]

    if header == "Program.Main":
        for item in lines:
            run_item(item)
        return

    if header.startswith("Program.Loop"):
        count = int(extract_args(header)[0])
        for _ in range(count):
            try:
                for item in lines:
                    run_item(item)
            except ContinueSignal:
                continue
            except BreakSignal:
                break
        return

    if header == "Program.ForeverLoop":
        while True:
            try:
                for item in lines:
                    run_item(item)
            except ContinueSignal:
                continue
            except BreakSignal:
                break
        return
    
    if header.startswith("Program.If"):
        condition = header[header.find("(")+1 : header.rfind(")")]
        result = eval_expr(condition)
        _last_if_executed = result

        if result:
            for item in lines:
                run_item(item)
        return

    if header == "Program.Else":
        # Program.Else only executes if the previous Program.If condition was False
        if not _last_if_executed:
            for item in lines:
                run_item(item)
        _last_if_executed = False  # Reset after Else block
        return

    raise RuntimeErrorICTL(f"Unknown block: '{header}'")


def execute_line(line):
    """
    Execute a single ICTL command.
    
    Args:
        line (str): The ICTL command to execute
        
    Raises:
        RuntimeErrorICTL: On execution errors
    """
    try:
        if line.startswith("Terminal.Echo"):
            value = eval_expr(extract_args(line)[0])
            terminal_echo(value)
            return

        if line.startswith("Terminal.Ask"):
            return terminal_ask(eval_expr(extract_args(line)[0]))

        if line.startswith("Variables.New"):
            new_variable(extract_args(line)[0])
            return

        if line.startswith("Variables.") and "=" in line:
            name, expr = line.split("=", 1)
            var_name = name.replace("Variables.", "").strip()
            expr = expr.strip()

            if expr.startswith("Terminal.Ask"):
                prompt = eval_expr(extract_args(expr)[0])
                variables[var_name] = terminal_ask(prompt)
            else:
                variables[var_name] = eval_expr(expr)

            return

        if line == "Program.BreakLoop":
            raise BreakSignal()

        if line == "Program.Continue":
            raise ContinueSignal()
        
        if line == "Terminal.Clear":
            terminal_clear()
            return
        
        if line.startswith("Terminal.Style"):
            style = eval_expr(extract_args(line)[0])
            terminal_style(style)
            return

        if line.startswith("Time.Wait"):
            seconds = eval_expr(extract_args(line)[0])
            time_wait(seconds)
            return

        # Unknown command
        error = RuntimeErrorICTL(f"Unknown command: '{line}'")
        hint = format_command_help(line)
        if hint:
            raise RuntimeErrorICTL(f"Unknown command: '{line}'\n{hint}")
        raise error
        
    except (BreakSignal, ContinueSignal):
        raise
    except (RuntimeErrorICTL, VariableErrorICTL, MathErrorICTL):
        raise
    except Exception as e:
        raise RuntimeErrorICTL(f"Execution error: {str(e)}")

def extract_args(text):
    inside = text[text.find("(")+1:text.rfind(")")]
    args = split_by_comma_respecting_quotes(inside)
    return args

def split_by_comma_respecting_quotes(text):
    """Split by comma but respect string literal boundaries"""
    args = []
    current = ""
    in_string = False
    
    for char in text:
        if char == '"':
            in_string = not in_string
            current += char
        elif char == ',' and not in_string:
            args.append(current.strip())
            current = ""
        else:
            current += char
    
    if current.strip():
        args.append(current.strip())
    
    return args

def eval_expr(expr):
    """
    Evaluate an ICTL expression.
    
    Args:
        expr (str): The expression to evaluate
        
    Returns:
        Any: The evaluated result
        
    Raises:
        VariableErrorICTL: On variable-related errors
        MathErrorICTL: On math-related errors
    """
    expr = expr.strip()

    # Boolean literals
    if expr == "True":
        return True
    if expr == "False":
        return False

    # Handle concatenation FIRST (before string literal check)
    if has_concat_outside_quotes_and_parens(expr):
        parts = split_by_concat_operator(expr)
        return "".join(str(eval_expr(p.strip())) for p in parts)

    # String literal (only simple strings without +)
    if expr.startswith('"') and expr.endswith('"'):
        return expr[1:-1]

    # Variable
    if expr.startswith("Variables."):
        var_name = expr.replace("Variables.", "")
        if var_name not in variables:
            raise VariableErrorICTL(f"Variable '{var_name}' is not defined")
        return variables[var_name]

    # Math.Eval MUST be resolved early
    if expr.startswith("Math.Eval"):
        try:
            inner = extract_args(expr)[0]
            # Pass raw expression directly, math engine handles Variables.*
            return math_eval(inner)
        except IndexError:
            raise MathErrorICTL("Math.Eval() requires an expression: Math.Eval(2+2)")
        except Exception as e:
            raise MathErrorICTL(f"Math.Eval error: {str(e)}")

    # Math.Compare
    if expr.startswith("Math.Compare"):
        try:
            args = extract_args(expr)
            if len(args) != 3:
                raise MathErrorICTL("Math.Compare requires 3 arguments: Math.Compare(a, op, b)")
            a, symbol, b = args
            return math_compare(eval_expr(a), eval_expr(symbol), eval_expr(b))
        except MathErrorICTL:
            raise
        except Exception as e:
            raise MathErrorICTL(f"Math.Compare error: {str(e)}")

    # Math.Random
    if expr.startswith("Math.Random"):
        try:
            args = extract_args(expr)
            if len(args) != 2:
                raise MathErrorICTL("Math.Random requires 2 arguments: Math.Random(min, max)")
            min_val, max_val = args
            return math_random(eval_expr(min_val), eval_expr(max_val))
        except MathErrorICTL:
            raise
        except Exception as e:
            raise MathErrorICTL(f"Math.Random error: {str(e)}")

    # Program.Not
    if expr.startswith("Program.Not"):
        try:
            args = extract_args(expr)
            if len(args) != 1:
                raise RuntimeErrorICTL("Program.Not requires 1 argument: Program.Not(condition)")
            inner = args[0]
            result = eval_expr(inner)
            # Convert result to boolean and negate
            return not bool(result)
        except RuntimeErrorICTL:
            raise
        except Exception as e:
            raise RuntimeErrorICTL(f"Program.Not error: {str(e)}")

    if expr.startswith("Time.Current"):
        try:
            format_str = eval_expr(extract_args(expr)[0])
            return time_current(format_str)
        except IndexError:
            raise RuntimeErrorICTL("Time.Current() requires a format string: Time.Current(\"HH:mm:ss tt\")")
        except RuntimeError as e:
            raise RuntimeErrorICTL(str(e))
        except Exception as e:
            raise RuntimeErrorICTL(f"Time.Current error: {str(e)}")

    if expr.startswith("Data.Compare"):
        try:
            args = extract_args(expr)
            if len(args) != 2:
                raise RuntimeErrorICTL("Data.Compare requires 2 arguments: Data.Compare(a, b)")
            a, b = args
            return data_compare(eval_expr(a), eval_expr(b))
        except Exception as e:
            raise RuntimeErrorICTL(f"Data.Compare error: {str(e)}")

    # Raw number (handles integers, negative numbers, and floats)
    try:
        if '.' in expr:
            return float(expr)
        else:
            return int(expr)
    except ValueError:
        pass

    return expr

#def resolve_math_expr(expr):
#    expr = expr.strip()
#
#    # Replace Variables.X with their values
#    for name, value in variables.items():
#        expr = expr.replace(f"Variables.{name}", str(value))
#
#    return expr

def split_by_concat_operator(expr):
    """Split expression by + operator, but respect string boundaries and parentheses"""
    parts = []
    current = ""
    in_string = False
    paren_depth = 0
    
    for char in expr:
        if char == '"':
            in_string = not in_string
            current += char
        elif char == '(' and not in_string:
            paren_depth += 1
            current += char
        elif char == ')' and not in_string:
            paren_depth -= 1
            current += char
        elif char == '+' and not in_string and paren_depth == 0:
            if current:
                parts.append(current)
            current = ""
        else:
            current += char
    
    if current:
        parts.append(current)
    
    return parts

def has_concat_outside_quotes_and_parens(expr):
    """Check if there's a + operator outside of string literals AND parentheses"""
    in_string = False
    paren_depth = 0
    for char in expr:
        if char == '"':
            in_string = not in_string
        elif char == '(' and not in_string:
            paren_depth += 1
        elif char == ')' and not in_string:
            paren_depth -= 1
        elif char == '+' and not in_string and paren_depth == 0:
            return True
    return False
