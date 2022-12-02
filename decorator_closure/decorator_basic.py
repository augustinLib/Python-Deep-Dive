def logger(func):
    def wrapper(arg):
        print("function start")
        func(arg)
        print("function end")

    return wrapper


@logger
def say_hello(name):
    print("Hello", name)


@logger
def say_bye(name):
    print("Bye", name)
