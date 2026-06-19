# recursion_count_digit_occurrence.py
def count_digit(num, target):
    if num == 0:
        return 0
    last = num % 10
    count = count_digit(num//10, target)
    if last == target:
        return count + 1
    return count

number = int(input("Enter the number: "))
digit_c = int(input("Enter the digit: "))
print(f"Digit {digit_c} appears {count_digit(number, digit_c)} times in {number}.")