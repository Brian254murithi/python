text = "Hello"
text1 = "THERE"

print(text)

# Accessing an element in a string
print(text[1])
print(text[4])

# Modifying a string
print(text.upper())
print(text1.lower())

# size/Length of a string
print(len(text))

# String Concatenation - Combining Strings
print(text + text1)
print(text + " " + text1)

# Assignment
# 1. Reassign a string
# 2. Deleting string

# Reassigning a string
s = "Hello O World"
result_string =""
index = 6

for i in range(len(s)):
     if i !=index:
        result_string+=s[i]

# How to Delete a string
print(result_string)


