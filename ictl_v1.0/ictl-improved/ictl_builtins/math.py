import math
import operator
from ictl_builtins.variables import variables

OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow,
}

PREC = {"+":1,"-":1,"*":2,"/":2,"^":3}

FUNCS = {
    "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "asin": math.asin, "acos": math.acos, "atan": math.atan,
    "sinh": math.sinh, "cosh": math.cosh, "tanh": math.tanh,
    "log": math.log, "log10": math.log10, "exp": math.exp,
    "abs": abs, "floor": math.floor, "ceil": math.ceil,
    "round": round, "degrees": math.degrees, "radians": math.radians,
}

CACHE = {}

# ------------------------
# Tokenizer (fast)
# ------------------------

def tokenize(expr):
    tokens = []
    i = 0
    prev = None

    while i < len(expr):
        c = expr[i]

        # number (with unary minus)
        if c.isdigit() or c == "." or (
            c == "-" and prev in (None,"(","+","-","*","/","^")
        ):
            num = c
            i += 1
            while i < len(expr) and (expr[i].isdigit() or expr[i] == "."):
                num += expr[i]
                i += 1
            tokens.append(("num", float(num)))
            prev = "num"
            continue

        # Variables.x
        if expr.startswith("Variables.", i):
            i += 10
            name = ""
            while i < len(expr) and (expr[i].isalnum() or expr[i]=="_"):
                name += expr[i]
                i += 1
            tokens.append(("var", name))
            prev = "var"
            continue

        # function
        if c.isalpha():
            name = c
            i += 1
            while i < len(expr) and expr[i].isalpha():
                name += expr[i]
                i += 1
            tokens.append(name)
            prev = "func"
            continue

        if c.strip():
            tokens.append(c)
            prev = c

        i += 1

    return tokens


# ------------------------
# Parser
# ------------------------

def shunting_yard(tokens):
    out, stack = [], []

    for token in tokens:

        if isinstance(token, tuple):
            out.append(token)

        elif token in FUNCS:
            stack.append(token)

        elif token in OPS:
            while stack and stack[-1] in OPS and PREC[stack[-1]] >= PREC[token]:
                out.append(stack.pop())
            stack.append(token)

        elif token == "(":
            stack.append(token)

        elif token == ")":
            while stack and stack[-1] != "(":
                out.append(stack.pop())
            stack.pop()

            if stack and stack[-1] in FUNCS:
                out.append(stack.pop())

    while stack:
        out.append(stack.pop())

    return out


# ------------------------
# Evaluator
# ------------------------

def eval_rpn(rpn):
    stack = []

    for token in rpn:

        if isinstance(token, tuple):

            t, v = token

            if t == "num":
                stack.append(v)

            elif t == "var":
                if v not in variables:
                    raise RuntimeError(f"[Math Error] Variable '{v}' not defined")
                stack.append(float(variables[v]))

        elif token in OPS:
            b = stack.pop()
            a = stack.pop()
            stack.append(OPS[token](a,b))

        elif token in FUNCS:
            stack.append(FUNCS[token](stack.pop()))

    return stack[0]


# ------------------------
# Main API
# ------------------------

def math_eval(expr):

    if expr not in CACHE:
        tokens = tokenize(expr)
        CACHE[expr] = shunting_yard(tokens)

    try:
        return str(eval_rpn(CACHE[expr]))
    except Exception:
        raise RuntimeError(f"[Math Error] Invalid Math.Eval expression: {expr}")


def math_compare(a,symbol,b):

    a,b = float(a),float(b)

    if symbol=="==": return a==b
    if symbol=="!=": return a!=b
    if symbol==">": return a>b
    if symbol=="<": return a<b
    if symbol==">=": return a>=b
    if symbol=="<=": return a<=b

    raise RuntimeError("[Math Error] Invalid comparison symbol")