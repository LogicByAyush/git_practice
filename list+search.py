nums = []
count = 0

elem = int(input("Enter the size of list: "))
print(f"Enter {elem} elements: ")

for i in range(elem):
    num = int(input(f"Enter {i+1} term: "))
    nums.append(num)

search = int(input("Enter the number you want to search: "))

for i in range(elem):
    if search == nums[i]:
        print(f"{search} found in list at position {i+1}")
        count = 1
        break

if count == 0:
    print("Not found in list")