ask = float(input("Please Enter your weight: "))
ask2= input("Is the weight in (K)g or (L)bs?: ")


pounds = 2.20462

if ask2.upper() == "L":
    print("Your weight in kilogram is:", float (ask/pounds))

elif ask2.upper() == "K":
    print("Your weight is:", float(ask2*pounds))

