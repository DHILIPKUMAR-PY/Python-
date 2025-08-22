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

# outdoorgames=["cricket","basketball","football","throwball","tennis","hockey"]
# total_attempts=5
# again_play="yes"
# while again_play=="yes":
#     Answer=random.choice(outdoorgames)
#     attempts=0
#     for i in range(1,total_attempts+1):
#         player1=input("Enter a playgame:")
#         attempts+=1
#         if player1==Answer:
#             print("both the players entered corretly")
#             break
#         elif attempts<total_attempts:
#             print("not matched,Try another time")

#         else:
#             print("all attempts are finished")

#     again_play=input("do you want to play again(yes or no):")



# (GAME 2)


# posibility= ["rock", "paper", "scissors"]
# player_score = 0
# random_score = 0

# for i in range(3):   
#    player = input("Enter rock/paper/scissors: ")
#    rand = random.choice(posibility)
#    print("Random:", rand)

#    if player == rand:
#        print("Tie:")
#    elif (player=="rock" and rand=="scissors") or  (player=="paper" and rand=="rock") or (player=="scissors" and rand=="paper"):
#        print("You win this round!")
#        player_score += 1
#    else:
#        print("Computer wins this round!")
#        random_score += 1

# print("Final Result:")
# if player_score > random_score:
#    print("player win the game")
# elif random_score > player_score:
#    print("Randon win the game")
# else:
#    print("Game Draw")
    

#TREASURE HUNT:

# locations = ["cave", "river", "mountain", "forest", "desert"]
# hints = {
#     "cave": "Treasure is underground.",
#     "river": "Treasure is near water.",
#     "mountain": "Treasure is in a high place.",
#     "forest": "Treasure is among trees.",
#     "desert": "Treasure is in a dry place."
# }
# treasure = random.choice(locations)   
# attempts = 3

# print(" Treasure Hunt Game")
# print("Find the treasure! Locations:", ", ".join(locations))
# print(f"You have {attempts} attempts.\n")

# while attempts > 0:
#     guess = input("Enter your guess: ").lower()

#     if guess == treasure:
#         print(" You found the treasure in the", treasure)
#         break
#     else:
#         attempts -= 1
#         if attempts > 0:
#             print(" Wrong guess.")
#             print(" Hint:", hints[treasure])
#             print(f"Attempts left: {attempts}")
#         else:
#             print(" Out of attempts! The treasure was in the", treasure)

    


    
 


