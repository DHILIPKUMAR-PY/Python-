#Dictionary:

# qualification={
#     "vehicle":"car",
#     "experience":"5years",
#     "age":"35",
#     "no.plate":"py.01-5555"
# }
# print(qualification)

# print(type(qualification))

# qualification={
#     "vehicle":"car",
#     "experience":"5years",
#     "age":"35",
#     "no.plate":"py.01-5555"
# }
#print(qualification["age"])
# i=qualification.get("age")
# print(i)

# qualification={
#     "vehicle":"car",
#     "experience":"5years",
#     "age":"35",
#     "no.plate":"py.01-5555"
# }
# x=qualification.keys()
# print(x)

# qualification["colour"]="white"
# print(x)


# i=qualification.values()
# print(i)

# x=qualification.items()
# print(x)


# mydict={
#     "vehicle":"car",
#     "experience":"5years",
#     "age":"35",
#     "no.plate":"py.01-5555"
# }
# mydict["vehicle"] = "bike"
# print(mydict)

# mydict={
#     "vehicle":"car",
#     "experience":"5years",
#     "age":"35",
#     "no.plate":"py.01-5555"
# }
# mydict.update({"age": "7years"})
# print(mydict)

# mydict["vehicle"]="bike"
# print(mydict)


#Remove:
# mydict={
#     "vehicle":"car",
#     "experience":"5years",
#     "age":"35",
#     "no.plate":"py.01-5555"
# }
# mydict.pop("age")
# print(mydict)

# mydict={
#     "vehicle":"car",
#     "experience":"5years",
#     "age":"35",
#     "no.plate":"py.01-5555"
# }
# mydict.popitem()
# print(mydict)



#del method
# mydict={
#     "vehicle":"car",
#     "experience":"5years",
#     "age":"35",
#     "no.plate":"py.01-5555"
# }
# del mydict["age"]
# print(mydict)



#Clear
# mydict={
#     "vehicle":"car",
#     "experience":"5years",
#     "age":"35",
#     "no.plate":"py.01-5555"
# }
# mydict.clear()
# print(mydict)



#Fromkeys:

# keys=("key1","key2","key3","key4")
# values=0
# mydict=dict.fromkeys(keys,values)
# print(mydict)



# mydict={
#     "vehicle":"car",
#     "experience":"5years",
#     "age":"35",
#     "no.plate":"py.01-5555"
# }
# i=mydict.setdefault("color","white")
# print(i)

# mydict={
#     "vehicle":"car",
#     "experience":"5years",
#     "age":"35",
#     "no.plate":"py.01-5555"
# }
# newdict=mydict.copy()
# print(newdict)

# mydict={
#     "vehicle":"car",
#     "experience":"5years",
#     "age":"35",
#     "no.plate":"py.01-5555"
# }
# newdict=dict(mydict)
# print(newdict)


#employees
# employee1={
#     "name":"vetri",
#     "age":"29",
#     "experience":"4years",
#     "salary":"85k/month"
#     }

# employee2={
#     "name":"gowtham",
#     "age":"31",
#     "experience":"2years",
#     "salary":"80k/month"
#     }

# employee3={

#     "name":"thamizh",
#     "age":"29",
#     "experience":"4years",
#     "salary":"60k/month"
#     }

# employee4={

#     "name":"yuva",
#     "age":"32",
#     "experience":"5years",
#     "salary":"75k/month"
#     }

# employee5={
    
#     "name":"balaji",
#     "age":"23",
#     "experience":"1.5years",
#     "salary":"45k/month"
#     }

# employees={
#     "employee1":employee1,
    
#     "employee2":employee2,

#     "employee3":employee3,

#     "employee4":employee4,

#     "employee5":employee5
# }

# for key , valuesDic in employees .items():
#     print("\n",key)
#     for keynes in valuesDic:
#         print(keynes,":",valuesDic[keynes])
