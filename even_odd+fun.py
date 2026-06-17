def is_even(num):
    return num % 2 == 0

number = int(input("Enter the number: "))
print(f"{number} is an even number : {is_even(number)}")