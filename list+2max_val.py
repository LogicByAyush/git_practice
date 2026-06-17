nums = []
elem = int(input("Enter the size of list: "))

if elem < 2:
    print("List must contain two or more elements")
    
else:
    for i in range(elem):
        num = int(input(f"Enter {i+1} element: "))
        nums.append(num)

    first = nums[0]
    count = 0

    for num in nums:
        if num > first:
            first = num

    for num in nums:
        if num == first:
            count += 1

    if count >= 2:
        second = first
    else:
        second = None

        for num in nums:
            if num != first:
                second = num
                break

        for num in nums:
            if num != first and num > second:
                second = num

    print("Second largest:", second)