#Example_operator_overloading
# class Abc:
#         x = 2+3
#         y = "jiji"+"gomez"
        
# obj = Abc()
# print(obj.x)

# print(obj.y)



#function polymorphism
# print(len("hellofriends"))

# print(len(["python","java","c++","c#"]))
# print(len({"Name":"anjali","age":22,"City":"trivandrum"}))

#method overriding

# class shape:
#     def area(self):
#         return 0
# class Circle(shape):
#         def __init__(self,radius):
#                self.radius=radius
        
#         def area(self):
#             return 3.14 * self.radius **2
# circle=Circle(radius=2)
# print(circle.area())
# program to illustrate public access modifier in a class

class Geek:
	
	# constructor
	def __init__(self, name, age):
		
		# public data members 
		self.geekName = name
		self.geekAge = age

	# public member function	 
	def displayAge(self):
		
		# accessing public data member
		print("Age: ", self.geekAge)

# creating object of the class
obj = Geek("R2J", 20)

# accessing public data member
print("Name: ", obj.geekName)

# calling public member function of the class
obj.displayAge()



# Private_access_modifiers 
class Student: 
    def __init__(self, age, name): 
        self.__age = age
        
        def __funName(self):
            self.y = 34
            print(self.y)

class Subject(Student):
    pass

obj = Student(21,"pythonlobby")
obj1 = Subject

# calling by object reference of class Student
print(obj.__age)
print(obj.__funName())

# calling by object reference of class Subject
print(obj1.__age)
print(obj1.__funName())