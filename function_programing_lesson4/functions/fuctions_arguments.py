# Позиционные аргументы, обязательные
def example_pos(a, b):
    print("a:", a, "b:", b)


# Именовыные (имеющие значение по умалчанию)
def example_name(a=1, b=1):
    pass


# Комбинированая сигнатура
def foo(a, b=1):
    return a + b


# Передача по имени
example_pos(b=10, a=12)


def any_pos_args(*args):
    print(args)


any_pos_args(1, 2, 3, 4)


# Функция принимающая любое количество именованных аргументов

def any_kwargs(**kwargs):
    print(kwargs)


any_kwargs(a=2, b=3, d=4, g=3)
