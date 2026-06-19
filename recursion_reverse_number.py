# recursion_reverse_number.py
def digit_count(num):
    if num == 0:
        return 0
    return 1 + digit_count(num // 10)

def reverse_number(num):
    if num == 0:
        return 0
    last = num % 10
    dig = digit_count(num // 10)
    return last * 10 ** dig + (reverse_number(num // 10))

number = int(input("Enter the number: "))
print(f"Reverse of {number} is {reverse_number(number)}.")