def reverseString(string):
    rev_string = ""
    for char in string:
        rev_string = char + rev_string
    print(rev_string)


reverseString("Hello World")
