#Encapsulation:
#bundle of variable and methods 
#three types of Encapsulation:
#1. Public 
#2.Protected (_)
#3. Private  (__)


#1.public can be usable in anywhere:

# class MyClass:
#     def __init__(self):
#         self.name = "Alice" 

# obj = MyClass()
# print(obj.name)

#2. Protected can be usable when another by another class:

# class MyClass:
#     def __init__(self):
#         self._age = 25  

# class Child(MyClass):
#     def show_age(self):
#         print(self._age)

# obj = Child()
# obj.show_age()     
# print(obj._age) 


#3.private can be accessable by another function method:

# class MyClass:
#     def __init__(self):
#         self.__salary = 400000  

#     def show_salary(self):
#         print(self.__salary)

# obj = MyClass()
# obj.show_salary()    


# class myclass:
#     def __init__(self,name,age):
#         self.name=name
#         self._age=age
#         self.__salary= 4000000

#     def get_salary(self):
#         return self.__salary
    
#     def set_salary(self,new_salary):
#         if new_salary>0:
#             return self.__salary== new_salary
#         else:
#             return ("Invalid salary")
        
#     def display_info(self):
#         print(f"Name: {self.name}, Age: {self._age}, Salary: {self.__salary}")

# obj=myclass("dhilip",30)
# print(obj.name)



