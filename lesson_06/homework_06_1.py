chars = input("Enter the text and I'll count the unique characters in it: ")
unique_chars = set(chars)

# print(type(chars))
# print(type(unique_chars))

def unique (unique_chars):
    if len(unique_chars) > 10:
        return True
    else:
        return False
print(unique(unique_chars))


