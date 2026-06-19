#list_common_elements.py
list1 = []
list2 = []

size = int(input("Enter the size of list one and list two: "))
print(f"-----Enter {size} element of list 1------")

for i in range(size):
    num1 = int(input(f"Enter {i+1} element of list 1: "))
    list1.append(num1)

print(f"------Enter {size} element of list 2------")

for i in range(size):
    num2 = int(input(f"Enter {i+1} element of list 2: "))
    list2.append(num2)

for num1 in list1:
    if num1 in list2:
        print(num1)