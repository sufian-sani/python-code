x = 100
def some_function():
    global x
    x = x+50
    print('Inside = ',x)

some_function()
print('Outside = ',x)