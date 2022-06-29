import random
weapons=["rock","paper","scissors"]
user_select=input("Choose one of the weapons to start the game [rock,paper,scissors] : ")
computer_select=random.choice(weapons)
if user_select=="rock":
    if computer_select=="paper": print("You won :)")
    if computer_select=="scissors": print("The computer won!")
    if computer_select=="rock": print("Intense equals")

if user_select=="paper":
    if computer_select=="rock": print("You won :)")
    if computer_select=="scissors": print("The computer won!")
    if computer_select=="paper": print("Intense equals")
    
if user_select=="scissors":
    if computer_select=="rock": print("You won :)")
    if computer_select=="scissors": print("Intense equals")
    if computer_select=="paper": print("You won :)")


print("user : ", user_select)
print("computer : ", computer_select)   