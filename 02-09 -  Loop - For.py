# iterate over a sequence (list, tuple, string) or other iterable objects " travesal

# for <iter_variable> in <iterable>:
#                 Body of for


# Example 2
alist = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,0,0,1,1,1,1,1,0,0,1,1,1],
[1,1,0,0,1,1,1,1,1,0,0,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,0,1,1,1,1,1,1,1],
[1,1,1,1,1,1,0,1,1,1,1,1,1,1],
[1,1,1,1,1,0,0,0,1,1,1,1,1,1],
[1,0,1,1,1,1,1,1,1,1,1,1,0,1],
[1,0,1,1,1,1,1,1,1,1,1,1,0,1],
[1,1,0,0,0,0,0,0,0,0,0,0,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

for clist in alist:
    for number in clist:
        print(number, end=' ')
    print()