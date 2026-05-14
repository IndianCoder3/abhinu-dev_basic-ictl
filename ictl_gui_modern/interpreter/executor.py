"""
ICTL Code Executor - Uses actual ICTL interpreter
"""

import sys
import io
import tempfile
import os
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path


class ICTLExecutor:
    """Executes ICTL code using the actual ICTL parser and runtime"""
    
    def __init__(self):
        # Add parent directory to path to import ICTL modules
        parent_dir = str(Path(__file__).parent.parent.parent)
        if parent_dir not in sys.path:
            sys.path.insert(0, parent_dir)
        
        try:
            from parser import parse_file
            from runtime import run_program
            from error_handler import ICTLError
            
            self.parse_file = parse_file
            self.run_program = run_program
            self.ICTLError = ICTLError
            self.available = True
        except ImportError as e:
            print(f"Warning: Could not import ICTL modules: {e}")
            self.available = False
    
    def execute(self, code):
        """
        Execute ICTL code and return output
        
        Args:
            code (str): The ICTL code to execute
            
        Returns:
            str: Output from code execution
        """
        if not self.available:
            raise RuntimeError("ICTL interpreter not available. Make sure you're in the correct directory.")
        
        output_buffer = io.StringIO()
        error_buffer = io.StringIO()
        
        try:
            # Write code to temporary file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.ictl', delete=False) as f:
                f.write(code)
                temp_file = f.name
            
            try:
                # Redirect stdout/stderr
                with redirect_stdout(output_buffer), redirect_stderr(error_buffer):
                    # Parse and execute
                    program = self.parse_file(temp_file)
                    self.run_program(program)
                
                output = output_buffer.getvalue()
                errors = error_buffer.getvalue()
                
                if errors:
                    return errors
                
                return output if output else ""
                
            finally:
                # Clean up temp file
                try:
                    os.unlink(temp_file)
                except:
                    pass
                    
        except Exception as e:
            error_msg = str(e)
            if "not defined" in error_msg.lower() or "unknown" in error_msg.lower():
                return f"Error: {error_msg}"
            return f"Execution Error: {type(e).__name__}: {error_msg}"
        finally:
            output_buffer.close()
            error_buffer.close()
    
    def reset(self):
        """Reset the executor state"""
        pass
