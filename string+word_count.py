text = input("Enter the text: ")
count = 0
n = len(text)

for i in range(n):
    if text[i] == " ":
        count += 1
    if text[i-1] == " " and text[i] == " ":
        count -= 1

print(f"word = {count + 1}")