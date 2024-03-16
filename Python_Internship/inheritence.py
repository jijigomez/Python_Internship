# class Animal:
#     def __init__(self,name):
#         self.name=name
# class Dog(Animal):
#     def make_sound(self):
#         return "woof"
# d1=Dog("jack")
# print(d1.name)
# print(d1.make_sound())



# class Brands:               #parent_class
#     brand_name_1 = "Amazon"
#     brand_name_2 = "Ebay"
#     brand_name_3 = "OLX"
    
# class Products(Brands):       #child_class
#     prod_1 = "Online Ecommerce Store"
#     prod_2 = "Online Store"
#     prod_3 = "Online Buy Sell Store"
    
# obj_1 = Products()          #Object_creation
# print(obj_1.brand_name_1+" is an "+obj_1.prod_1)
# print(obj_1.brand_name_2+" is an "+obj_1.prod_2)
# print(obj_1.brand_name_3+" is an "+obj_1.prod_3)


class Brands:               #parent_class
    brand_name_1 = "Amazon"
    brand_name_2 = "Ebay"
    brand_name_3 = "OLX"
    
class Products:            #child_class
    prod_1 = "Online Ecommerce Store"
    prod_2 = "Online Store"
    prod_3 = "Online Buy Sell Store"

class Popularity(Brands,Products):
    prod_1_popularity = 100
    prod_2_popularity = 70
    prod_3_popularity = 60
    
obj_1 = Popularity()          #Object_creation
print(obj_1.brand_name_1+" is an "+obj_1.prod_1)

print(obj_1.brand_name_2+" is an "+obj_1.prod_2)
print(obj_1.brand_name_3+" is an "+obj_1.prod_3)