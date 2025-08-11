# paragraph="He  \"is\" a  great artist in the world."
#condition1=(paragraph.replace("is" , "was"))
#print(condition1)

#condition2=(paragraph.count("a"))
#print(condition2)

#GET AN INPUT FROM THE USER AND CHECK ITS A EMAIL ID


#GET AN INPUT FROM THE USER AND CHECK ITS A EMAIL ID

# if "@" in email and "." in email:

#     if email.endswith("@gmail.com"):
#         at_index = email.index("@")
#         dot_index = email.index(".")  

#         if at_index < dot_index and dot_index < len(email) - 1:
#             print("It is a Valid Email Id")
#         elif at_index > dot_index:
#             print("Email Invalid, '@' and '.' are misplaced")
#         else:
#             print("Please enter a valid input")
#     else:
#         print("Invalid Email:\"@\" and \".\" is misplaced ")

# elif "@" in email and "." not in email:
#     print("Email Invalid, '.' is missing")

# elif "@" not in email and "." in email:
#     print("Email Invalid, '@' is missing")

# else:
#     print("Please enter a valid input")

#3.CHECK AN INPUT FROM THE USER AND ALSO CHECK ITS PASSWORD;

# password=input("Enter your password:")

# special_character="!@#$%^&*"
# upper_count=0
# lower_count=0
# special_count=0
# for i in password:
#  if i!=i.lower():  
#   upper_count += 1
#  if  i!=i.upper():
#     lower_count += 1
#  if  i in special_character:
#      special_count += 1

# if len(password)<6:
#      print("Invalid password:")
# elif upper_count == 0:
#      print("Password Invalid:")
# elif lower_count == 0:
#      print("Password Invalid:")
# elif special_count == 0:
#      print("Password Invalid:")
# else:
#     print("It is a Valid Password.")

#4.login task - get input from user name & password its align with your previous data.throw a login successful message.otherwise its a Invalid input. ( with specific attempts)
    
# exact_username="dhilip"
# exact_password="0908"

# max_atempts=3

# for atempt in range(max_atempts):
#  username=input("Enter your username")
# if username==exact_username:

#  password=int(input("Enter your password"))
#  if password==exact_password:
#   print("Login Successful")

#  else:
#   print("Incorrect password; Please enter valid password")

# else:
#  print("Incorrect password: Please enter valid username")

# remaining= max_atempts-atempt-1

# if remaining>0:
#  print("You have {remaining} atempts left To try")

# else:
#  print("No atempts left")

