name = input("Enter your name: ")
length = len(name)

if length < 4:
    print(f'name must be 3 characters long')
elif length > 50:
    print(f'name must be 50 characters long')
else:
    print('name looks good!')