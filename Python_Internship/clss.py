# class Myclass:
#     x=20
# obj1=Myclass()
# print(obj1.x)

# class Bike:
#     name="bullet"
#     gear=0
# bike1=Bike()
# print(bike1.name)
# print(bike1.gear)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("jiji",24)
print(p1.name)

print(p1.age)