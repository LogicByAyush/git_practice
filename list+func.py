def largest(num):
    big = num[0]
    for i in range(1,len(num)):
        if big < num[i]:
            big = num[i]
    return big

numbers = []

for i in range(5):
    number = int(input(f"Enter {i+1} element: "))
    numbers.append(number)

print(f"Largest number among the list is {largest(numbers)}")