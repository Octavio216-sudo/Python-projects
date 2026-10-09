first_word = input("Input the first word: ")
second_word = input("input the second word: ")
for ch in first_word:
    if ch in second_word:
        second_word = second_word.replace(ch, "", 1)
if second_word == "":
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")