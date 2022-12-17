Symbol = str              # A Scheme Symbol is implemented as a Python str
Number = (int, float)     # A Scheme Number is implemented as a Python int or float
Atom   = (Symbol, Number) # A Scheme Atom is a Symbol or Number
List   = list             # A Scheme List is implemented as a Python list
Exp    = (Atom, List)     # A Scheme expression is an Atom or List
Env    = dict             # A Scheme environment (defined below) 
                          # is a mapping of {variable: value}

def tokenize(string: str):
    import re
    string = re.sub('\[.*?\]', '', string)
    return string.replace("(", " ( ").replace(")", " ) ").split()

def parse(program: str) -> Exp:
    "Read a Scheme expression from a string."
    return read_from_tokens(tokenize(program))

def read_from_tokens(tokens: list) -> Exp:
    "Read an expression from a sequence of tokens."
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0) # pop off ')'
        return L
    elif token == ')':
        raise SyntaxError('unexpected )')
    else:
        return atom(token)

def atom(token: str) -> Atom:
    "Numbers become numbers; every other token is a symbol."
    try: return int(token)
    except ValueError:
        try: return float(token)
        except ValueError:
            return Symbol(token)

def eval(x: Exp, vars: dict):
    import math

    funcs = {
        'print': lambda args: print(args[0]),
        'sort': lambda args: sorted(args[0]),
        'sqrt': lambda args: math.sqrt(args[0]),
        'factorial': lambda args: math.factorial(args[0]),
        'sum': lambda args: sum(args),
        'exp': lambda args: exp(args[0]),
        'log': lambda args: math.log(args[0]),
        'pow': lambda args: math.pow(args[0], args[1]),
        'cos': lambda args: math.cos(args[0]),
        'sin': lambda args: math.sin(args[0]),
        'tan': lambda args: math.tan(args[0]),
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
        '__vars': lambda args: vars,
    }

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