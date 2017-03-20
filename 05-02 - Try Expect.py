# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except (ValueError,TypeError,ZeroDivisionError):
        print("Oops!",sys.exc_info()[0],"occured.")
        print("\n New entry.")
print("The reciprocal of",entry,"is",r)