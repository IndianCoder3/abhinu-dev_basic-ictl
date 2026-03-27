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
