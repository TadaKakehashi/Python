#Check how many vowels are their in the word entered by the user
word = input("Enter: ")

def check(word):
    count = 0
    for char in word:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            count += 1
    print(f'number of vowels in {word} is {count}')

check(word)
