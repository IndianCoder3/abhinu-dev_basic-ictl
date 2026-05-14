# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# builtins/variables.py
"""Global variable storage for ICTL programs."""

variables = {}

def new_variable(name):
    """Create a new variable (deprecated - variables are auto-created on assignment)."""
    if name in variables:
        raise RuntimeError(f"Variable {name} already exists")
    variables[name] = None
