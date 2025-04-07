import math as m
from pytexit import py2tex

class Evaluator():

    def __init__(self, expr):
        self.__BIN = {'__builtins__': None}
        self.__math_allowed = {'e': m.e, 'pi': m.pi, 'tau': m.tau, 'abs': abs, 'factorial': m.factorial, 'exp': m.exp, 'pow': m.pow,'sqrt': m.sqrt,
                   'ln': m.log, 'log': m.log, 'log2': m.log2, 'log10': m.log10, 'acos': m.acos,'asin': m.asin, 'atan': m.atan, 'cos': m.cos,
                   'sin': m.sin, 'tan': m.tan, 'acosh': m.acosh, 'asinh': m.asinh, 'atanh': m.atanh,'cosh': m.cosh, 'sinh': m.sinh, 'tanh': m.tanh}
        self.expr = expr.replace("^","**")

    def evaluate(self, x):
        self.__math_allowed['x'] = x
        return eval(self.expr, self.__BIN, self.__math_allowed)

    def parse_arguments(self, *args):
        parsed = [0]*len(args)
        idx = 0
        for i in args:
            if (type(i) is str):
                x = i.replace('pi', str(m.pi)).replace('e', str(m.e))
                parsed[idx] = eval(x, {}, {})
            idx += 1
        return parsed[0] if len(args) == 1 else parsed

    def get_latex(self):
        eq = py2tex(self.expr)
        return eq[2:-2]
