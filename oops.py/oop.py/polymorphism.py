#Polymorphism - in Python refers to the ability of different 
# classes to respond to the same method call in different ways.

#polymorphism:
#"Even if the method name is the same, it shows different behavior in different classes."



# class Bird:
#     def about(self):
#         return "Some about birds"
    
# class peackock(Bird):
#     def about(self):
#         return "Some Bird Nation bird"

# class parrot(Bird):
#     def about(self):
#         return "It can speak"

# obj1=Bird()
# obj2=peackock()
# obj3=parrot()
# print(obj1.about())
# print(obj2.about())
# print(obj3.about())

    
#1. Compile-type polymorphism(static Polymorphism):

# class calculator:
#     def add(self,a=0 , b=0 , c=0):
#         return a + b + c
    
# cal=calculator()
# print(cal.add(2,3,6))
# print(cal.add(2,4))
# print(cal.add(1))

# #2. Run time polymorphism (Dynamic polymorphism);
# class Bird:
#     def about(self):
#         return "Some about birds"
    
# class peackock(Bird):
#         def about(self):
#             return "Some Bird Nation bird"

# class parrot(Bird):
#     def about(self):
#         return "It can speak"

# Birds = [Bird(),peackock(),parrot()]
# for i in Birds:
#      print(i.about())








