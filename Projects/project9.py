import random

print("Welcome to Blackjack!")


def calculate_total(cards):
    total = sum(cards)
    for card in cards:
        if total > 21 and card == 11:
            total -= 10   #reducing Ace card value to 1
    return total


while True:
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    player_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]

    while True:
        print(f'Your cards: {player_cards}, Your total is {calculate_total(player_cards)}')
        player_input = input("Do you want to draw another card? (y/n): ")
        if player_input == "y":
            player_cards.append(random.choice(cards))
        else:
            break

        if calculate_total(player_cards) > 21:
            print(f'Your cards: {player_cards}, Your total is {calculate_total(player_cards)}')
            print(f'You bust! Computer Wins!')
            break

    if calculate_total(player_cards) > 21:
        continue

    print(f'Your cards: {player_cards}, Your total is {calculate_total(player_cards)}')

    while calculate_total(computer_cards) < 17:
        computer_cards.append(random.choice(cards))
        print(f"Computer cards: {computer_cards}, total: {calculate_total(computer_cards)}")

    player_total = calculate_total(player_cards)
    computer_total = calculate_total(computer_cards)

    print(f'Your final total is: {player_total}')
    print(f'Computer final total is: {computer_total}')

    if player_total > 21:
        print("You bust! Computer wins!")
    elif computer_total > 21:
        print("Computer bust! You wins!")
    elif player_total > computer_total:
        print("You win!")
    elif player_total < computer_total:
        print("You lose!")
    else:
        print("Its a draw!")

    play_again = input("Would you like to play again? (y/n): ")
    if play_again != "y":
        break

print("Thanks for playing!")
