class Point:
    default_color = "red"
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point({self.x},{self.y})")
    @classmethod   
    def zero(cls):
       return cls(0,0)

point = Point(1,2)
print(point.x)
print(point.y)
point.z = 3 #object dynamic like javascript
print(point.z)
print(point.default_color)
point.default_color = "orange"
print(point.default_color)
point.draw
point_zero = Point.zero()
print(point_zero.x,point_zero.y)
##################
class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self,tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(),0) + 1

    def __getitem__(self,tag):
        return self.tags.get(tag.lower(),0)

    def __setitem__(self,tag,count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)

cloud = TagCloud()
cloud["python"] = 10
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)
##################
class TagCloudPrivate:
    def __init__(self):
        self.__tags = {}

    def add(self,tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(),0) + 1

    def __getitem__(self,tag):
        return self.__tags.get(tag.lower(),0)

    def __setitem__(self,tag,count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)

cloud_private = TagCloudPrivate()
print(cloud_private._TagCloudPrivate__tags) #you can access private object against java or c#
##################
# class Product:
#     def __init__(self,price):
#         self.set_price(price)

#     def get_price(self):
#         return self.__price

#     def set_price(self,value):
#         if value < 0:
#             raise ValueError("price cannot be negative.")
#         self.__price = value

# product = Product(-50) like java
class Product:
    def __init__(self,price):
        self.set_price(price)

    @property
    def get_price(self):
        return self.__price

    @property
    def set_price(self,value):
        if value < 0:
            raise ValueError("price cannot be negative.")
        self.__price = value

    price = property(get_price,set_price)

# product = Product(10)
# print(product.price)
##################
class Animal:
    def __init__(self):
        print("animal constructor")
        self.age = 1

    def eat(self):
        print("eat")

class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("mammal constructor")
        self.weight = 2
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal()
print(m.age)
print(m.weight)
##################
from abc import ABC, abstractmethod
class human(ABC):
    def __init__(self):
        print("hi")
    @abstractmethod
    def age(self):
        pass
##################