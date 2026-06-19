# list_frequency_count.py
def counting(number, targat):
    count = 0
    for num in number:
        if num == targat:
          count += 1
    return count

number = []
unique = []
size = int(input("Enter the size of list: "))

for i in range(size):
    num = int(input(f"Enter {i+1} element of list: "))
    number.append(num)

for num in number:
    if num not in unique:
        unique.append(num)

for i in range(len(unique)):
    print(f"{unique[i]} appears {counting(number, unique[i])}")