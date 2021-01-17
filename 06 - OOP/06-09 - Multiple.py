# MultiDerived ..> Base1, Base2
class Base1:
    pass


class Base2:
    pass


class MultiDerived(Base1, Base2):
    pass


# Multilevel ..> Base, Derived, Derived2
class Base:
    pass


class Derived1(Base):
    pass


class Derived2(Derived1):
    pass


# Method Resolution Order (MRB)
# print(issubclass(list,object))
# print(isinstance(5.5,object))
# print(isinstance("Hello",object))


print(MultiDerived.mro())
print(Derived2.mro())


# Tree
class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X,Y):
    pass


class B(Y,Z):
    pass


class M(B, A, Z):
    pass

print('\n', M.mro())