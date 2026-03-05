# builtins/math.py
def math_eval(expr):
    try:
        # only allow digits and operators
        for c in expr:
            if c not in "0123456789+-*/(). ":
                raise RuntimeError

        return str(eval(expr, {"__builtins__": {}}))
    except:
        raise RuntimeError("[Math Error] Invalid Math.Eval expression")


def math_compare(a, symbol, b):
    a = float(a)
    b = float(b)

    if symbol == "==": return a == b
    if symbol == "!=": return a != b
    if symbol == ">": return a > b
    if symbol == "<": return a < b
    if symbol == ">=": return a >= b
    if symbol == "<=": return a <= b

    raise RuntimeError("[Math Error] Invalid comparison symbol")
