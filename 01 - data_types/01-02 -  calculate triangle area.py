# Python program to calculate triangle area


# Numbers
a = float(input('first side : '))
b = float(input('second side: '))
c = float(input('third side : '))


# Operations
s = ( a + b + c)                                          # perimeter
s_s = ( a + b + c) / int(2)                               # semi-perimeter
area = (s_s*(s_s-a)*(s_s-b)*(s_s-c)) ** float(0.5)        # area


# Executing
print('The perimeter is {0} '.format(s))
print('The area is {0} '.format(area))