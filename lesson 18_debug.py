def debug(func):
    def wrapper(*args):
        print(f'Имя функции: {func.__name__}, значения: {args}')
        print('Результат выполнения  функции')
        func(*args)

    return wrapper


@debug
def ex(a,b):
    print(a + b)


ex(2, 4)
