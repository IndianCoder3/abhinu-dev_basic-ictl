# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# handlers/KachuaHandler.py
from ictl_builtins.turtle_graphics import (
    kachua_forward, kachua_backward, kachua_right, kachua_left,
    kachua_pen_up, kachua_pen_down, kachua_set_color, kachua_set_pen_width,
    kachua_set_speed, kachua_go_to, kachua_home, kachua_clear, kachua_reset,
    kachua_show_turtle, kachua_hide_turtle, kachua_show, kachua_stamp,
    kachua_fill_start, kachua_fill_end, kachua_circle, kachua_heading,
    kachua_set_heading
)
from error_handler import RuntimeErrorICTL

def handle_kachua(command, args, eval_expr):
    """
    Route Kachua (turtle graphics) commands to appropriate functions.
    
    Example:
        Kachua.Forward(100)
        Kachua.Right(90)
        Kachua.SetColor("red")
    """
    command_lower = command.lower()
    
    commands = {
        "forward": kachua_forward,
        "backward": kachua_backward,
        "right": kachua_right,
        "left": kachua_left,
        "penup": kachua_pen_up,
        "pendown": kachua_pen_down,
        "setcolor": kachua_set_color,
        "setpenwidth": kachua_set_pen_width,
        "setspeed": kachua_set_speed,
        "goto": kachua_go_to,
        "home": kachua_home,
        "clear": kachua_clear,
        "reset": kachua_reset,
        "show": kachua_show,
        "hide": kachua_hide_turtle,
        "stamp": kachua_stamp,
        "fillstart": kachua_fill_start,
        "fillend": kachua_fill_end,
        "circle": kachua_circle,
        "heading": kachua_heading,
        "setheading": kachua_set_heading,
    }
    
    if command_lower not in commands:
        available = ", ".join(sorted(commands.keys()))
        raise RuntimeErrorICTL(f"Unknown Kachua command: {command}\nAvailable: {available}")
    
    # Evaluate arguments
    evaluated_args = [eval_expr(arg) for arg in args]
    
    # Call the appropriate function
    return commands[command_lower](*evaluated_args)
