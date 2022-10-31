from abc import ABC, abstractmethod
class Polygon(ABC):
 
    def mock(self):
        print("hello")
        print("working")
 
class Triangle(Polygon):
 
    # overriding abstract method
    def mock(self):
        return self
        

R = Polygon()
R.mock()
 
# K = Triangle()
# K.mock()


# Astarct class or method is a method in which we can use the functionality in parent classs as well child class without modifying functionalities.
# abstarction hiding wanted data showing minimal information is called abstraction.
# using single interface showing multiple functionalities.