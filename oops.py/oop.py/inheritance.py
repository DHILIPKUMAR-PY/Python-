#2. INHERITANCE:
#there are five types of inheritance in oops:

#1. Single Inheritance :"one childclass from one parent class":
#2. Multiple Inheritance: "One child class from more than one parent class":
#3. Multilevel Inheritance: "Grandparetns to parents and to child":
#4. Hierarchial Inheritance: "Multiple class inherit from same parent class":
#5. Hybrid Inheritance "A combination of two or more types of inheritance":

#1. Single Inheritance:

# class buyer():
#     def seller(self):
#         print("how much this product?")

# class price(buyer): 
#     def price(self):
#         print("it is 300")

# obj=price()
# obj.seller()
# obj.price()

#2. Multiple Inheritance:

# class flyable:
#     def fly(self):
#         print("yes,it can fly")

# class swimable:
#     def swim(self):
#         print("yes it can swim")

# class hen(flyable,swimable):
#     pass

# obj=hen()
# obj.swim()
# obj.fly()


#3.Multilevel Inheritance:
# class Manager():
#     def head(self):
#         print("head of the leader")

# class teamleader(Manager):
#     def leader(self):
#         print("leader of the team")

# class worker(teamleader):
#     def work(self):
#         print("working under leader")


# order=worker()
# order.head()
# order.leader()
# order.work()


#4.Hierarchial Inheritence:

# class AK:
#     def parent(self):
#         print("AK has two children")

# class child1(AK):
#     def child(self):
#         print("Anouska Kumar")

# class child2(AK):
#     def childs(self):
#         print("Adhvik Kumar")

# obj1=child1()
# obj2=child2()

# obj1.parent()
# obj1.child()
# obj2.childs()