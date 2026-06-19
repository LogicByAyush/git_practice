# recursion_product_digits.py
def product_digit(num):
    if num == 0:
        return 1
    return num % 10 * product_digit(num // 10)

number = int(input("Enter the number: "))
print(f"product of all digit of {number} is {product_digit(number)}")