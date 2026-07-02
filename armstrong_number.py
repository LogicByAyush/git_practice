#Q10_Armstrong_Number.py
num = int(input("Enter the number: "))
number = num

digit = len(str(number))
armstrong = 0

while num > 0:
    last = num % 10
    armstrong += pow(last, digit)
    num //= 10

if number == armstrong:
    print("Armstrong number")
else:
    print("Not an armstrong number")