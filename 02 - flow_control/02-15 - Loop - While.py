# iterate over a sequence (list, tuple, string) or other iterable objects " travesal

# while <logic statement> :
#       statements

# Example 1
limit = int(input("Enter limit : "))
count = int(input("Enter count : "))
n = int(input("Enter n : "))
while count <= limit:
    count = count + n                                   # count += n
print(count)