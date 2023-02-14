def smart_divide(func):
    def inner_function(a,b):
        # print(f"Dividing {} by {}"a,b)
        print("Dividing {} by {}".format(a,b))
        if b == 0:
            print("Can't divide by zero")
            return
        return func(a,b)
    return inner_function

@smart_divide
def division(a,b):
    print(a/b)

division(4,0)