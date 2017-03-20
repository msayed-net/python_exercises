# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

# iterate through it using next()

# prints 4
print(next(my_iter))

# prints 7
print(next(my_iter))

# next(obj) is same as obj.__next__()

# prints 0
print(my_iter.__next__())

# prints 3
print(my_iter.__next__())

# This will raise error, no items left
next(my_iter)

# for statement
# for element in my_list:
#     print(element)
