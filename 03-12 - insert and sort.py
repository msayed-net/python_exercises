def insertionsort( aList ):
    for i in range(1, len( aList )):
        tmp = aList [i]
        k = i
        while k > 0 and tmp < aList[k - 1]:
            aList[k] = aList[k - 1]
            k -= 1
        aList[k] = tmp

count = int(input("Enter count : "))
sort_list = []
for i in range(count):
    sort_list.append(int(input("Numbers : ")))

insertionsort(sort_list)

print(sort_list)