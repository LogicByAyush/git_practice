text = input("Enter the word: ")
count = 0

for ch in text:
    if ch in "aeiouAEIOU":
        count += 1

if count == 0:
    print("No vowels found")
else:
    print(f"Vowels = {count}")