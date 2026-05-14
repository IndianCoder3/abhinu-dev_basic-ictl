# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# handlers/ListsHandler.py
from ictl_builtins.lists import (
    create_list, add_to_list, get_from_list, remove_from_list,
    list_length, clear_list, delete_list, list_contains, lists, get_list
)
from error_handler import RuntimeErrorICTL

def handle(cmd, args, eval_expr):
    """
    Handle Lists.* commands.
    
    Args:
        cmd (str): The command name (e.g., "Create", "Add", "Get")
        args (list[str]): Raw string arguments
        eval_expr: Reference to the eval_expr function for recursive evaluation
        
    Returns:
        Any: The result of the command
        
    Raises:
        RuntimeErrorICTL: On errors
    """
    try:
        if cmd == "Create":
            if len(args) < 1:
                raise RuntimeErrorICTL("Lists.Create requires at least 1 argument: Lists.Create(name) or Lists.Create(name, [items])")
            name = args[0]
            # Second argument is optional list of items
            if len(args) > 1:
                items_expr = args[1]
                # Try to evaluate as a list-like expression or variable
                items = eval_expr(items_expr)
                if not isinstance(items, list):
                    # If it's a single value, wrap it in a list
                    items = [items]
                create_list(name, items)
            else:
                create_list(name)
            return None
            
        elif cmd == "Add" or cmd == "Push":
            if len(args) != 2:
                raise RuntimeErrorICTL(f"Lists.{cmd} requires 2 arguments: Lists.{cmd}(name, item)")
            name = args[0]
            item = eval_expr(args[1])
            add_to_list(name, item)
            return None
            
        elif cmd == "Get":
            if len(args) != 2:
                raise RuntimeErrorICTL("Lists.Get requires 2 arguments: Lists.Get(name, index)")
            name = args[0]
            index = eval_expr(args[1])
            return get_from_list(name, index)
            
        elif cmd == "Pop":
            # Pop without index removes last item
            if len(args) < 1:
                raise RuntimeErrorICTL(f"Lists.{cmd} requires at least 1 argument: Lists.{cmd}(name)")
            name = args[0]
            # Remove last item (typical pop behavior)
            if list_length(name) > 0:
                remove_from_list(name, list_length(name) - 1)
            return None
            
        elif cmd == "Length":
            if len(args) != 1:
                raise RuntimeErrorICTL("Lists.Length requires 1 argument: Lists.Length(name)")
            name = args[0]
            return list_length(name)
            
        elif cmd == "Clear":
            if len(args) != 1:
                raise RuntimeErrorICTL("Lists.Clear requires 1 argument: Lists.Clear(name)")
            name = args[0]
            clear_list(name)
            return None
            
        elif cmd == "Delete":
            if len(args) != 1:
                raise RuntimeErrorICTL("Lists.Delete requires 1 argument: Lists.Delete(name)")
            name = args[0]
            delete_list(name)
            return None
            
        elif cmd == "Contains":
            if len(args) != 2:
                raise RuntimeErrorICTL("Lists.Contains requires 2 arguments: Lists.Contains(name, item)")
            name = args[0]
            item = eval_expr(args[1])
            return list_contains(name, item)
            
        elif cmd == "Set":
            if len(args) < 1:
                raise RuntimeErrorICTL("Lists.Set requires at least 1 argument: Lists.Set(name, ...items)")
            name = args[0]
            # If additional args provided, set items to those args
            if len(args) > 1:
                items = [eval_expr(arg) for arg in args[1:]]
            else:
                # If only name provided, create empty list
                items = []
            # Directly set the list in the global lists dictionary
            lists[name] = items
            return None
            
        else:
            raise RuntimeErrorICTL(f"Unknown Lists command: {cmd}")
            
    except RuntimeErrorICTL:
        raise
    except ValueError as e:
        raise RuntimeErrorICTL(f"Lists.{cmd} error: {str(e)}")
    except Exception as e:
        raise RuntimeErrorICTL(f"Lists.{cmd} error: {str(e)}")
