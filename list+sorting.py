number = []

elem = int(input("Enter the size of list: "))
print(f"Enter {elem} element's: ")

for i in range(elem):
    num = int(input())
    number.append(num)

for i in range(elem):
    for j in range(i+1, elem):
        if number[i] > number[j]:
            temp = number[i]
            number[i] = number[j]
            number[j] = temp

for i in range(elem):
    print(f"{number[i]}", end=" ")