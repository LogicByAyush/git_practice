num1 = int(input("Enter a number: "))
num = num1
le = len(str(num)) 
arm = 0 
 

while (num1 > 0):
    dig = num1 % 10 
    arm += dig ** le 
    num1 = num1 // 10

if num == arm:
    print("Armstrong number")
else:
    print("Not Armstrong number")