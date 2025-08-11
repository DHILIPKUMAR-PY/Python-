# 1)Library Fine System
#    0 days late → No fine
#   1–5 days → ₹5/day
#   6–10 → ₹10/day

# days=int(input("enter numbers of days late:"))

# if days==0:
#     print("No fine")

# elif days>=1 and days<=5:
#     print(days*5,"Rupees Fine")

# elif days>=6 and days<=10:
#      print(days*10 ,"Rupees Fine")


# 2.Electricity Bill Slab System
#    Units consumed:
#  0–100 → ₹3/unit
#  101–300 → ₹5/unit
# 301–500 → ₹7/unit
# 500 → ₹10/unit

# unit=int(input("Enter a no of units"))

# if unit>=0 and unit<=0:
#     print( unit*3,"Rupees fine")

# elif unit>=101 and unit<=300:
#     print( unit*5,"Rupees Fine")

# elif unit>=301 and unit<=500:
#     print(unit*7, "Rupees fine")

# elif unit<=500:
#     print( unit*10," Rupees Fine")



#1.Allow max 3 attempts to guess a password:

# exact_password="svkdeiahnmmi"

# attempt=3

# for attempts in range(attempt):
#     password=input("Enter the password:")
#     if password==exact_password:
#      print( "Correct Password")
#      break
#     else: 
     
#      print("Password is incorrect, Try again")

#     remaining=attempt-attempts-1

#     if remaining > 0:
#             print(f"You have {remaining} attempt(s) left")
#     else:
#             print("No attempts left. 'Account Blocked'")


# 3.Count the number of vowels and consonants in a given string using a loop:

# name = input("Enter a name: ")
# vowels = 0
# consonants = 0
# for char in name:
#     if char.isalpha():
#         if char in 'aeiou':
#             vowels += 1
#         else:
#             consonants += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants")