import string

def alphabet_position(text_string):
    dict1 = {value: (int(key) + 1) for key, value in enumerate(list(string.ascii_lowercase))}
    return ", ".join([str(dict1[alp]) for alp in list(text_string.lower()) if alp.isalpha()])
_string = input("English: ")
print("Encoded: "+ alphabet_position(_string))
