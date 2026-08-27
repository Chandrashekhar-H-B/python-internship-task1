# Task 6: Palindrome Check

text = input("Enter a word: ")

clean_text = text.lower()

if clean_text == clean_text[::-1]:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")
