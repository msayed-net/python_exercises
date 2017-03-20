# * : Tuple  |  ** : Dictionary


def total(a=5, *args, **kwargs):
    print('a', a)

    # iterate through all the items in tuple
    for single_item in args:
        print('single_item', single_item)

    # iterate through all the items in dictionary
    for first_part, second_part in kwargs.items():
        print(first_part, second_part)


total(10, 1, 2, 3, Ahmed=261548, Ali=356824, Mohamed=125687)
