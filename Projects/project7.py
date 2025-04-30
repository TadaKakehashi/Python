import random

words = ['hangman','cars']
word = random.choice(words)

guessed_letters =[]
tries = 5

hidden_word = ['_']*len(word)

print("--------Welcome to Hangman!---------")
while tries > 0 and '_' in hidden_word:
    print("\nWord:",' '.join(hidden_word))
    print(f"You have {tries} guesses left")
    guess = input("Guess a letter: ")
    
    # Check conditions first so that we dont add garbage values
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter")
        continue
    if guess in guessed_letters:
        print("You have already guessed this word!")
        continue
    #appending the guessed word now after the check, for first pass the guess word will fail second check and then get appended!
    guessed_letters.append(guess)
    
    if guess in word:
        for i, char in enumerate(word):
            if char == guess:
                hidden_word[i] = guess
        print("Correct!")
        if(tries<3):
            tries += 1
        continue
    else:
        tries -= 1
        print("Wrong!")
        print(f'You have {tries} guesses left!')

if '_' not in hidden_word:
    print('\n You guess the word!')
    print('\n ',word)
else:
    print("You lost! The word was: ",word)
