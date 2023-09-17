import functools


@functools.lru_cache
def fib_lru(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_lru(n - 1) + fib_lru(n - 2)


def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


def memoization(fib_fun):
    # To store the value
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        resul = fib_fun(*args)
        cache[args] = resul
        return resul

    return wrapper


# Without using LRU cache
fib_memo = memoization(fibonacci)

# Using LRU cache
fib_memo_lru = memoization(fib_lru)

if __name__ == "__main__":
    print(fib_memo(10))
    print(fib_memo_lru(10))
