
# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
def generator(n:int):
    for number in range(0, n + 1, 2):
            yield number

res = generator(686)
print(next(res))
print(next(res))
print(next(res))

# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci_generator_2(n:int):
    n1, n2 = 0, 1
    while n1 <= n:
        yield n1
        n1, n2 = n2, n1+n2

fib_gen = fibonacci_generator_2(50)
for num in fib_gen:
    print(num)


# Реалізуйте ітератор для зворотного виведення елементів списку.
class ReverseIterator:
    def __init__(self, list_e:list):
        self.list_e = list_e
        self.index = len(list_e) - 1
        print('---  reverse  ---')

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.list_e[self.index]
        self.index -= 1
        return value

reverse_iter = ReverseIterator(['Kyiv', [7, 7, 9], 'America', 'Africa', 5])
for item in reverse_iter:
    print(item)



# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class PairNumbers:
    def __init__(self, n:int):
        self.n = n
        self.actual_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual_value > self.n:
            raise StopIteration
        value = self.actual_value
        self.actual_value += 2
        return value

pair = PairNumbers(41)
for num in pair:
    print(num)

from logger_error import logger
# Напишіть декоратор, який логує аргументи та результати викликаної функції.
def decorator(func):
    def wrapper(*args):
        logger.debug('before the function execution')
        result = func(*args)
        logger.debug(f'Function result: {result}')
        logger.debug('after the function execution')
        return result
    return wrapper

@decorator
def i_am_bald(value: bool):
    if value:
        return 'You are bold'
    return 'You are not bold'

i_am_bald(True)

# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

def exp_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f'Помилка {e}')
            return e
    return wrapper

@exp_handler
def get_len(value):
    return len(value)

get_len([1, 4, 3])
get_len(1)

