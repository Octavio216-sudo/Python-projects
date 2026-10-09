text = input("Input the text you want to encrypt: ")
shift = int(input("Input the amount you want to shift each letter in the text(1-25): "))

for char in text:
    if char.isalpha():
        if char.islower():
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    else:
        new_char = char
    print(new_char, end="")