class ComplexNumber:
    def __init__(self, r=0, i=0):                           # __init__() to initialize the variables (defaults to zero)
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

# Create a new ComplexNumber object
c1 = ComplexNumber(2, 3)

# Call getData() function
# Output: 2+3j
c1.getData()                                                # getData() to display the number

# Create another ComplexNumber object
# and create a new attribute 'attr'
c2 = ComplexNumber(5)
c2.attr = 10

print((c2.real, c2.imag, c2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
# print(c1.attr)


# del c1.imag                                               # Delete Attribute
# c1.getData()

# del ComplexNumber.getData                                 # Delete Attributes
# c1.getData()

# del c1                                                    # Delete object
# c1.getData()
