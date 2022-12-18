import math

MATH_FUNCS = {
    'sqrt': lambda args: math.sqrt(args[0]),
    'factorial': lambda args: math.factorial(args[0]),
    'sum': lambda args: sum(args),
    'exp': lambda args: math.exp(args[0]),
    'log': lambda args: math.log(args[0]),
    'pow': lambda args: math.pow(args[0], args[1]),
    'cos': lambda args: math.cos(args[0]),
    'sin': lambda args: math.sin(args[0]),
    'tan': lambda args: math.tan(args[0]),
}

OPERATOR_FUNCS = {
    '==': lambda args: args[0] == args[1],
    '!=': lambda args: args[0] != args[1],
    'and': lambda args: args[0] and args[1],
    'or': lambda args: args[0] or args[1],
    '<': lambda args: args[0] < args[1],
    '>': lambda args: args[0] > args[1],
    '+': lambda args: args[0] + args[1],
    '-': lambda args: args[0] - args[1],
    '*': lambda args: args[0] * args[1],
    '/': lambda args: args[0] / args[1],
}

DEBUG_FUNCS = {
    '__vars': lambda args: vars,
}

CORE_FUNCS = {
    'print': lambda args: print(args[0]),
    'sort': lambda args: sorted(args[0]),
}

FUNCS = { **MATH_FUNCS, **OPERATOR_FUNCS, **DEBUG_FUNCS, **CORE_FUNCS }