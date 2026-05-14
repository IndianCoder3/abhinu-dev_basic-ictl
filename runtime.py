# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# runtime.py
from ictl_builtins.terminal import terminal_clear, terminal_echo, terminal_ask, terminal_style
from ictl_builtins.variables import variables
from ictl_builtins.time import time_wait
from control import BreakSignal, ContinueSignal
from error_handler import (
    RuntimeErrorICTL, VariableErrorICTL, MathErrorICTL, format_command_help
)
import re

# Global state to track if the last If condition was executed
_last_if_executed = False

# Global dictionary to store user-defined Kheer functions (like scripts/procedures)
# Format: {"name": {"lines": [...], "params": [...]}}
_kheers = {}

def run_program(program):
    for item in program:
        run_item(item)

def run_item(item):
    if isinstance(item, str):
        execute_line(item)
    elif isinstance(item, dict):
        run_block(item)

def run_block(block):
    global _last_if_executed, _kheers
    
    header = block["header"]
    lines = block["lines"]
    
    # Normalize block header for case-insensitive support
    header = _normalize_command(header)

    if header == "Program.Main":
        # Reset flag when starting the main program
        _last_if_executed = True
        for item in lines:
            run_item(item)
        return

    if header.startswith("Program.Kheer"):
        # This line was missing! It finds the name inside the ( )
        kheer_name = header[header.find("(")+1 : header.rfind(")")]
        
        _kheers[kheer_name] = lines
        _last_if_executed = True # Reset flag
        return

    if header.startswith("Program.Loop"):
        _last_if_executed = True # Reset flag
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
        _last_if_executed = True # Reset flag
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
        
        # This tells the next Else block if it should run or skip
        _last_if_executed = result

        if result:
            for item in lines:
                run_item(item)
        return

    if header == "Program.Else":
        # Only run if the LAST If block was False
        if not _last_if_executed:
            for item in lines:
                run_item(item)
        
        # Set to True after running so a second Else cannot trigger
        _last_if_executed = True 
        return

    raise RuntimeErrorICTL(f"Unknown block: '{header}'")


# Cache for case mapping to avoid repeated dictionary creation
_CASE_MAP_CACHE = None

def _get_case_map():
    """Get the cached case mapping dictionary."""
    global _CASE_MAP_CACHE
    if _CASE_MAP_CACHE is None:
        _CASE_MAP_CACHE = {
        # Categories
        "terminal": "Terminal",
        "variables": "Variables",
        "math": "Math",
        "data": "Data",
        "program": "Program",
        "time": "Time",
        "lists": "Lists",
        "kachua": "Kachua",
        "gui": "GUI",
        
        # Terminal commands
        "echo": "Echo",
        "ask": "Ask",
        "style": "Style",
        "clear": "Clear",
        
        # Variables commands
        "new": "New",
        
        # Math commands
        "eval": "Eval",
        "compare": "Compare",
        "random": "Random",
        "numpy": "NumPy",
        "sympy": "SymPy",
        
        # Data commands
        "toint": "ToInt",
        "tofloat": "ToFloat",
        "tostring": "ToString",
        "typeof": "TypeOf",
        "loosecompare": "LooseCompare",
        
        # Program commands
        "main": "Main",
        "if": "If",
        "else": "Else",
        "loop": "Loop",
        "foreverloop": "ForeverLoop",
        "breakloop": "BreakLoop",
        "continue": "Continue",
        "not": "Not",
        "kheer": "Kheer",
        "executekheer": "ExecuteKheer",
        
        # Time commands
        "wait": "Wait",
        "current": "Current",
        
        # List commands
        "get": "Get",
        "create": "Create",
        "push": "Push",
        "pop": "Pop",
        
        # Kachua commands (Turtle Graphics)
        "forward": "Forward",
        "backward": "Backward",
        "right": "Right",
        "left": "Left",
        "penup": "PenUp",
        "pendown": "PenDown",
        "setcolor": "SetColor",
        "setpenwidth": "SetPenWidth",
        "setspeed": "SetSpeed",
        "goto": "GoTo",
        "home": "Home",
        "clear": "Clear",
        "reset": "Reset",
        "show": "Show",
        "hide": "Hide",
        "stamp": "Stamp",
        "fillstart": "FillStart",
        "fillend": "FillEnd",
        "circle": "Circle",
        "heading": "Heading",
        "setheading": "SetHeading",
        
        # GUI commands
        "messagebox": "MessageBox",
        "newdialogbox": "NewDialogBox",
        "inputbox": "InputBox",
        "choicebox": "ChoiceBox",
        "window": "Window",
        "button": "Button",
        "label": "Label",
        "image": "Image",
        "showwindow": "ShowWindow",
        "spacing": "Spacing",
        "separator": "Separator",
        "settheme": "SetTheme",
        "textfield": "TextField",
        "gettextfield": "GetTextField",
        "colorpicker": "ColorPicker",
        "colorpalette": "ColorPalette",
        "datepicker": "DatePicker",
        "colormap": "ColorMap",
        "infodialog": "InfoDialog",
        "warningdialog": "WarningDialog",
        "errordialog": "ErrorDialog",
        "confirmdialog": "ConfirmDialog",
        "fileopendialog": "FileOpenDialog",
        "filesavedialog": "FileSaveDialog",
        "folderdialog": "FolderDialog",
        "inputdialog": "InputDialog",
        "multichoicedialog": "MultiChoiceDialog",
        "numberdialog": "NumberDialog",
        "okcanceldialog": "OkCancelDialog",
    }
    return _CASE_MAP_CACHE

def _normalize_command(text):
    """
    Normalize command case for beginner-friendly input.
    
    Converts case-insensitive input like:
    - "terminal.echo(...)" -> "Terminal.Echo(...)"
    - "VARIABLES.NEW(...)" -> "Variables.New(...)"
    - "lists.GET(...)" -> "Lists.Get(...)"
    - "program.if(...)" -> "Program.If(...)"
    
    Args:
        text (str): Raw input that may have incorrect casing
        
    Returns:
        str: Normalized command with proper casing
    """
    case_map = _get_case_map()
    
    # Find the Category.Command part (before any parentheses, brackets, or spaces)
    match = re.match(r'([A-Za-z_]\w*)\.([A-Za-z_]\w*)', text)
    
    if not match:
        return text  # Return unchanged if no Category.Command found
    
    category_original = match.group(1)
    command_original = match.group(2)
    
    # Normalize to lowercase for lookup
    category_lower = category_original.lower()
    command_lower = command_original.lower()
    
    # Get proper casing
    category_proper = case_map.get(category_lower, category_original)
    command_proper = case_map.get(command_lower, command_original)
    
    # Replace in the original text
    normalized = text.replace(f"{category_original}.{command_original}", 
                            f"{category_proper}.{command_proper}", 1)
    
    return normalized

def execute_line(line):
    """
    Execute a single ICTL command.
    
    Args:
        line (str): The ICTL command to execute
        
    Raises:
        RuntimeErrorICTL: On execution errors
    """
    try:
        # Normalize command casing for beginner-friendly input
        line = _normalize_command(line)
        
        if line.startswith("Terminal.Echo"):
            value = eval_expr(extract_args(line)[0])
            terminal_echo(value)
            return

        if line.startswith("Terminal.Ask"):
            return terminal_ask(eval_expr(extract_args(line)[0]))

        if line.startswith("Variables.New"):
            # No-op: Variables.New() does nothing (kept for backward compatibility)
            return

        if line.startswith("Variables.") and "=" in line:
            name, expr = line.split("=", 1)
            var_name = name.replace("Variables.", "").strip()
            expr = expr.strip()

            # Normalize the right-hand side expression too
            expr = _normalize_command(expr)

            if expr.startswith("Terminal.Ask"):
                prompt = eval_expr(extract_args(expr)[0])
                variables[var_name] = terminal_ask(prompt)
            else:
                variables[var_name] = eval_expr(expr)

            return

        if line.startswith("Lists.") and "=" in line:
            # Handle list assignment: Lists.Name = [1, 2, 3]
            name, expr = line.split("=", 1)
            list_name = name.replace("Lists.", "").strip()
            expr = expr.strip()
            
            # Normalize the expression
            expr = _normalize_command(expr)
            
            # Parse and evaluate the list expression
            if expr.startswith("[") and expr.endswith("]"):
                # Extract list contents and evaluate nested expressions
                list_items = _parse_list_literal(expr, eval_expr)
                # Create or update the list
                from ictl_builtins.lists import lists
                lists[list_name] = list_items
            else:
                raise RuntimeErrorICTL(f"Lists assignment requires a list literal: Lists.{list_name} = [items]")
            return

        if line == "Program.BreakLoop":
            raise BreakSignal()

        if line == "Program.Continue":
            raise ContinueSignal()

        if line.startswith("Program.ExecuteKheer"):
            # Execute a user-defined Kheer function
            # Format: Program.ExecuteKheer(function_name)
            kheer_name = eval_expr(extract_args(line)[0])
            if kheer_name not in _kheers:
                raise RuntimeErrorICTL(f"Kheer '{kheer_name}' not defined")
            for item in _kheers[kheer_name]:
                run_item(item)
            return
        
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

        # Try handler-based commands (Math.*, Data.*, Lists.*, Program.*, Time.*, Terminal.*)
        if '.' in line and '(' in line:
            try:
                category, cmd, args = organize_input(line)
                result = ping_handler(category, cmd, args, eval_expr)
                # If the handler returns a value and we're in execute_line context,
                # just silently succeed (the result isn't printed unless in an Echo)
                return
            except (MathErrorICTL, VariableErrorICTL):
                # Re-raise specific errors
                raise
            except RuntimeErrorICTL as e:
                # If it fails due to parsing or handler error, re-raise instead of silently continuing
                raise

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

def _parse_list_literal(list_expr, eval_expr_func):
    """
    Parse a list literal and evaluate nested expressions.
    
    Args:
        list_expr (str): Expression like "[1, 2, Math.Eval(1+2)]"
        eval_expr_func: Reference to eval_expr for evaluating items
        
    Returns:
        list: Evaluated list items
        
    Raises:
        RuntimeErrorICTL: On parsing errors
    """
    # Remove outer brackets
    if not (list_expr.startswith("[") and list_expr.endswith("]")):
        raise RuntimeErrorICTL(f"Invalid list literal: {list_expr}")
    
    inside = list_expr[1:-1].strip()
    
    if not inside:
        return []
    
    # Split by comma but respect strings, parentheses, and brackets
    items = []
    current = ""
    in_string = False
    paren_depth = 0
    bracket_depth = 0
    escape_next = False
    
    for char in inside:
        if escape_next:
            current += char
            escape_next = False
            continue
            
        if char == '\\':
            escape_next = True
            current += char
            continue
            
        if char == '"' and not escape_next:
            in_string = not in_string
            current += char
        elif char == '(' and not in_string:
            paren_depth += 1
            current += char
        elif char == ')' and not in_string:
            paren_depth -= 1
            current += char
        elif char == '[' and not in_string:
            bracket_depth += 1
            current += char
        elif char == ']' and not in_string:
            bracket_depth -= 1
            current += char
        elif char == ',' and not in_string and paren_depth == 0 and bracket_depth == 0:
            if current.strip():
                # Evaluate the item
                items.append(eval_expr_func(current.strip()))
            current = ""
        else:
            current += char
    
    if current.strip():
        items.append(eval_expr_func(current.strip()))
    
    return items

def split_by_comma_respecting_quotes(text):
    """
    Split by comma but respect string literal boundaries, parentheses, and brackets.
    
    This ensures nested function calls like Data.Compare(1, 100) are not split.
    
    Args:
        text (str): The text to split
        
    Returns:
        list[str]: List of arguments
    """
    args = []
    current = ""
    in_string = False
    paren_count = 0
    bracket_count = 0
    escape_next = False
    
    for char in text:
        if escape_next:
            current += char
            escape_next = False
            continue
            
        if char == '\\':
            escape_next = True
            current += char
            continue
            
        if char == '"' and not escape_next:
            in_string = not in_string
            current += char
        elif char == '(' and not in_string:
            paren_count += 1
            current += char
        elif char == ')' and not in_string:
            paren_count -= 1
            current += char
        elif char == '[' and not in_string:
            bracket_count += 1
            current += char
        elif char == ']' and not in_string:
            bracket_count -= 1
            current += char
        elif char == ',' and not in_string and paren_count == 0 and bracket_count == 0:
            args.append(current.strip())
            current = ""
        else:
            current += char
    
    if current.strip():
        args.append(current.strip())
    
    return args

def organize_input(expr):
    """
    Parse an ICTL function call into (category, command, args).
    
    Handles case-insensitive input for beginner-friendly experience.
    
    Args:
        expr (str): The expression to parse (e.g., "Math.Random(1, 100)" or "math.random(1, 100)")
        
    Returns:
        tuple: (category: str, command: str, args: list[str])
        
    Raises:
        RuntimeErrorICTL: If the expression cannot be parsed
        
    Example:
        >>> organize_input("Math.Random(1, 100)")
        ("Math", "Random", ["1", "100"])
        >>> organize_input("math.random(1, 100)")
        ("Math", "Random", ["1", "100"])
    """
    expr = expr.strip()
    
    # Normalize the expression first
    expr = _normalize_command(expr)
    
    # Check if it's a function call (has . and ()
    if '.' not in expr or '(' not in expr:
        raise RuntimeErrorICTL(f"Invalid function call: '{expr}'")
    
    # Extract category (before first .)
    dot_idx = expr.find('.')
    category = expr[:dot_idx].strip()
    
    # Extract command (between . and ()
    paren_idx = expr.find('(')
    command = expr[dot_idx+1:paren_idx].strip()
    
    # Extract arguments
    args = extract_args(expr)
    
    return category, command, args

# Cache handler modules to avoid repeated imports
_HANDLER_CACHE = {}

def _get_handler(category):
    """Get a handler module with caching to avoid repeated imports."""
    if category not in _HANDLER_CACHE:
        if category == "Math":
            from handlers.MathHandler import handle as math_handle
            _HANDLER_CACHE[category] = math_handle
        elif category == "Data":
            from handlers.DataHandler import handle as data_handle
            _HANDLER_CACHE[category] = data_handle
        elif category == "Program":
            from handlers.ProgramHandler import handle as program_handle
            _HANDLER_CACHE[category] = program_handle
        elif category == "Terminal":
            from handlers.TerminalHandler import handle as terminal_handle
            _HANDLER_CACHE[category] = terminal_handle
        elif category == "Time":
            from handlers.TimeHandler import handle as time_handle
            _HANDLER_CACHE[category] = time_handle
        elif category == "Variables":
            from handlers.VariablesHandler import handle as variables_handle
            _HANDLER_CACHE[category] = variables_handle
        elif category == "Lists":
            from handlers.ListsHandler import handle as lists_handle
            _HANDLER_CACHE[category] = lists_handle
        elif category == "Kachua":
            from handlers.KachuaHandler import handle_kachua
            _HANDLER_CACHE[category] = handle_kachua
        elif category == "GUI":
            from handlers.GUIHandler import handle_gui
            _HANDLER_CACHE[category] = handle_gui
        else:
            return None
    return _HANDLER_CACHE[category]

def ping_handler(category, cmd, args, eval_expr_func):
    """
    Route a command to the appropriate handler module.
    
    Args:
        category (str): The handler category (e.g., "Math", "Data")
        cmd (str): The command name (e.g., "Random", "ToInt")
        args (list[str]): Raw string arguments (not yet evaluated)
        eval_expr_func: Reference to eval_expr for recursive evaluation
        
    Returns:
        Any: The result of the handler
        
    Raises:
        RuntimeErrorICTL: If the category is unknown
    """
    handler = _get_handler(category)
    if handler is None:
        raise RuntimeErrorICTL(f"Unknown command category: '{category}'")
    return handler(cmd, args, eval_expr_func)

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
        RuntimeErrorICTL: On other runtime errors
    """
    expr = expr.strip()
    
    # Handle empty expressions
    if not expr:
        raise RuntimeErrorICTL("Cannot evaluate empty expression")

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
    if expr.startswith('"') and expr.endswith('"') and expr.count('"') == 2:
        return expr[1:-1]

    # Variable (case-insensitive)
    # Check for Variables., variables., or VARIABLES.
    if expr.lower().startswith("variables."):
        # Normalize to proper case
        expr_normalized = _normalize_command(expr)
        var_name = expr_normalized.replace("Variables.", "")
        if var_name not in variables:
            raise VariableErrorICTL(f"Variable '{var_name}' is not defined")
        return variables[var_name]

    # ====================
    # Handler-based command routing
    # ====================
    # Check if this is a function call (Category.Command(args))
    if '.' in expr and '(' in expr:
        try:
            category, cmd, args = organize_input(expr)
            return ping_handler(category, cmd, args, eval_expr)
        except RuntimeErrorICTL:
            # If it's not a valid handler command, continue to number parsing
            pass
        except (MathErrorICTL, VariableErrorICTL):
            # Re-raise specific ICTL errors from handlers
            raise
    
    # =====================

    # Raw number (handles integers, negative numbers, and floats)
    try:
        if '.' in expr:
            return float(expr)
        else:
            return int(expr)
    except ValueError:
        pass

    # If all else fails, return as string
    return expr

# Below Section Commented - As not needed, math engine functions now directly handle Variables.* resolution
# (inside MathInternal.py). 
# Keeping it here for reference in case of future changes.:
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
