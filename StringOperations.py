#Q6-String Operations 

# Python Code-
original_string = "Hello, My Name is Jiten"

uppercase_string = original_string.upper()
print("Uppercase:", uppercase_string)

lowercase_string = original_string.lower()
print("Lowercase:", lowercase_string)

replaced_string = original_string.replace("World", "Python")
print("Replaced:", replaced_string)

split_string = original_string.split(", ")
print("Split:", split_string)

joined_string = ", ".join(split_string)
print("Joined:", joined_string)

reversed_string = original_string[::-1]
print("Reversed:", reversed_string)

substring = original_string[18:23]
print("Substring:", substring)


# Output
# Uppercase: HELLO, MY NAME IS JITEN
# Lowercase: hello, my name is jiten
# Replaced: Hello, My Name is Jiten
# Split: ['Hello', 'My Name is Jiten']
# Joined: Hello, My Name is Jiten
# Reversed: netiJ si emaN yM ,olleH
# Substring: Jiten
