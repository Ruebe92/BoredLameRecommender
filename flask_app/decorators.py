### Make a simple decorator that modified any function -> e.g. run that function twice


def do_twice(f):
    def inner_function():
        f()
        f()

    return inner_function


@do_twice
def hello():
    print("Hello!")
