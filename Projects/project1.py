import random
num = random.randint(1, 100)
tries = 0
while tries<5:
    guess_num = int(input("Enter a number: "))
    tries += 1
    if guess_num > num:
        print("Too high")
    elif guess_num < num:
        print("Too low")
    else:
        print("Correct! You guessed it!")
        print(f'Number of tries: {tries}')
        break
    if tries == 5:
        print()
        print(f'You Failed! The correct number was {num}')


