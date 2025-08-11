# n_terms = int(input("Enter the number of terms: "))


# if n_terms <= 0:
#     print("Please enter a positive integer.")
# else:
#     a, b = 0, 1
#     print("Fibonacci sequence:")
#     for _ in range(n_terms):
#         print(a, end=' ')
#         a, b = b, a + b



#Check Armstrong Number:
        
# num = int(input("Enter a number: "))
# total=0
# digits=str(num)
# if digits:
#     power=len(digits)
#     if power:
#         total = 0
#         for digit in digits:
#          total += int(digit) ** power
# if num==total:
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")



#Count the number of digits:-

# user_input = input("Enter a number: ")

# num = int(user_input)
# count = 0

# while num != 0:
#     num //= 10    
#     count += 1
# print("Number of digits:", count)

#Print prime numbers upto to N:-


# N = int(input("Enter N: "))

# for num in range(2, N + 1):
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             break
#     else:
#         print(num, end=" ")


# 5.Palindrome Number Check:-

# x = int(input("Enter a number: "))
# orignal = x  
# reverse = 0
# while x > 0:
#     digit = x % 10
#     reverse = reverse * 10 + digit
#     x = x // 10

# if orignal == reverse:
#     print(f"{orignal} is a palindrome")
# else:
#     print(f"{orignal} is not a palindrome")



#6.Sum of Digits Until Single Digit:-

# n = int(input("Enter a non-negative integer: "))

# while n > 9:
#     total = 0
#     i = n
#     while i > 0:
#         total += i % 10
#         i //= 10
#     print("Sum:", total)
#     n = total
# print("Result:", n)



#7.Reverse a String Without Using Built-in Functions:-

# s = input("Enter a string: ")
# rev = ""
# i = len(s) - 1
# while i >= 0:
#     rev += s[i]
#     i -= 1

# print("Reversed string:", rev)




#product of the list, when zero in list it can't product that number:

mylist=[1,2,8,7,0,4,3]

product=1
new_product=[]

for num in mylist:
    if num!=0:
       product*=num

new_product.append(product)

print("PRODUCT OF THE NUMBERS:",new_product)
