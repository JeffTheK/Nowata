from .ntypes import *
from .nparser import *
from .stdlib import FUNCS
import sys

def eval(x: Exp, vars: dict):
    import math

    funcs = FUNCS

    if isinstance(x, Symbol):
        return vars[x]
    elif isinstance(x, Number):
        return x
    elif x[0] == 'if':
        (_, test, conseq, alt) = x
        exp = (conseq if eval(test, vars) else alt)
        return eval(exp, vars)
    elif x[0] == 'str':
        return " ".join(x[1:])
    elif x[0] == 'var':
        (_, symbol, exp) = x
        vars[symbol] = eval(exp, vars)
    elif x[0] == 'begin':
        for y in x[1:]:
            eval(y, vars)
    elif x[0] == 'while':
        while eval(x[1], vars) != False:
            for exp in x[2:]:
                eval(exp, vars)
    elif x[0] == 'list':
        out = []
        out.extend(x[1:])
        return out
    elif x[0] == 'input':
        return input()
    elif x[0] == 'foreach':
        var_name = x[1]
        collection = x[2]
        for i in range(len(collection)):
            vars[var_name] = collection[i]
            for expr in x[3:]:
                eval(expr, vars)
    elif x[0] == 'func':
        name = x[1]
        body = x[2:]
        funcs[name] = lambda args, body=body: [eval(y, vars) for y in body]
    else:
        func = funcs[x[0]]
        args = [eval(arg, vars) for arg in x[1:]]
        return func(args)

def exec_file(file_path: str):
    file = open(file_path, 'r')
    text = file.read()
    expressions = parse(text)
    eval(expressions, vars={})
    file.close()

def run():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        exec_file(file_path)