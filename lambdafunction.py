#lambda function:

#1.Add Two Numbers

# add=lambda x,y:print(x+y)
# add(2,3)


#2..Find the Maximum of Two Numbers:

# max_num=lambda x,y: print(x) if x>y  else print(y)
# max_num(2,5)

#3.Square a Number
# square=lambda num: print(f"{num*num}") 
# square(5)

#4.Reverse a String

# reverse=lambda string: print(string[::-1])
# string="doctor"

#5.Check if a Number is Even
# number=lambda num: print("even") if num%2==0 else print("odd") 
# number(12)

#Recursive Function:
#1.print 10 to 1.

# def sample_order(num):
#     if num!=0:
#      print(num)
#      sample_order(num-1)
# sample_order(10)

#2.Print 1 to 10.
# def sample_number(num):
#     if num!=11:
#         print(num)
#         sample_number( num+1)
        
# sample_number(1)

# 3.Fibonacci:

# def cal_fibo(x):
#         if x<= 0:
#             print("Please enter a positive integer.")
#         else:
#             a, b = 0, 1
#             print("Fibonacci sequence:")
#             for i in range(x):
#                 if a>10:
#                     break
#                 print(a, end=' ')
#                 a, b = b, a + b
# cal_fibo(6)

#4.Sum of list:
# def sum_list(num):
#     if len(num)==0:
#      return 0
#     else:
#        return num[0]+ sum_list(num[1:])

# print(sum_list([1,4,7,9,5]))

#5. Get a input from user as number. If user entered negative number. Throw message as invalid. If user entered  0 throw factorial of 0.  Else it has to act as recursive factorial function.

number=int(input("Enter a number"))

def factorial(i):
 
 if i < 0:
   print ("invalid number, enter a postve number")
 
 elif i==0:
  print(1)
 
 else:
    i*factorial(i-1)
 
factorial(5)