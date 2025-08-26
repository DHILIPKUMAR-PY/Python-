import random
#File Handling:
# "r"= read:
# "w"= write:
# "x"= create:
# "a"= append:


# 1) Word Frequency Counter
# Read a text file (say a story).Count how many times each word appears.Save the result into another file like:
# the -> 15
# cat -> 4
# jumped -> 2

# with open("first.text", "w") as myfile:
#     myfile.write("Later, the stork decided jumped to return the favor. She invited the fox to her house and served a delicious meal in a tall, narrow-necked jar.")
# count_the = 0
# count_cat = 0
# count_jumped = 0

# with open("first.text", "r") as myfile:
#     text = myfile.read().lower().replace(".", "").replace(",", "")
#     words = text.split()
#     for word in words:
#         if word == "the":
#             count_the += 1
#         elif word == "cat":
#             count_cat += 1
#         elif word == "jumped":
#             count_jumped += 1

# with open("first.text", "w") as myfile:
#     myfile.write("Count of 'the': " + str(count_the) + "\n")
#     myfile.write("Count of 'cat': " + str(count_cat) + "\n")
#     myfile.write("Count of 'jumped': " + str(count_jumped) + "\n")


#2)Random Story Picker.

# quote=("The only way to do great work is to love what you do.","Believe you can and you're halfway there", "The greatest glory in living lies not in never falling, but in rising every time we fall.","Do something today that your future self will thank you for.")
# with open("first.txt", "w") as myfile:
#     my_quote=random.choice(quote)

# with open("first.txt", "r") as myfile:
#     text = myfile.read().lower().replace(".", "").replace(",", "")
#     words = text.split()
#     quote=words

# with open("Quote of the day.text", "w") as myfile:
#     myfile.write(my_quote)