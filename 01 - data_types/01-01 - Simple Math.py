# Python program to do simple math methods


# Numbers
num1 = float(input('input first number : '))
num2 = float(input('input second number : '))


# Operations
Output1 = num1 + num2
Output2 = num1 - num2
Output3 = num1 / num2
Output4 = num1 * num2
Output5 = num1 ** num2


# Executing
print('{0} + {1} = {2}'.format(num1, num2, Output1))
print('{0} - {1} = {2}'.format(num1, num2, Output2))
print('{0} / {1} = {2}'.format(num1, num2, Output3))
print('{0} * {1} = {2}'.format(num1, num2, Output4))
print('{0} ** {1} = {2}'.format(num1, num2, Output5))

# Transformation
num1, num2 = num2, num1

# Reversed operations
Output6 = num1 + num2
Output7 = num1 - num2
Output8 = num1 / num2
Output9 = num1 * num2
Output10 = num1 ** num2

# Executing
print('This is the reverse : num1 = num2 , num2 = num1')
print('{0} + {1} = {2}'.format(num1, num2, Output6))
print('{0} - {1} = {2}'.format(num1, num2, Output7))
print('{0} / {1} = {2}'.format(num1, num2, Output8))
print('{0} * {1} = {2}'.format(num1, num2, Output9))
print('{0} ** {1} = {2}'.format(num1, num2, Output10))