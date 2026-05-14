# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# ictl_builtins/lists.py
"""
List management for ICTL.
Provides storage and manipulation of lists.
"""

# Global dictionary to store all lists
lists = {}

def create_list(name, items=None):
    """
    Create a new list.
    
    Args:
        name (str): Name of the list
        items (list): Initial items (optional)
        
    Raises:
        ValueError: If list already exists
    """
    if name in lists:
        raise ValueError(f"List '{name}' already exists")
    lists[name] = list(items) if items else []

def add_to_list(name, item):
    """
    Add an item to a list.
    
    Args:
        name (str): Name of the list
        item: Item to add
        
    Raises:
        ValueError: If list doesn't exist
    """
    if name not in lists:
        raise ValueError(f"List '{name}' does not exist. Use Lists.Create({name}) first.")
    lists[name].append(item)

def get_from_list(name, index):
    """
    Get an item from a list by index.
    
    Args:
        name (str): Name of the list
        index (int): Index of the item
        
    Returns:
        The item at that index
        
    Raises:
        ValueError: If list doesn't exist or index out of range
    """
    if name not in lists:
        raise ValueError(f"List '{name}' does not exist. Use Lists.Create({name}) first.")
    try:
        return lists[name][int(index)]
    except IndexError:
        raise ValueError(f"Index {index} out of range for list '{name}' (length: {len(lists[name])}). Indices start at 0.")

def remove_from_list(name, index):
    """
    Remove an item from a list by index.
    
    Args:
        name (str): Name of the list
        index (int): Index of the item to remove
        
    Raises:
        ValueError: If list doesn't exist or index out of range
    """
    if name not in lists:
        raise ValueError(f"List '{name}' does not exist")
    try:
        lists[name].pop(int(index))
    except IndexError:
        raise ValueError(f"Index {index} out of range for list '{name}'")

def list_length(name):
    """
    Get the length of a list.
    
    Args:
        name (str): Name of the list
        
    Returns:
        int: Length of the list
        
    Raises:
        ValueError: If list doesn't exist
    """
    if name not in lists:
        raise ValueError(f"List '{name}' does not exist")
    return len(lists[name])

def clear_list(name):
    """
    Clear all items from a list.
    
    Args:
        name (str): Name of the list
        
    Raises:
        ValueError: If list doesn't exist
    """
    if name not in lists:
        raise ValueError(f"List '{name}' does not exist")
    lists[name].clear()

def delete_list(name):
    """
    Delete a list entirely.
    
    Args:
        name (str): Name of the list
        
    Raises:
        ValueError: If list doesn't exist
    """
    if name not in lists:
        raise ValueError(f"List '{name}' does not exist")
    del lists[name]

def list_contains(name, item):
    """
    Check if a list contains an item.
    
    Args:
        name (str): Name of the list
        item: Item to check for
        
    Returns:
        bool: True if item is in list, False otherwise
        
    Raises:
        ValueError: If list doesn't exist
    """
    if name not in lists:
        raise ValueError(f"List '{name}' does not exist")
    return item in lists[name]

def get_list(name):
    """
    Get the entire list.
    
    Args:
        name (str): Name of the list
        
    Returns:
        list: The list
        
    Raises:
        ValueError: If list doesn't exist
    """
    if name not in lists:
        raise ValueError(f"List '{name}' does not exist")
    return lists[name]
