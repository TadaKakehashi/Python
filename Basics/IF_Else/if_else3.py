#Pounds to Kilos or Kilos to Pounds

weight = int(input("Enter your weight: "))
weigth_metric = str(input("(L)bs or (K)g: ")).upper()

if weigth_metric == "L":
    kilogram = weight/2.20462
    print(f'Your weight in kilogram is {kilogram:.2f}Kg')
elif weigth_metric == "K":
    pounds = weight*2.20462
    print(f'Your weight in pounds is {pounds:.2f}lbs')
else:
    print("Wrong input")