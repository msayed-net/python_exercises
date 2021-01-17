# Admin
balance = float(input("{Admin} ; Enter his/her balance : "))
name = str(input("{Admin ; Enter his/her name : "))
print("Welcome, " + name)                                        # welcoming

# Password
password = int(input("Enter password : "))
if password == int(9510):
    print("Access granted")
else:
    print("Wrong password")
    exit()

# Operations
service = int(input("1:check , 2:pull out : "))
if service == 1:
    print("Balance is, {0}".format(balance))
elif service == 2:
    pull_out = int(input("How much? : "))
    if pull_out <= balance:
        print("Take card, wait for money")
    else:
        print("Sorry, you don't have enough budget")


# Finally
print("We are glade to serve you.")