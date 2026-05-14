# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# ictl_builtins/math.py
"""Math operations for ICTL including evaluation, comparison, and advanced math."""

# Imports
import ictl_builtins.math_engine.MathInternal as mathEngine
import ictl_builtins.math_engine.PyEval as math_pyeval

# Tunnel all math operations into mathEngine (eval, compare, random) and PyEval (sympy, numpy)
def math_sympy(expr):
    """Evaluate expression using SymPy symbolic math library."""
    return math_pyeval.math_sympy(expr)

def math_numpy(expr):
    """Evaluate expression using NumPy numerical library."""
    return math_pyeval.math_numpy(expr)

def math_random(min_val, max_val):
    """Generate random integer between min_val and max_val (inclusive)."""
    return mathEngine.math_random(min_val, max_val)

def math_compare(a, symbol, b):
    """Compare two values using a comparison operator."""
    return mathEngine.math_compare(a, symbol, b)

def math_eval(expr):
    """Evaluate a mathematical expression."""
    return mathEngine.math_eval(expr)
