def debug(func):
    def wrapper(*args):
        print(f'Имя функции: {func.__name__}, значения: {args}')
        print('Результат выполнения  функции')
        func()

    return wrapper


@debug
def ex(*args):
    print(sum(args))


ex(2, 4)