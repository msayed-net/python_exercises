# global
x = 50


# def
def func():
    global x                                        # global declaration
    print('x is', x)
    x = 2                                           # global variable
    print('Changed global x to', x)


# call
func()


# check global
print('Value of x is', x)