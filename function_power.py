# function_power
def power(n, m):
    if n == 0:
        return 0
    elif m == 0:
        return 1
    else:
        return n*power(n,m-1)
    
number = int(input("Enter the number: "))
num_pow = int(input("Enter the power of number: "))
print(f"{number} to the power {num_pow} is equal to {power(number, num_pow)}")