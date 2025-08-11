#FUNCTIONS-set of code run when it is called-Reusability:

#1.Calculate Square
# def cal_square():
#     num=int(input("enter a number:"))
#     if num:
#         print("Square of the number",num*num)

# cal_square()

#2.Calculate Area of Rectangle
# def cal_rectangle(lenght,breadth):
#     if lenght>0 and breadth>0:
#         print("Area of Rectangle:",lenght*breadth)

#     else:
#         print("invalid")


# cal_rectangle(11,22)

#3.Check Even or Odd

# def Check_evenorodd(num):
#     if num %2==0:
#         print("the number is even:",num)
#     else:
#         print("the number is odd:",num)


# Check_evenorodd(2)
# Check_evenorodd(5)


#3.Calculate Factorial:
# def cal_factorial(num):

#    factorial=1 
#    for x in range(1,num+1):
#         factorial*=1
#         return factorial
        
#    cal_factorial(5)
#    print("Factorial is:",cal_factorial(5))



#5.Check Prime Number:


# def check_primenumber(num):
#    if num>=1:
#       if num==2 or num==3 or num==5 or num==7:
#           print("Its a prime number",num)
#       elif num%2==0 or num%3==0 or num%5==0 or num%7==0:
#           print(" Not a Prime number",num)
#    else:
#       print( "Not a prime number:",num)


# check_primenumber(8)
# check_primenumber(7)

#6..Reverse a String

# def reverse_string():
#    stg=input("enter a string")
#    reverse=""
#    i=len(stg)-1
#    while i>=0:
#       reverse+=stg[i]
#       print("Reverse a string",reverse)
# reverse_string()

#7. Count Character:

# def count_chr():
#     name = input("Enter the string: ")
#     count = 0
#     for char in name:
#         count += 1
#     print("Number of characters:", count)

# count_chr()



# 8.In a list print Sum of Squares:

# list=[1,2,3,4,5,6]

# def sum_square():
#     sum=0
#     for i in list:
#         sum+=i*i
#     print(sum)

# sum_square()

#9.Check Palindrome:-

# def check_num(x):
#     orignal = x  
#     reverse = 0
#     while x > 0:
#         digit = x % 10
#         reverse = reverse * 10 + digit
#         x = x // 10
#     if orignal == reverse:
#         print(f"{orignal} is a Palindrome Number")
#     else:
#         print(f"{orignal} is not a Palindrome Number")
# check_num(123)


#10. Calculate Fibonacci:-

# def cal_fibo(x):
#     if x<= 0:
#         print("Please enter a positive integer.")
#     else:
#         a, b = 0, 1
#         print("Fibonacci sequence:")
#         for _ in range(x):
#             print(a, end=' ')
#             a, b = b, a + b
# cal_fibo(12)


#11.Check Armstrong Number:-

# def check_num(x):
#     total=0
#     digits=str(x)
#     if digits:
#         power=len(digits)
#         if power:
#             total = 0
#             for digit in digits:
#                 total += int(digit) ** power
#     if x==total:
#         print(f"{x} is an Armstrong number.")
#     else:
#         print(f"{x} is not an Armstrong number.")
# check_num(153)
