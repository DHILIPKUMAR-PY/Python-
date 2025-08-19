import functools

#1.Square all numbers in a list

# List=[2,4,6,8,12]

# def square(x):
#     return x*x


# res= map(square,List)
# print(list(res))


#2.Convert all strings in a list to uppercase:

# mylist=["jio","airtel","vi"]

# def upper_case(string):
    # return list((map(str.upper,string)))

# print(upper_case(mylist))

#3.Add 10 to each number in a list

# mylist=[2,4,6,8,10,0]

# def add(x):
#     return (x+10)

# res= map(add,mylist)
# print(list(res))

#4.Double each number in a list:

# mylist=[2,4,6,8,10,12]

# def double(x):
#     return x+x

# res=map(double,mylist)
# print(list(res)


#5.Capitalize the first letter of each string in a list

# mylist=["america","australia","africa"]
# def capitalize_first(string):
#     return list(map(str.capitalize,string))
# print(capitalize_first(mylist))


#6.Filter out even numbers from a list:

# mylist=[1,3,2,5,7,6,8]

# def even_number(x):
#     return x%2==0

# result= filter(even_number,mylist)
# print(list(result))


#7.Filter out numbers greater than 10

# mytuple=(2,5,9,11,33,49,77)

# def greater_ten(x):
#     return x>10

# result=filter(greater_ten,mytuple)
# print(tuple(result))

#8.Filter out strings containing the letter 'a':
# mylist=["yuva","dhilip","vetri","thamizh"]
# def letter_a(x):
#     return letter_a in x

# result=filter(letter_a,mylist)
# print(list((result)))

#9.Filter out numbers that are not divisible by 3:

# mylist=[1,4,3,7,6,9,12,13]

# def not_divisible(x):
#     return x%3!=0

# result=filter(not_divisible,mylist)
# print(list(result))

#10.Filter out negative numbers from a list

# mylist=[1,5,6,-2,-7,3,-12]

# def negative_number(x):
#     return x>0

# result=filter(negative_number,mylist)
# print(list(result))

#12.Find the product of all numbers in a list

# mylist=[1,4,7,9,12,16]

# def product_number(x,y):
#     return x*y

# result=functools.reduce(product_number,mylist)
# print(result)


#14.Concatenate a list of strings:

# list= ["Vetri","is","a","son","of","Janakiraman"]

# def concatenate(x,y):
#     return x+y

# result=functools.reduce(concatenate,string)
# print(result)

#15.Find the maximum number in a list:

# mylist=[10,25,37,44,55,77]

# def max_number(x,y):
#     return x if x>y else y

# result=functools.reduce(max_number,mylist)
# print(result)

#16.Compute the sum of squares of numbers in a list:

# list=[2,4,6,8,10]

# def sum_square(x,y):
#     return x+y**2

# result=functools.reduce(sum_square,list)
# print(result)

#17.Compute the factorial of a number using reduce

# number=6
# def factorial(x,y):
#     return x*y

# if number<0:
#     print("invalid number")

# elif number==0:
#     print (1)

# result=functools.reduce(factorial,range(1,number+1))
# print(result)

