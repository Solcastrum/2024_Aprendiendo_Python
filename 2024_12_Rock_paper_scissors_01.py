import random
print ("Let's play rock, paper or scissors")
player_choice = input("Choose your weapon: rock, paper or scissors: ").lower()
choices = ["rock", "paper" ,"scissors"]
computer_choice = random.choice(choices)
print (f"Computer chose {computer_choice}")

if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
  winner = "Player"
elif  player_choice == computer_choice :
    winner = "Tie"
else :
   winner = "Computer"

if winner == "Player" :
  print ("You won")
elif winner == "Tie" :
  print ("Is a tie")
else :
  print ("Computer won")