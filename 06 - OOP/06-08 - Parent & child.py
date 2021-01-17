class Polygon:                                                          # Base | Parent
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])


class Triangle(Polygon):                                                # derived | Child ..> + more features
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):                                                 # New Feature
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)


t = Triangle()                                                          # object
t.inputSides()
t.dispSides()
t.findArea()

# Overriding
isinstance(t,Triangle)                                                  # isinstane (obj)
isinstance(t,Polygon)
isinstance(t,int)
isinstance(t,object)

issubclass(Polygon,Triangle)                                            # issubclass (class inheritance)
issubclass(Triangle,Polygon)
issubclass(bool,int)