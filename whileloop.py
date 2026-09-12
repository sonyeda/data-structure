# Print numbers from 1 to 10 using a while loop.
i = 1
while i <=10:
  print (i)
  i= i+1

# Print numbers from 10 to 1 using a while loop.
i = 10
while i >= 1:
    print(i)
    i = i - 1
  
# Print all even numbers from 1 to 20.
i = 2
while i <=20:
  print(i)
  i = i +2
  
# Print all odd numbers from 1 to 20.
i= 1
while i<=20:
  print(i)
  i = i+2
  
# Take a number from the user and print numbers from 1 up to that number.
a= 20
i= 1
while i <= a :
  print (i)
  i=i+1
  
# Take a number from the user and print its multiplication table.
a = int(input())
i= 1
while i<= 10:
  print(a , "x", i, "=", a *i)
  i=i+1
  
# Take a number n and calculate the sum of numbers from 1 to n.
n= int(input("enter the number :"))
i = 1
while i<=n :
  print(n, "+", i, "=" ,n+i)
  i=i+1

# Take a number and count how many digits it has.
# Example: 58392 → 5
num = int(input("Enter a number: "))
count = 0
# Convert negative numbers to positive for accurate counting
num = abs(num)
# Special case for zero
if num == 0:
    count = 1
else:
    while num > 0:
        num = num // 10
        count = count + 1

print("Number of digits:", count)
