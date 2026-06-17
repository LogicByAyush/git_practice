def rev_text(text):
    n = len(text)
    rev = ""
    if n != 0:
        rev += text[0]
    text = text[1:n]
    if n == 0:
        return rev
    else:
        return rev_text(text) + rev

text = input("Enter the text: ")
print("Reversed text: ", rev_text(text))