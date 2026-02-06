operator = input("enter an operator for calculation: ")

num1=int(input("enter 1st digit: "))
num2=int(input("enter 2nd digit: "))
if operator== "+":
    print(num1+num2)
elif operator =="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
else:
    print(f"{operator} is not a valid operator")
input("press enter to continue...")