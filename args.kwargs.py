#1: Sum of all arguments

# def sum_argument(*num):
#     total=0
#     for i in num:
#         total+=i
#     return total

# print(sum_argument(3,6,9,12,15,18))


#2.Multiply all arguments:

# def multiply_argument(*num):
#     total=1
#     for i in num:
#         total*=i
#     return total

# print(multiply_argument(1,6,7))

#3.Concatenate all arguments:

# def con_argument(*str):
#     total="  "
#     for i in str:
#      total+=i
#     return total
# print(con_argument(" vetri " ," topper "))

#4.Print arguments and keywords:
 
# def show_detail(*args,**kwargs):
#     print("aruguments:",args)
#     print("keywords:",kwargs)

# show_detail(1,2,4,"add", topper="vetri",batsman="yuvaraja")

#i/p : checkout_cart(100, 200, 150, discount=10, tax=5, shipping=50)

# def checkout_cart(*args,**kwargs):
#     subtotal = sum(args)

#     discount = kwargs.get('discount')
#     if discount:
#         subtotal -= (subtotal * discount / 100)
#     tax = kwargs.get('tax')
#     if tax:
#         subtotal += (subtotal * tax / 100)

#     shipping = kwargs.get('shipping')
#     subtotal += shipping
#     print(f"Final amount to pay: ₹{round(subtotal, 2)}")
# checkout_cart(100, 200, 150, discount=10, tax=5, shipping=50)

