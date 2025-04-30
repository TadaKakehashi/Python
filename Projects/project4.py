import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','+','-']

print("Welcome to the Password Generator Program!")
nr_letter = int(input("How many letters would you like to generate? "))
nr_number = int(input("How many numbers would you like to generate? "))
nr_symbol = int(input("How many symbols would you like to generate? "))

password = []
for i in range(nr_letter):
    password += random.choice(letters)

for j in range(nr_number):
    password += random.choice(numbers)

for k in range(nr_symbol):
    password += random.choice(symbols)


random.shuffle(password)

password = ''.join(password)

print("Your generated password is: " + password)
