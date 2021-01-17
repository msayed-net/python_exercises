def outer_function():                       # Local NameSpace   |   a : Local name
    a = 20

    def inner_function():                   # Nested NameSpace  |   a : nested name
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10                                      # Global NameSpace  |   a : global name
outer_function()
print('a =', a)
