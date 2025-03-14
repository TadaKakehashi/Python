import random

chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '[', ']', '}']
all_letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

char_num = int(input("How many characters do you want? "))
letter_num = int(input("How many letters do you want? "))
num_num = int(input("How many numbers do you want? "))

password = ""
for i in range(char_num):
    char = random.choice(chars)
    password = password + char

for i in range(letter_num):
    letters = random.choice(all_letters)
    password = password + letters

for i in range(num_num):
    num = random.choice(nums)
    password = password + num


print("Your password generated is:", password)
