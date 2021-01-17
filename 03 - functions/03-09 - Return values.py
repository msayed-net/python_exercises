def plus(x=0, y=0):
    x = float(input('x : '))
    y = float(input('x : '))
    num = x + y
    print('{0} + {1} = {2}'.format(x, y, num))
    return x and y

plus()


def action(a=0, b=0):
    a = float(input('a : '))
    b = float(input('b : '))
    num = a * b
    print('{0} x {1} = {2}'.format(a, b, num))
    return a and b

action()