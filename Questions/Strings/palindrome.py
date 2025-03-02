def isPalindrome(word):
    word = word.lower()
    temp = word[::-1]

    return word == temp


print(isPalindrome('madam'))
print(isPalindrome('RaceCar'))
print(isPalindrome('HorseShoe'))