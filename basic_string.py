

# 🔹 Basic Python String Concepts
# 1. Creating Strings
# python
# Copy
# Edit
# s1 = "Hello"
# s2 = 'World'
# print(s1,s2)




# 2. Multiline Strings
# python
# Copy
# Edit
# multi = """This is
# a multiline
# string

# python very easy language ."""

# print(multi)


# 3. Accessing Characters
# python
# Copy
# Edit
# s = "Python"
# #    0  1   2 3 4 5  starting positive  +
# #    -5 -4 -3 -2 -1    ending nagative  -

# print(s[5])   # P
# print(s[-5])  # o


# 4. String Slicing
# python
# Copy
# Edit
# s = "Programming" 
# print(s[5:10])   # ammin
# print(s[0:])    #rogramming 
# print(s[:10])    # Programmin


# 5. String Length
# python
# Copy
# Edit

# a="_ashish"
# print(len(a))  # 13
# 🔹 Intermediate String Concepts


# 6. String Methods
# python
# Copy
# # Edit
# s = " how are you guys "

# print(s.strip())      # how are you guys
# print(s.upper())      # " HELLO WORLD "
# print(s.lower())      # " hello world "
# print(s.title())      # " Hello World "
# print(s.replace("guys", "friends"))  # " hello Python "




# 7. Searching in Strings
# python
# Copy
# # Edit
# s = "Python"
# s1="python is very easy programing language"
# print("django" in s)       # True
# print(s.find("Python"))     # 10
# print(s.index("Python"))       # 7


# 8. String Formatting
# Old-style:
# python
# Copy
# Edit
name = "Alice"
age = 25
# print("My name is %s and I am %d years old" % (name, age))
# str.format()
# python
# Copy
# Edit
# print("My name is {} and I am {} years old".format(name, age))
# f-strings (Python 3.6+)
# python
# Copy
# Edit
# print(f"My name is {name} and I am {age} years old")


# 9. Splitting and Joining
# python
# Copy
# Edit
# sentence = "Python is awesome"
# words = sentence.split()  # ['Python', 'is', 'awesome']
# joined = "-".join(words)  # "Python-is-awesome"
# 🔹 Advanced String Concepts

# 10. String Immutability
# Strings in Python are immutable. You can't change them in-place:

# python
# Copy
# Edit
# s = "Hello"
# # s[0] = 'Y'  # ❌ Error
# s = "Y" + s[1:]  # ✅ New string


# 11. String Encoding & Decoding
# python
# Copy
# Edit
# s = "hello"
# encoded = s.encode('utf-8')   # b'hello'
# decoded = encoded.decode('utf-8')  # "hello"
# print(decoded)
# print(encoded)

# 12. Regular Expressions (regex) with strings
# python
# Copy
# Edit
# import re
# text = "The rain in Spain"
# result = re.findall(r"\b\w{4}\b", text)  # ['rain', 'Spain']


# 13. String Translation (Advanced Replace)
# python
# Copy
# Edit
table = str.maketrans("aeiou", "12345")
s = "aeiou"
print(s.translate(table))  # h2ll4 w4rld