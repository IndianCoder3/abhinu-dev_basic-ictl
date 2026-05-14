# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# Python style Extension of mathEngine by adding Math.SymPy and Math.NumPy

# Imports (sympy needs to be installed)
import re
from sympy import sympify, nsimplify
from ictl_builtins.variables import variables

# Rewriter: Preprocesses the math expression for SymPy and NumPy evaluation
 
def rewrite(expr: str):
    """
    Fully rewrite a math expression from ICTL style to pure math:
    - Replaces Variables.X with their numeric values
    - Converts √ to sqrt
    - Handles ^ as powers
    - Adds explicit multiplication for things like 2(3+1)
    - Returns a query for SymPy/NumPy to evaluate
    """
    expr = expr.strip()

    # 1️. Replace Variables.X with their actual numeric values
    for var, value in variables.items():
        if value is None:
            raise RuntimeError(f"Variable '{var}' is not assigned a value")
        expr = re.sub(rf"\bVariables\.{re.escape(var)}\b", str(value), expr)

    # 2️. Replace √ with sqrt
    expr = expr.replace("√", "sqrt")

    # 3️. Fix sqrt without parentheses: sqrt4 -> sqrt(4)
    expr = re.sub(r'sqrt(\d+(\.\d+)?)', r'sqrt(\1)', expr)

    # 4️. Add explicit multiplication: 2(3+1) -> 2*(3+1)
    expr = re.sub(r'(\d)\s*\(', r'\1*(', expr)
    expr = re.sub(r'\)\s*(\d)', r')*\1', expr)

    # 5️. Convert ^ to **
    expr = expr.replace("^", "**")

    # Optional: remove spaces
    expr = re.sub(r'\s+', '', expr)

    return (expr)

# Math.SymPy()
def math_sympy(query):
    """
    Solves a math expression using SymPy. It first rewrites the expression to handle ICTL-specific syntax, 
    then evaluates it with SymPy, and returns the result. If the expression is invalid, it raises a 
    RuntimeError with details.
    """
    question = rewrite(query)

    # Solve the question
    try:
        # Solve it
        result = sympify(question).doit()
        if result.is_number:
            result = result.evalf()

        # Return it
        return float(result)
    
    except Exception as e:
        # Throw error if invalid query
        raise RuntimeError(f"[Math Error] Invalid Math.SymPy expression: '{query}'. The interpreter had processed it as '{question}'")
    
# Math.NumPy()
def math_numpy(query):
    """
    Solves a math expression using NumPy. It first rewrites the expression to handle ICTL-specific syntax, 
    then evaluates it with NumPy, and returns the result. If the expression is invalid, it raises a 
    RuntimeError with details.
    """
    # Rewrite the query to handle ICTL-specific syntax and convert it to a form that can be evaluated by NumPy
    question = rewrite(query)

    # Solve the question
    try:
        # Solve it
        result = nsimplify(question).doit()
        if result.is_number:
            result = result.evalf()

        # Return it
        return float(result)
    
    except Exception as e:
        # Throw error if invalid query
        raise RuntimeError(f"[Math Error] Invalid Math.NumPy expression: '{query}'. The interpreter had processed it as '{question}'")
            
            