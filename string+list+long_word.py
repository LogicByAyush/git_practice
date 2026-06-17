names = []
print("Enter five names: ")
for i in range(5):
    name = input(f"Enter {i+1} name: ")
    names.append(name)

long_name = names[0]

for i in range(1, len(names)):
    if len(long_name) < len(names[i]):
        long_name = names[i]

print(f"longest name is = {long_name}")