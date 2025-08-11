#SET
# myset={"pushups","pullups","dumbells","benchpress","butterfly"}
# print(myset)
# print(len(myset))
# print(type(myset))


# myset={"pushups","pullups","dumbells","benchpress","butterfly"}
# print("benchpress" in myset)

#ADD:
# myset={"pushups","pullups","dumbells","benchpress","butterfly"}
# myset.add("cablework")
# print(myset)

#update:

# myset={"pushups","pullups","dumbells","benchpress","butterfly"}
# sets={"latpulldown","barbellpress","legpress"}
# myset.update(sets)
# print(myset)

#remove
# myset={"pushups","pullups","dumbells","benchpress","butterfly"}
# myset.remove("pushups")
# print(myset)

#Discard
# myset={"pushups","pullups","dumbells","benchpress","butterfly"}
# myset.discard("pullups")
# print(myset)

#pop:
# myset={"pushups","pullups","dumbells","benchpress","butterfly"}
# myset.pop()
# print(myset)

#Clear:
# myset={"pushups","pullups","dumbells","benchpress","butterfly"}
# myset.clear()
# print(myset)

#loop method:
# myset={"pushups","pullups","dumbells","benchpress","butterfly"}
# for i in myset:
#     print(i)

#union:
# myset={"pushups","pullups","dumbells","benchpress","butterfly"}
# sets={"jumping","latpulldown","barbellpress",}
# set1= myset|sets
# print(set1)

#update:
# myset={"pushups","pullups","dumbells","benchpress","butterfly"}
# sets={"jumping","latpulldown","barbellpress",}
# myset.update(sets)
# print(myset)

# sets={"jumping","latpulldown","barbellpress","pullups"}
# myset={"pushups","pullups","dumbells","benchpress","butterfly"}
# set=myset&sets
# print(set)

# myset={"pushups","pullups","dumbells","benchpress","butterfly"}
# sets={"jumping","latpulldown","barbellpress","pullups"}

# myset.intersection_update(sets)
# print(myset)

# sets={"jumping","latpulldown","barbellpress","pullups"}
# myset={"pushups","pullups","dumbells","benchpress","butterfly"}
# set=myset.difference(sets)
# print(set)

# myset={"pushups","pullups","dumbells","benchpress","butterfly"}
# sets={"jumping","latpulldown","barbellpress","pullups"}
# set=myset.symmetric_difference(sets)
# print(set)

# myset={"pushups","pullups","dumbells","benchpress","butterfly"}
# sets={"jumping","latpulldown","barbellpress","pullups"}
# set=myset.isdisjoint(sets)
# print(set)

# myset={"pushups","pullups","dumbells","benchpress","butterfly"}
# sets={"jumping","latpulldown","barbellpress","pullups"}
# set=myset.issubset(sets)
# print(set)



# myset={"pushups","pullups","dumbells","benchpress","butterfly"}
# sets={"jumping","latpulldown","barbellpress","pullups"}
# set=myset.issuperset(sets)
# print(set)




# myset={1,3,5,7,15,19,23,29}
# smallest=0
# largest=0

# for i in myset:
#   if smallest is 0 or i<smallest:
    # smallest=i

#   elif largest is 0 or i>largest:
#    largest=i

# print("Largest number",largest)
# print("Smallest number",smallest)