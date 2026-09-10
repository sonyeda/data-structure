
# Simple Calculator
# Take two numbers and an operator (+, -, *, /) and perform the operation
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


# red   → Stop
# yellow → Wait
# green → Go

a = "red"
b = "yello"
c= "green"
signal = input()
if a == "red":
  print("stop")
elif b == "yello":
  print("wait")
elif c == "green":
  print("go")



# Largest of Three Numbers
# Take three numbers and find the largest without using max()
a= 2
b = 3
c =6
if a>b and a >c :
  print ("yes")
elif b >a and b>c :
  print("yes1")
elif c>a and c>b :
  print("yes3")
