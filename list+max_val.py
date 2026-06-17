number = []

elem = int(input("Enter the size of list: "))
print(f"Enter {elem} elemets of list ")

for i in range(elem):
    num = int(input(f"Enter {i+1} number: "))
    number.append(num)

max = number[0]

for i in range(1,elem):
    if max < number[i]:
        max = number[i]

print(f"Largest number = {max}")