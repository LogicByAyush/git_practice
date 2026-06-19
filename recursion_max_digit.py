#recursion_max_digit.py
def max_digit(num):
    if num == 0:
        return 0
    last = num % 10
    rest = max_digit(num//10) 
    if last > rest:
        return last
    else:
        return rest

num = int(input("Enter the number: "))
print(f"largest digit in {num} is {max_digit(num)}.")