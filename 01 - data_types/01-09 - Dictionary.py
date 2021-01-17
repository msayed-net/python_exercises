# empty dictionary                              # my_dict = {}
# dictionary with integer keys                  # my_dict = {1: 'apple', 2: 'ball'}
# dictionary with mixed keys                    # my_dict = {'name': 'John', 1: [2, 4, 3]}
# using dict()                                  # my_dict = dict({1:'apple', 2:'ball'})
# from sequence having each item as a pair      # my_dict = dict([(1,'apple'), (2,'ball')])


# Defining Dictionary
ahmed_dict = dict({'name' : 'Ahmed', 'age' : 22, 'address' : 'Marg'})
print('This is default dictionary for ahmed khaled, \n{0}'.format(ahmed_dict))       # whole dictionary
# print('his name is    : {0}'.format(ahmed_dict.get('name')))                       # Name Value
# print('his age is     : {0}'.format(ahmed_dict.get('age')))                        # Age Value
# print('his address is : {0}'.format(ahmed_dict.get('address')))                    # Address Value

# Change element
ahmed_dict['age'] = 23
print('his age is : {0}'.format(ahmed_dict.get('age')))

# Add element
ahmed_dict['Hobby'] = 'GIS'
print('This is default dictionary for ahmed khaled, \n{0}'.format(ahmed_dict))

# remove elements
ahmed_dict.pop('age')                                          # (The key)
print('element deleted {0}'.format(ahmed_dict))
ahmed_dict.clear()                                             # removing everything
print('dictionary cleared {0}'.format(ahmed_dict))

# some tricks
# ahmed_dict.items()                                           # save to main list
