# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# builtins/data.py
"""Data type conversion and comparison functions for ICTL."""

def data_compare(a, b):
    """Compares two values for equality, considering type differences. For example, Data.Compare(123, "123") would return false."""
    return a == b

def data_loose_compare(a, b):
    """Compares two values for equality, ignoring type differences. For example, Data.LooseCompare(123, "123") would return true."""
    return str(a) == str(b)

def data_float(val):
    """Converts a value to a float. For example, Data.ToFloat(123) would return 123.0."""
    try:
        return float(val)
    except (ValueError, TypeError):
        raise RuntimeError(f"[Data Conversion Error] Data.ToFloat requires numeric arguments. Got: {repr(val)}")

def data_int(val):
    """Converts a value to an integer. For example, Data.ToInt(123.45) would return 123."""
    try:
        return int(float(val))  # Convert through float to handle "123.45"
    except (ValueError, TypeError):
        raise RuntimeError(f"[Data Conversion Error] Data.ToInt requires numeric arguments. Got: {repr(val)}")

def data_string(input_val):
    """Converts a value to a string. For example, Data.ToString(123) would return "123"."""
    try:
        return str(input_val)
    except (ValueError, TypeError):
        raise RuntimeError(f"[Data Conversion Error] Data.ToString has encountered an error. Input: {repr(input_val)}")

def data_typeof(val):
    """Returns the type of a value as a string. For example, Data.TypeOf(123) would return "int"."""
    return type(val).__name__