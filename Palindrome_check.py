text = input("Input the text you want to check: ")
palindrome = ""
is_palindrome = False
text = text.lower()
text = text.replace(" ", "")
if len(text) == 0:
    is_palindrome = False
for ch in reversed(text):
    palindrome += ch
if palindrome == text:
    is_palindrome = True
print("The reverse text is: ", palindrome, "\n", "the original text is: ", text, "\n", "Is the text a palindrome? ", is_palindrome)
