#Regular Expression - A RegEx, or Regular Expression,
#  is a sequence of characters that forms a search pattern.


#findall -Returns a list containing all matches

import re

#Metacharacters of findall()

# statement= "I need your help"
# y=re.findall("[a-m]",statement)
# print(y)

# txt="24 was a good movie"
# e=re.findall("\d",txt)
# print(e)


# cond="whats'up bro"
# w=re.findall("what..up",cond)
# print(w)

# txt="It's walk time"
# n=re.findall("^It",txt)
# print(n)
# if n:
#     print("Yes, it is start with ")

# else:
#     print("no")


# txt="It's walk time"
# n=re.findall("time$",txt)
# print(n)
# if n:
#     print("Yes, it is end with ")

# else:
#     print("no")



# txt="It's walk time"
# n=re.findall("time$",txt)
# print(n)
# if n:
#     print("Yes, it is end with ")

# else:
#     print("no")


# cond="whats'up bro"
# w=re.findall("what.*.",cond)
# print(w)

# cond="whats'up bro"
# w=re.findall("what.+.up",cond)
# # print(w)


# cond="whats'up bro"
# w=re.findall("what.?.up",cond)
# print(w)


# txt="welcome to everyone"
# e=re.findall("welc{1}me",txt)
# print(e)


# txt = "The rain in Spain"
# x = re.findall("\AThe", txt)
# print(x)
# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")


# txt = "The rain 34 in Spain"
# x = re.findall("\d", txt)
# print(x)
# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")


# txt = "The rain in Spain"
# x = re.findall("\DThe", txt)
# print(x)
# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")


# import re
# txt = "The rain in Spain"
# x = re.findall("\SThe", txt)
# print(x)
# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")


# txt = "The rain in Spain"
# x = re.findall("Spain\Z", txt)
# print(x)
# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")


# txt = "There is another way to solve"
# x = re.findall("\w", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")


# txt = "There is no way to solve"
# x = re.findall("\W", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

  
# txt = "Iam an average student in my class"
# x = re.findall("[ami]", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")


# txt="Can you send this file tomorrow at 3.00 pm"
# x=re.findall("[0-5][0-9]", txt)
# print(x)

# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")


# txt="The cost of my phone is 30,000"
# x=re.findall("[a-zA-Z]", txt)
# print(x)

# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")


# txt="Can I buy this for 2k"
# x=re.findall("[+]", txt)
# print(x)

# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")


# txt = "The rain in Spain"
# x = re.findall("[a-m]", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")


# txt="He was born in 2007"
# x=re.search("\s", txt)
# print("The first white-space character is located in position:", x.start())


# txt="I payed 15000 this course"
# x=re.search("kelvin", txt)
# print(x)


# txt="I purchased for 2000"
# x=re.split("\s", txt)
# print(x)


# txt="I will meet you tomorrow at 6 am"
# x=re.split("\s", txt, 1)
# print(x)


# txt="class will be start at 5.00 pm"
# x=re.sub("\s","28", txt)
# print(x)











    

    

