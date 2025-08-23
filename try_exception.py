#exception,try,else,finally:
# number=int(input("enter a number"))
# try:
#     result= number>0
#     print(result)
        

# except:
    # print("error......")

# finally:
    # print("done!!!")

# number1=int(input("enter a number1"))
# number2=int(input("ente a number2"))

# try:
#     result=number1/number2
#     print(result)

# except:
#     print("error..")



# try:
#     age=int(input("enter a number"))
#     result=age
#     print(result)

# except:
#     print("error..")


#1.Write a Python program that asks the user to input a number and prints
#  the reciprocal of that number. Handle the exception if the user inputs zero:

# number=int(input("enter a number"))
# if number==0:
#     raise Exception("Zero error..")

# else:
#     print(f"1/{number}")
    

#2.Modify the above program to also handle the exception 
#if the user inputs a non-numeric value

# try:
#     number=int(input("enter a number"))
#     print(number)
# except:
#     print("value Error...")

#3.Write a program that reads a number from the user and prints its square.
#  Use the else clause to print a success message:

# try:
#     number=int(input("enter a number"))
#     result=number**2
#     print(result)
# except:
#     print("error value...")
# else:
#     print("success...")


#4.Modify the program in Task 3 to include a finally clause that prints a message
#regardless of whether an exception occurred or not



# try:
#     number =int(input("Enter a number: "))
#     result= (number*number)
#     print(result)
# except ValueError:
#     print("Invalid input...")
# else:
#     print("Successfully calculated the square.")
# finally:
#     print("Program execution has finished.")

#5.Write a function that raises a ValueError if the input number is negative:
# number=int(input("enter a number"))
# if number<0:
#     raise Exception("Value Error")
# else:
#     print(number)

#6.Write a program that repeatedly asks the user for a number and handles 
# exceptions. The program should continue asking until a valid number is entered.
# while True:
#     try:
#         number=int(input("enter a number:"))
#         result=number
#         print(f"You entered a valid number,{number}")
#         break
#     except:
#         print("invalid number:")

