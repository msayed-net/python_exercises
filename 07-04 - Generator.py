# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

# sample 1
a = my_gen()
print(next(a))
print(next(a))
print(next(a))
print(next(a))                              # (4) _ doesn't exist


# sample 2
# for item in my_gen():
#     print(item)
