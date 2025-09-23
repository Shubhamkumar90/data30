from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,r):
        self.__radius=r
    def area(self):
        print(f"Circle Area: {3.14*self.__radius*self.__radius}")

class Rectangle(Shape):
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        print(f"Rectangle Area: {self.l*self.w}")
c=Circle(4)
c.area()
r=Rectangle(3,4)
r.area()