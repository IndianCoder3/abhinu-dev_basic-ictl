# Copyright (C) 2026-Present IndianCoder3
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# ictl_builtins/turtle_graphics.py
import turtle
from error_handler import RuntimeErrorICTL

# Global turtle screen and turtle instance
_screen = None
_turtle = None

def _init_turtle():
    """Initialize the turtle graphics screen and turtle."""
    global _screen, _turtle
    if _screen is None:
        _screen = turtle.Screen()
        _screen.setup(width=800, height=600)
        _screen.title("Kachua - ICTL Turtle Graphics")
        _turtle = turtle.Turtle()
        _turtle.speed(0)
    return _turtle

def kachua_forward(distance):
    """Move turtle forward by distance units."""
    try:
        t = _init_turtle()
        t.forward(float(distance))
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.Forward error: {e}")

def kachua_backward(distance):
    """Move turtle backward by distance units."""
    try:
        t = _init_turtle()
        t.backward(float(distance))
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.Backward error: {e}")

def kachua_right(angle):
    """Turn turtle right by angle degrees."""
    try:
        t = _init_turtle()
        t.right(float(angle))
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.Right error: {e}")

def kachua_left(angle):
    """Turn turtle left by angle degrees."""
    try:
        t = _init_turtle()
        t.left(float(angle))
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.Left error: {e}")

def kachua_pen_up():
    """Lift the pen up (don't draw)."""
    try:
        t = _init_turtle()
        t.penup()
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.PenUp error: {e}")

def kachua_pen_down():
    """Put the pen down (start drawing)."""
    try:
        t = _init_turtle()
        t.pendown()
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.PenDown error: {e}")

def kachua_set_color(color):
    """Set pen color."""
    try:
        t = _init_turtle()
        t.pencolor(str(color))
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.SetColor error: {e}")

def kachua_set_pen_width(width):
    """Set pen width/thickness."""
    try:
        t = _init_turtle()
        t.pensize(float(width))
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.SetPenWidth error: {e}")

def kachua_set_speed(speed):
    """Set drawing speed (0-10, 0=fastest)."""
    try:
        t = _init_turtle()
        t.speed(float(speed))
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.SetSpeed error: {e}")

def kachua_go_to(x, y):
    """Move turtle to position (x, y)."""
    try:
        t = _init_turtle()
        t.goto(float(x), float(y))
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.GoTo error: {e}")

def kachua_home():
    """Move turtle back to home position (0, 0)."""
    try:
        t = _init_turtle()
        t.home()
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.Home error: {e}")

def kachua_clear():
    """Clear all drawings from the screen."""
    try:
        t = _init_turtle()
        t.clear()
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.Clear error: {e}")

def kachua_reset():
    """Reset turtle to default state."""
    try:
        t = _init_turtle()
        t.reset()
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.Reset error: {e}")

def kachua_show_turtle():
    """Show the turtle cursor."""
    try:
        t = _init_turtle()
        t.showturtle()
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.Show error: {e}")

def kachua_hide_turtle():
    """Hide the turtle cursor."""
    try:
        t = _init_turtle()
        t.hideturtle()
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.Hide error: {e}")

def kachua_show():
    """Display the graphics window."""
    try:
        global _screen
        _screen = _init_turtle().getscreen()
        if _screen:
            _screen.update()
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.Show error: {e}")

def kachua_stamp():
    """Stamp a copy of the turtle at current position."""
    try:
        t = _init_turtle()
        return t.stamp()
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.Stamp error: {e}")

def kachua_fill_start():
    """Start a fill region."""
    try:
        t = _init_turtle()
        t.begin_fill()
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.FillStart error: {e}")

def kachua_fill_end():
    """End a fill region."""
    try:
        t = _init_turtle()
        t.end_fill()
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.FillEnd error: {e}")

def kachua_circle(radius):
    """Draw a circle with given radius."""
    try:
        t = _init_turtle()
        t.circle(float(radius))
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.Circle error: {e}")

def kachua_heading():
    """Get current heading direction."""
    try:
        t = _init_turtle()
        return t.heading()
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.Heading error: {e}")

def kachua_set_heading(angle):
    """Set heading direction."""
    try:
        t = _init_turtle()
        t.setheading(float(angle))
    except Exception as e:
        raise RuntimeErrorICTL(f"Kachua.SetHeading error: {e}")
