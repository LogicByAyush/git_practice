size = 5
number = []

print(f"Enter {size} elements ")

for i in range(size):
    num = int(input(f"Enter {i+1} element: "))
    number.append(num)

largest = second = float("-inf")

for num in number:
    if num > largest:
        second = largest
        largest = num
    elif num == largest:
        second = num
    elif num > second:
        second = num

print(f"First largest number is {largest}.\nSecond largest number in list is {second}.")