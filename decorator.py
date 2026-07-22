def my_decorator(func):
    def wrapper(name):
        print("Before")
        func(name)
        print("After")
    return wrapper


@my_decorator
def greet(name):
    print(f"Hello {name}")


greet("Alice")
