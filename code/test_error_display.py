# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

#!/usr/bin/env python3
"""Test script for shell error display"""
import sys
from runtime import run_item
from error_handler import VariableErrorICTL

# Test case 1: undefined variable
print("Test 1: Undefined variable error")
try:
    run_item('Terminal.Echo(Variables.Sus)')
except VariableErrorICTL as e:
    # Show like the shell would
    line = 'Terminal.Echo(Variables.Sus)'
    col = line.find('Variables.Sus') + 1
    print(f"  {line}")
    print(" " * (col - 1) + "^")
    print(f"❌ {str(e.message)}")
