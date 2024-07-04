first = int(input("Enter the first number:"))
operator = input("Enter the operator (+,-,*,/,%):")
second = int (input("enter the second number:"))

if operator == "+":
    print("The Summation is",first+second)
elif operator == "-":
    print("The Substraction is",first-second)
elif operator =="*":
    print("The Multiplication is",first*second)
elif operator =="/":
    print("The Division is",first/second)
elif operator =="%":
    print("The Reminder is",first%second)
else:
    print("invalid operator")