# list_remove_duplicates.py
number = []
unique = []
size = int(input("Enter the size of list: "))

for i in range(size):
    num = int(input(f"Enter {i+1} element of list: "))
    number.append(num)

print(f"Your list is {number}")

for num in number:
    if num not in unique:
        unique.append(num)

print(f"After deleted all duplicates the list is now {unique}")