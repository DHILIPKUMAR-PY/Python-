import random

# print(random.randrange(2,5))

# list=[1,6,9,12,45,67]
# res=(random.choice(list))
# print(res)

# print(random.random())

# print(random.randint(2,7))

# list=["butterfly","harmell curl","bench press","leg extension"]
# res=(random.sample(list,k=3))
# print(res)

# print(random.uniform(10,40))


#1. Random Puzzle Task:

outdoorgames=["cricket","basketball","football","throwball","tennis","hockey"]
total_attempts=5
again_play="yes"
while again_play=="yes":
    Answer=random.choice(outdoorgames)
    attempts=0
    for i in range(1,total_attempts+1):
        player1=input("Enter a playgame:")
        attempts+=1
        if player1==Answer:
            print("both the players entered corretly")
            break
        elif attempts<total_attempts:
            print("not matched,Try another time")

        else:
            print("all attempts are finished")

    again_play=input("do you want to play again(yes or no):")
    

    

    


    
 


