# #1. voter eligibility checker

# name=int(input("what is your name"))

# age=int(input("what is your age"))

# if age>=18:
#    print("is eligible for voting:")

# elif 10<=age<18:
#    print("is underaged,wait for a few more years:")
   
# elif age<10:
#    print("is a child, focus on studies:")

#2.JOB APPLICATION LOGIC

# age=int(input("what is your age"))	
   
# experience=int(input("how many years of experience"))

# skills=(input("enter your skills"))

# if age>=21 and experience>2 and skills in "python":
#    print("eligible for developer role")

# else:
#    print("not eligible for developer role")


#3. LOGIC VALIDATION:

# correct_username="admin"

# correct_password="1234"


# username=input("enter a username")

# password=input("enter a password")


# if username== correct_username and password== correct_password:
#    print("login successfully")
   
# elif username==correct_username :
#    print("password is wrong")
   
# else:
#    print("user not found")


#Rock, Paper and Scissors:

# player1=input("enter for player1:")

# player2=input("enter for player2")

# if player1=="Rock" and player2=="Paper":
#     print("Paper beats Rock:")

# elif player1=="Paper" and player2== "Rock":
#     print("Paoer beats rock:")

# elif player1=="Scissor" and player2=="Paper:":
#     print("scissor beats paper:")

# elif player1=="Paper" and player2=="Scissor:":
#     print("Scissor beats Paper")

# elif player1=="Rock" and player2=="Scissor":    
#     print("Rock beats Scissor")

# elif player1=="Scissor" and player2=="Rock":
#     print("Rock beats Scissor")

# else:
#     print ("it is a tie")

#time based greeting:
# hour=int(input("enter the hour"))

# if hour>=5 and hour<11:
#     print("Good Morning")

# elif hour>=12 and hour<17:
#     print("Good Afternoon")

# elif hour>=18 and hour<20:
#     print("Good Evening")

# elif hour>=21 and hour<23:
#     print("Good Night")

# elif hour>=0 and hour<4:
#     print("Good Night")

# else:
#     ("Invalid Hour")

# input user's account balance and amount to withdraw:

# account=int(input("Enter the account balanace:"))
# withdrawal=int(input("Enter the withdrawal amount:"))

# Balance=account-withdrawal
# if  withdrawal%100==0 and account>withdrawal:
#     print("Balance amount:",Balance)

# elif withdrawal%100!=0 and account>withdrawal:
#     print("Amount must be mupltiples of 100")

# elif withdrawal%100==0 and account<withdrawal:
#     print("Insufficient balance")