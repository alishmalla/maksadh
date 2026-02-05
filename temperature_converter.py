temp = float(input("what is the temperature? "))
unit = input("Is it in celsius or Ferhinheit ?(C,F): ")
if(unit=="C"):
    temp= (9*temp)/5+32
    print(f"The temperature in Fahrenheit is: {round(temp,2)}")
elif(unit=="F"):
    temp = (temp-32)*5 / 9
    print(f"The temperature in Celsius is: {round(temp,2)}")
else:
    print(f"{unit} is not a valid unit")
input("press enter to continue...")