def outer_function(msg):
    message = msg
    def inner_function():
        print(message)
    return inner_function

my_func = outer_function("print this message")
my_func()