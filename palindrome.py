def is_palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

text = input("Enter a string to check if it is a palindrome: ")
if is_palindrome(text):
    print(f'"{text}" is a palindrome.')
else:
    print(f'"{text}" is not a palindrome.')
