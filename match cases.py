#check a day as weekday or weekend:
# day=input("enter a day")

# match day.lower():

#     case day if day==("Monday,tuesday,wednesday,thursday,friday"):
#         print("its a weekday")
    
#     case day if day==("saturday,sunday"):
#         print("its a weekend")

#     case _:
#         print("it is invalid ")


#print a no of days in a month:

# month=input("enter a month")

# match month.lower():

#     case month if month==("January,march,may,july,august,october,december"):
#         print("this month contains 31 days")
#     case month if month=="febraury":
#         print("this month contains 28 days if its leapyer 29 days ")
#     case month if month==("april,june,september,november"):
#         print("this month contains 30 dyas")
    
#     case _:
#         print("ivalid month")

#PRINT A ENTERED INPUT IS VOWEL OR CONSTANT:

# letter=input("enter a letter")

# match letter.lower():
#     case letter if letter in ("a,e,i,o,u"):
#         print("this is vowels")
#     case letter if letter in ("b,c,d,f,g,h,j,k,l,,m,n,p,q,r,s,t,v,w,x,y,,z"):
#         print("this is constant")

#     case _:
#         print("both vowel and constant")

#GRADE BY PERCENTAGE:
# percentage=int(input("enter a percentage"))

# match percentage:
#     case percentage if percentage<=100 and percentage>=80:
#         print("GRADE A")
#     case percntage if percntage<=80 and percentage>=60:
#         print("GRADE B")
#     case percentage if percntage<=60 and percentage>=50:
#         print("GRADE C")
#     case percentage if percntage<=50 and percentage>=35:
#         print("GRADE D")
#     case percentage if percntage<35:
#         print("GRADE F")
    

#SEASON BASED ON MONTH NAME:

# month=input("enter a month")

# match month .lower():
#   case month if month in ("december,january,february"):
#     print("season:winter")
#   case month if month in ("march,april,may"):
#     print("season:spring")
#   case month if month in ("june,juy,august"):
#     print("season:summer")
#   case month if month in("sepember,october,november"):
#     print("season:spring")
  
#   case _:
#     print("invalid month")

# POSITIVE OR NEGATIVE;
# number=int(input("enter a number"))

# match number:
#   case number if number>0 :
#     print(" the numebr is positive")
#   case number if number<0:
#     print("the number is negative")

#   case _:
#     print("invalid number")


#.Get input from user print if it is between 1-50. 

# number=int(input("enter a number"))

# match number:
#     case number if number>=1 and number<=50:
#         print("the number is between in range")
    
#     case _:
#         print("the number is not in range")


#GET AN INPUT FROM THE USER NUMBER,OPERATOR:

# number1=int(input("Enter the number1:"))
# number2=int(input("Enter the number2:"))

# operator="+","-","*"
# match operator=