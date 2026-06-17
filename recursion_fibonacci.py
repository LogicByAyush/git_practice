#recursion_fibonacci
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
    
number = int(input("Enter the number: "))
print(fibonacci(number))