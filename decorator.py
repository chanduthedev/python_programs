# decorator definition
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        dec_str = f"Sum of {args[0]} and {args[1]} is "
        res = func(*args, **kwargs)
        return dec_str + str(res)

    return wrapper


@decorator_with_args
def add_with_args(n1, n2):
    return n1 + n2


# Decorator definition
def decorator_func(func):
    def wrapper():
        decor_str = "Sum of 2 and 3 is "
        res = func()
        return decor_str + str(res)

    return wrapper


# Decorator usage
@decorator_func
def add_num():
    return 2 + 3


if __name__ == "__main__":
    print(add_num())
    print(add_with_args(2, 3))
