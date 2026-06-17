text = input("Enter the text: ")
letter = input("Enter the character: ")

count = 0
text = text.lower()
letter = letter.lower()

for ch in text:
    if ch == letter:
        count += 1

if count == 0:
    print("character is not found in text.")
else:
    print(f"{letter} appears {count} times.")