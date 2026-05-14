import os
from setuptools import setup, Extension
from Cython.Build import cythonize

# 1. Define files to ignore (don't compile these)
EXCLUDE_FILES = {"main.py", "app.py", "setup.py"}

def get_ext_modules():
    """Scan workspace and generate list of Python files to compile with Cython."""
    extensions = []
    for root, dirs, files in os.walk("."):
        # Skip build directories to avoid recursion issues
        if any(skip in root for skip in ["build", "dist", ".git", "__pycache__"]):
            continue
            
        for file in files:
            if file.endswith(".py") and file not in EXCLUDE_FILES:
                path = os.path.join(root, file)
                # Create module name (e.g., "utils.helpers")
                module_name = path.replace(".py", "").replace(os.sep, ".").strip(".")
                extensions.append(path)
    return extensions

setup(
    ext_modules=cythonize(
        get_ext_modules(),
        compiler_directives={'language_level': "3"},
        exclude=list(EXCLUDE_FILES)
    )
)
