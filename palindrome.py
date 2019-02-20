def input_message(prompt):
    return input(prompt)

#set letters
def letters_only(entry):
    """only return letters into a string with no punctuation or caps"""
    letters = "abcdefghijklmnopqurstuvwxyz"
    letters = letters.lower() + letters.upper()

    new_entry = ""
    for char in entry:
        if char in letters:
            new_entry = new_entry + char
    return new_entry.lower()

# print(letters_only(entry))

quit = "false"

entry = letters_only(input_message("Enter a word or sentence(s):  "))
if entry == entry[::-1]:
    print("is a palindrome")
else:
    print("is not a palindrome")







