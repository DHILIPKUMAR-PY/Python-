#print numbers 1to 10:
# for i in range(1,11):
#     print(i)

# #print the square of each number from 1 to 10:

# for i in range(1,11):
#   print(i*i)
    
# #print each character in string:
# name="jhony"

# for i in range(len(name)):
#    print(name[i])

#sum of number from 1 to 10:
 
# for i in range(1,11):
#     i = i(i+1)/2
#     print(i)


#print each elemnt in a list:

# list=[1,2,3,4,5]
# for i in range(len(list)):
#     print(list[i])

#print only even number from 10 to 20:

# for i in range(10,21):
#     if i%2==0:
#      print(i)


#print number from 10 to 1 (reverse order):

# for i in range(10,0,-1):
#     print(i)

#print the multiples of 5 between 20 to 50 .
# for i in range(20,51):
#   if i%5==0:
#    print(i)

#print number from a list that are greater than 10:
# list=[5,45,6,66,7,22,]

# for i in list:
#  if i>10:
#   print(i)

#print all the prime numbers between 10 and 20:

for i in range(10,20): 
    if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
        print(i)

#find the largest number in a list:

# list=[1,5,7,8]
# max=list[0]
# for i in range(len(list)):
#     if list[i]>max:
#         max=list[i]
# print(max)

#count a number of vowels in a string:
# name="ram"
# count=0
# for i in name:
#     if i in ("a","e","i","o","u"):
#         count+=1
#         print(count)