# recursion_count_digits.py
def dig_count(digit):
    if digit == 0:
        return 0

    return 1 + dig_count(digit//10)

number = int(input("Enter the number: "))

if number == 0:
    print("The 0 is having 1 digit")
else:
    print(f"The {number} is having {dig_count(number)} digit")