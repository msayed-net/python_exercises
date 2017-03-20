# iterate over a sequence (list, tuple, string) or other iterable objects " travesal

# for <iter_variable> in <iterable>:
#                 Body of for


# Example 4
print(range(10))                                    # output : range(0, 10)
print(list(range(10)))                              # output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(2,20,3)))                          # [2, 5, 8, 11, 14, 17]

Doctors = ['Mona','Gehan','Wafik','Omnia']
for i in range(len(Doctors)):
    print('Ahmed like Dr',Doctors[i])