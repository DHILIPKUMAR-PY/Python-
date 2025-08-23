import collections


# counter 

# myList=["A","B","C","D","A","B","D"]

# results=collections.Counter(myList)
# print(results)

# ordered dict
# mydict=collections.OrderedDict()
# mydict["a"]=1
# mydict["b"]=3
# mydict["c"]=4

# for i , j in mydict.items():
#     print(i,j)

# mydict.pop("a")
# print("\n")
# for i , j in mydict.items():
#     print(i,j)

# mydict["a"]=4

# print("\n")
# for i , j in mydict.items():
#     print(i,j)


# default dict

# mydict=collections.defaultdict(int)

# myList=[1,2,3,1,1,21,3]

# for i in myList:
#     mydict[i]+=1


# print(mydict)

# chain map
# student1={
#     "name":"gowtham",
#     "age":18
  
# }
# student2={
#     "name":"dhilip",
#     "age":18
  
# }

# results=collections.ChainMap(student1,student2)
# print(results)

# namedtuple

# students=collections.namedtuple("Student",["name","age","course"])

# student=students("vetri",18,"java")

# print(student.name)


# deque

# myitems=collections.deque(["ball","bat","apple","watch","android","phone"])
# print(myitems)

# myitems.append("pencil")
# print(myitems)

# myitems.appendleft("pen")
# print(myitems) 