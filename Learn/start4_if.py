#logical operators or (at eleast one true), and (both true), not (inverses value)

price = 5
print(price > 10 or price < 30)

#if statements 

temperature =  int(input("Enter the temperature in Celcius: "))

if temperature > 30:
    print("It's a hot day")

elif temperature >=20:
    print("It's not too hot")

elif temperature >=10:
    print("It's snowing")

else: #If none of the condition is true
    print ("It's a cold day")