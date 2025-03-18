import random
dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]

while True:
    user_input = str(input("Do you want to roll the dice? y or n (q to quit)")).lower()
    
    if user_input == 'q':
        print("Exiting game")
        break
    
    if user_input == "y":
        random_dice1 = random.choice(dice1)
        random_dice2 = random.choice(dice2)
        print(f'{random_dice1},{random_dice2}')
    elif user_input == "n":
        print("Exit the program?")
        user_input == 'q'
    
    else:
        print('Invalid input!')
        