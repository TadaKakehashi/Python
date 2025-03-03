def price(cost, tax=0.19):
    return f'{cost} : tax is: {tax}'


def generateNumber(count_code, area_code, first4_d, last4_d):
    return f"{count_code}-{area_code}-{first4_d}-{last4_d}"


def add_number(*args):
    return sum(args)


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}:{value}')


price(10)  #default_arguments

phone_num = generateNumber(1, 312, 431, 542)
print(phone_num)
#keyword_arguments
#ARBITARY ARGUMENTS
print(add_number(1, 2, 3, 4))

print_address(street="123 Nk Street",
              city="Mongolia",
              state="MI",
              zip="5412")
