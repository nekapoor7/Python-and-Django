#How to check if a class is subclass of another?

class Base:
    pass

class Derived(Base):
    pass

print(issubclass(Base,Derived))
print(issubclass(Derived,Base))

b = Base()
d = Derived()

print(isinstance(b,Derived))
print(isinstance(d,Base))