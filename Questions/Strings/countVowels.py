
def count_vowels(string):
    countV = 0
    for char in string:
        if char.lower() in 'aeiou':
            countV += 1
    return countV

result = count_vowels("RayKirigaya")
print(f'The number of vowels in the string given: {result}')
