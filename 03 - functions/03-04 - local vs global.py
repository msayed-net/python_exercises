# global variable
x = 50


# def
def func(x):
    print('x is', x)
    x = 2                                                   # local variable
    print('Changed local x to', x)


# call
func(x)


# check global
print('x is still', x)