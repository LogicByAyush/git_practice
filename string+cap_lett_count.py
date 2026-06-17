text = input("Enter the text: ")
count = 0

for ch in text:
    if 'A' <= ch <= 'Z':
        count += 1

if count == 0:
    print("No uppercase letter found in text.")
else:
    print(f"Uppercase letters = {count}")