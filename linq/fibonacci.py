from enumerable import Enumerable


def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


Enumerable(fibonacci())\
    .where(lambda x: x % 3 == 0)\
    .select(lambda x: x ** 2 if x % 2 == 0 else x)\
    .take(5)\
    .select(lambda x: print(x, end=' '))\
    .to_list()
