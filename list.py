#list
#1.ORDERED

# mylist=["mt15","yamaha","Royal Enfield","kawasaki"]
# print(mylist)

#DUPLICATES
# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# print(mylist)

# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]

# print(len(mylist))


# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# print(type(mylist))

#list() constructor

# mylist=list(("mt15","yamaha","Royal Enfield","kawasaki","mt15"))
# print(mylist)

#list access item;
# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# print(mylist[0])

# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# print(mylist[-3:])

# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# print(mylist[-4:-1])

#check if item exist:
# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# if "splendor" in mylist:
#     print("yes")

#changeable:
# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# mylist[1:3]= "R15","shine"
# print(mylist)

#insert()
# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# mylist.insert(0,"GT650")
# print(mylist)

# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# mylist.insert(2,"appache")
# print(mylist)

#APPEND
# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# mylist.append("zest")
# print(mylist)

#APPEND
# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# newtuple=("jupiter","access")
# mylist.extend(newtuple)
# print(mylist)

# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# mylist.remove("mt15")
# print(mylist)

# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# mylist.pop(3)
# print(mylist)

mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
del mylist[2]
print(mylist)


#WHILE LOOP
# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# for i in range(len(mylist)):
#     print(mylist[i])

# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# i=0
# while i  < len(mylist):
#   print(mylist[i])

#LIST COMPREHENSION
# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# newlist=[]
# for i in mylist:
#     if "i" in mylist:
#         newlist.append(i)
#         print(newlist)

# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# newlist=[i for i in mylist if "a" in i]
# print(newlist)

# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# newlist=[x for x in mylist]
# print(newlist)

#SORT LIST:
# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# mylist.sort()
# print(mylist)

# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# mylist.sort(reverse=True)
# print(mylist)

# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# mylist.reverse()
# print(mylist)

# #COPY LIST
# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# NEWLIST=mylist.copy()
# print(NEWLIST)

#JOIN LIST:
# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# newlist=[1,5,9,0]
# for i in newlist:
#     mylist.append(i) 
# print(mylist)

# mylist=["mt15","yamaha","Royal Enfield","kawasaki","mt15"]
# list2=[1,4,7,9,]
# list3= mylist + list2
# print(list3)

