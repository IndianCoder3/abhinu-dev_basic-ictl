# builtins/time.py
import time
from datetime import datetime

def time_wait(seconds):
    """
    Wait for a specified number of seconds.
    
    Args:
        seconds (int or float): Number of seconds to wait
        
    Raises:
        RuntimeError: If seconds is not a valid number
    """
    try:
        seconds = float(seconds)
        if seconds < 0:
            raise RuntimeError("[Time Error] Seconds cannot be negative")
        time.sleep(seconds)
    except (ValueError, TypeError):
        raise RuntimeError(f"[Time Error] Invalid wait time: {seconds}")

def time_current(format_str):
    """
    Get the current time in the specified format.
    
    Args:
        format_str (str): Format string for the time (e.g., "HH:mm:ss tt", "YYYY-MM-DD")
        
    Returns:
        str: The current time formatted according to the format string
        
    Raises:
        RuntimeError: If the format string is invalid
    """
    try:
        # Convert ICTL-style format to Python strftime format
        # ICTL uses: HH (hour 24), mm (minutes), ss (seconds), tt (AM/PM), etc.
        # Python uses: %H (hour 24), %M (minutes), %S (seconds), %p (AM/PM), etc.
        
        format_map = {
            'YYYY': '%Y',  # 4-digit year
            'YY': '%y',    # 2-digit year
            'MM': '%m',    # 2-digit month
            'M': '%-m',    # Month (no leading zero, Windows doesn't support this)
            'DD': '%d',    # 2-digit day
            'D': '%-d',    # Day (no leading zero)
            'HH': '%H',    # Hour (24-hour)
            'hh': '%I',    # Hour (12-hour)
            'mm': '%M',    # Minutes
            'm': '%-M',    # Minutes (no leading zero)
            'ss': '%S',    # Seconds
            's': '%-S',    # Seconds (no leading zero)
            'tt': '%p',    # AM/PM
        }
        
        python_format = format_str
        for ictl_fmt, py_fmt in format_map.items():
            python_format = python_format.replace(ictl_fmt, py_fmt)
        
        # Handle Windows compatibility (doesn't support %-M, %-d, etc.)
        # Convert these to their full versions for now
        python_format = python_format.replace('%-m', '%m').replace('%-d', '%d')
        python_format = python_format.replace('%-M', '%M').replace('%-S', '%S')
        
        current_time = datetime.now()
        return current_time.strftime(python_format)
    except Exception as e:
        raise RuntimeError(f"[Time Error] Invalid format string '{format_str}': {str(e)}")
