# builtins/variables.py
variables = {}

def new_variable(name):
    if name in variables:
        raise RuntimeError(f"Variable {name} already exists")
    variables[name] = None
