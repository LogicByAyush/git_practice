# Perfect_Number
num = int(input("Enter the number: "))
factor_sum = 0

for i in range(1, (num//2)+1):
    if num % i == 0:
        factor_sum += i

if num == factor_sum:
    print("Perfect number")
else:
    print("Not Perfect Number")