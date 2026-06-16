def is_even(num):
    return num % 2 == 0
num = int(input("Enter a number to check if it's even or odd: "))
print(f"The number {num} is {'even' if is_even(num) else 'odd'}.")