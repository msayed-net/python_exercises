# IF_ELIF_ELSE

# variable
weight = float(input("How many kilograms does your suitcase weigh? : "))

# Conditional Flow-chart
if weight < 10:
    print("There is a $5 charge for luggage that heavy.")
elif weight < 20:
    print("There is a $10 charge for luggage that heavy.")
elif weight < 30:
    print("There is a $15 charge for luggage that heavy.")
else:
    print("Sorry we can't handle that heavy")

# Finally
print("We are glade to serve you.")