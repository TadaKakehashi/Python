import random

score = 0
tie = 0
lose = 0

while True:
    pc_choice = ["rock", "paper", "scissors"]
    random_choice = random.choice(pc_choice)
    
    user_choice = input("Enter your choice (Rock, Paper, Scissors) or 'q' to quit: ").lower()
    
    if user_choice == 'q':
        print("\nExiting Game!")
        print("Game completed!")
        print("Your Score Card:")
        print(f'Score: {score}\nTies: {tie}\nLosses: {lose}')
        break

    if user_choice not in pc_choice:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        continue

    if user_choice == random_choice:
        print(f"Tie! You both chose {user_choice}.")
        tie += 1
        
    elif (user_choice == "paper" and random_choice == "rock") or \
         (user_choice == "rock" and random_choice == "scissors") or \
         (user_choice == "scissors" and random_choice == "paper"):
        print(f'You Win! You chose {user_choice} and the computer chose {random_choice}.')
        score += 1
    else:
        print(f'You Lose! You chose {user_choice} and the computer chose {random_choice}.')
        lose += 1

        
