import random

print("start the game 🎮")
player_choise = input("rock or paper, scissors?")

if player_choise == "rock":
    print("oh you choose rock 🪨")
elif player_choise == "paper":
    print("oh you choose paper 📜")
else:
    print("oh you choose scissors ✂️")

Game = ["rock","paper","scissors"]
pc_choice = random.choice(Game)
print("pc choose is:",pc_choice)

def win():
    if pc_choice == player_choise:
        print("its ti 😒")
    elif (player_choise == "rock" and pc_choice == "scissors") or \
            (player_choise == "paper" and pc_choice == "rock") or \
            (player_choise == "scissors" and pc_choice == "paper"):
        print("you win 😍")
    else:
        print("you lose 😭")
win()
