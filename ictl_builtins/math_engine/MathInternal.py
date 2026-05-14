# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

import math
import random
import operator
from ictl_builtins.variables import variables

OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow,
}

PREC = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

FUNCS = {
    "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "asin": math.asin, "acos": math.acos, "atan": math.atan,
    "sinh": math.sinh, "cosh": math.cosh, "tanh": math.tanh,
    "log": math.log, "log10": math.log10, "exp": math.exp,
    "abs": abs, "floor": math.floor, "ceil": math.ceil,
    "round": round, "degrees": math.degrees, "radians": math.radians,
}

CACHE = {}

# ------------------------
# Tokenizer (fast)
# ------------------------

def tokenize(expr):
    tokens = []
    i = 0
    prev = None

    while i < len(expr):
        c = expr[i]

        # number (with unary minus)
        if c.isdigit() or c == "." or (
            c == "-" and prev in (None,"(","+","-","*","/","^")
        ):
            num = c
            i += 1
            while i < len(expr) and (expr[i].isdigit() or expr[i] == "."):
                num += expr[i]
                i += 1
            tokens.append(("num", float(num)))
            prev = "num"
            continue

        # Variables.x
        if expr.startswith("Variables.", i):
            i += 10
            name = ""
            while i < len(expr) and (expr[i].isalnum() or expr[i]=="_"):
                name += expr[i]
                i += 1
            tokens.append(("var", name))
            prev = "var"
            continue

        # function
        if c.isalpha():
            name = c
            i += 1
            while i < len(expr) and expr[i].isalpha():
                name += expr[i]
                i += 1
            tokens.append(name)
            prev = "func"
            continue

        if c.strip():
            tokens.append(c)
            prev = c

        i += 1

    return tokens


# ------------------------
# Parser
# ------------------------

def shunting_yard(tokens):
    out, stack = [], []

    for token in tokens:

        if isinstance(token, tuple):
            out.append(token)

        elif token in FUNCS:
            stack.append(token)

        elif token in OPS:
            while stack and stack[-1] in OPS and PREC[stack[-1]] >= PREC[token]:
                out.append(stack.pop())
            stack.append(token)

        elif token == "(":
            stack.append(token)

        elif token == ")":
            while stack and stack[-1] != "(":
                out.append(stack.pop())
            stack.pop()

            if stack and stack[-1] in FUNCS:
                out.append(stack.pop())

    while stack:
        out.append(stack.pop())

    return out


# ------------------------
# Evaluator
# ------------------------

def eval_rpn(rpn):
    stack = []

    for token in rpn:

        if isinstance(token, tuple):

            t, v = token

            if t == "num":
                stack.append(v)

            elif t == "var":
                if v not in variables:
                    raise RuntimeError(f"[Math Error] Variable '{v}' not defined")
                stack.append(float(variables[v]))

        elif token in OPS:
            b = stack.pop()
            a = stack.pop()
            stack.append(OPS[token](a,b))

        elif token in FUNCS:
            stack.append(FUNCS[token](stack.pop()))

    return stack[0]


# ------------------------
# Main API
# ------------------------

def math_eval(expr):

    if expr not in CACHE:
        tokens = tokenize(expr)
        CACHE[expr] = shunting_yard(tokens)

    try:
        result = eval_rpn(CACHE[expr])
        # Return as integer if it's a whole number, otherwise as float
        return int(result) if isinstance(result, float) and result.is_integer() else result
    except Exception:
        raise RuntimeError(f"[Math Error] Invalid Math.Eval expression: {expr}")


def math_compare(a, symbol, b):
    """Compare two numeric values using a comparison operator.
    
    Args:
        a: First value
        symbol: Comparison operator (==, !=, >, <, >=, <=)
        b: Second value
        
    Returns:
        bool: Result of comparison
        
    Raises:
        RuntimeError: If invalid comparison symbol
    """
    a, b = float(a), float(b)

    if symbol == "==":
        return a == b
    if symbol == "!=":
        return a != b
    if symbol == ">":
        return a > b
    if symbol == "<":
        return a < b
    if symbol == ">=":
        return a >= b
    if symbol == "<=":
        return a <= b

    raise RuntimeError("[Math Error] Invalid comparison symbol")


def math_random(min_val, max_val):
    """
    Generate a random integer between min_val and max_val (inclusive).
    
    Args:
        min_val: Minimum value (inclusive)
        max_val: Maximum value (inclusive)
        
    Returns:
        int: Random integer between min_val and max_val
        
    Raises:
        RuntimeError: If arguments are invalid
    """
    try:
        min_val = int(float(min_val))
        max_val = int(float(max_val))
        
        if min_val > max_val:
            raise RuntimeError("[Math Error] min value cannot be greater than max value")
        
        return random.randint(min_val, max_val)
    except (ValueError, TypeError):
        raise RuntimeError(f"[Math Error] Math.Random requires numeric arguments: Math.Random(min, max). Got min={min_val}, max={max_val}")