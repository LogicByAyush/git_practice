num1 = int(input("Enter a number: "))
num = num1
rev = 0

while (num1 > 0):
    rem = num1 % 10
    rev = rev * 10 + rem
    num1 = num1 // 10

print(f"The reverse of {num} is {rev}")