# empty list                           # my_list = []
# list of integers                     # my_list = [1, 2, 3]
# list with mixed data types           # my_list = [1, "Hello", 3.4]
# nested list                          # my_list = ["mouse", [8, 4, 6], ['a']]


# Defining list
list1 = list([1, 3, 5])
print('The Normal list {0} '.format(list1))

# List Index
print('first value is {0} '.format(list1[0]))
print('second value is {0} '.format(list1[-2]))
print('from second to third value is {0} '.format(list1[1:3]))
print('first and third values is {0} and {1} '.format(list1[0], list1[2]))
print('from beginning to second value is {0} '.format(list1[:2]))

# Change element
list1[0] = 4
print('Here is the change {0}'.format(list1))

# add elements
list1.append(7)
print('added element {0}'.format(list1))
list1.extend([9,11,13])
print('added elements {0}'.format(list1))

# remove elements
list1.remove(13)                                        # (The element itself)
print('element deleted  : {0}'.format(list1))
list1.pop(5)                                            # (The Index Number)
print('element deleted  : {0}'.format(list1))
# list1.clear()                                         # removing everything
print('elements cleared : {0}'.format(list1))

# some tricks
# list1.sort()                                            # sort A-Z
# list1.reverse()                                         # reverse order
# list1.count()                                           # save to main list
# list1.insert(6, 1)                                      # add element in specific index
# print('list manipulated {0}'.format(list1))
# print(9 in list1)                                       # Membership test
# print(list1[1] is 3)                                     # validate test
