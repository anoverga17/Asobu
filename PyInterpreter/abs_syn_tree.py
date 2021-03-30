from typing import List, Dict, Union

class Value:
    """A terminal value in an expression

    The type of a literal must be one of:
        - Number
        - Bool
        - String
        - Closure
    """
    _type: str
    _value: Union[float, bool, str]

    def __init__(self, value: Union[float, bool, str]) -> None:
        if isinstance(value, float):
            self._type = 'Number'
        elif isinstance(value, bool):
            self._type = 'Bool'
        elif isinstance(value, str):
            self._type = 'String'
        else:
            self._type = 'Undefined'
        self._value = value

    def get_value(self) -> Union[float, bool, str]:
        return self._value

    def get_type(self) -> str:
        return self._type

    def __str__(self):
        return str(self._value)

class Expr:
    def eval(self, env: Dict[str, Value]) -> Value:
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

class Literal(Expr):
    def __init__(self, value: Value):
        self._value = value

    def eval(self, env: Dict[str, Value]) -> Value:
        return self._value

    def __str__(self):
        return str(self._value)

class Id(Expr):
    def __init__(self, id: str):
        self._id = id

    def eval(self, env: Dict[str, Value]) -> Value:
        if self._id in env:
            return env[self._id]
        else:
            print(f"Evaluation Error: variable {self._id} not defined")
            quit()

    def __str__(self):
        return self._id

class Builtin(Expr):
    def __init__(self, op: str, args: List[Expr]) -> None:
        self._op = op
        self._args = args

    def eval(self, env: Dict[str, Value]) -> Value:
        bin_ops = {'+', '-', '/', '*'}
        if self._op in bin_ops:
            sub_expr1 = self._args[0].eval(env)
            sub_expr2 = self._args[1].eval(env)
            if sub_expr2.get_type() == 'Number' and sub_expr1.get_type() == 'Number':
                if self._op == '+':
                    return Value(sub_expr1.get_value() + sub_expr2.get_value())
                elif self._op == '-':
                    return Value(sub_expr1.get_value() - sub_expr2.get_value())
                elif self._op == '*':
                    return Value(sub_expr1.get_value() * sub_expr2.get_value())
                elif self._op == '/' and sub_expr2.get_value() == 0:
                    print("Zero Division Error")
                    return Value(0)
                else:
                    return Value(sub_expr1.get_value() / sub_expr2.get_value())
            print(f"Evaluation Error: cannot evaluate {sub_expr1.get_value()} {self._op} {sub_expr2.get_value()}")
            quit()
        else:
            print(f"Evaluation Error: operator {self._op} not defined")
            quit()

    def __str__(self):
        out = ''
        for i in range(len(self._args) - 1):
            out += f'{str(self._args[i])} {self._op} '
        out += f'{str(self._args[-1])}'
        return out

class Lambda(Expr):
    def __init__(self, id: str, expr: Expr) -> None:
        self._id = id
        self._expr = expr

    def eval(self, env: Dict[str, Value]) -> Value:
        return Closure(self._id, self._expr, env.copy())

    def __str__(self):
        return 'lambda ' + self._id + ' {' + str(self._expr) + '}'


class Closure(Value):
    """A closure
    """
    _id: str
    _expr: Expr
    _env: Dict[str, Value]

    def __init__(self, id: str, expr: Expr, env: Dict[str, Value]) -> None:
        super().__init__('Undefined')
        self._type = 'Closure'
        self._id = id
        self._expr = expr
        self._env = env

    def apply_closure(self, arg: Value) -> Value:
        self._env[self._id] = arg
        return self._expr.eval(self._env)

    def __str__(self):
        return 'Closure(lambda ' + self._id + ' {' + str(self._expr) + '})'

class Apply(Expr):
    def __init__(self, fn: Expr, arg: Expr) -> None:
        self._fn = fn
        self._arg = arg

    def eval(self, env: Dict[str, Value]) -> Value:
        function = self._fn.eval(env)
        arg = self._arg.eval(env)
        if function.get_type() != 'Closure':
            print(f'{function.get_value()} not an applicable expression')
            quit()
        return function.apply_closure(arg)
