text = input("Enter the text: ")
text = text.lower()
Text = text 
rev = ""

for i in range(len(text)-1, -1, -1):
    rev += text[i]

if rev == Text:
    print("Palindrome")
else:
    print("Not Palindrome")