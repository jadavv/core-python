

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
# sssss

# svkmvvm
# python very easy language ."""

# print(multi)


# 3. Accessing Characters
# python
# Copy
# Edit
# s = "python"
#    0  1   2 3 4 5  starting positive  +
#    -5 -4 -3 -2 -1    ending nagative  -

# print(s[1])   # y
# print(s[-4])  # t
# print("skss")

# 4. String Slicing
# python
# Copy
# # Edit
# s = "Programming"  # 11 
# print(s[2:])   #ogramming 
# print(s[1:])    #rogramming
# print(s[10:])    # Programmin

# 5. String Length
# python
# Copy
# Edit

# a="_ashishhiralshahal_655dcfct"
# print(len(a))  # 13
# 🔹 Intermediate String Concepts


# 6. String Methods
# python
# Copy
# # Edit
# s = " how are you hello  mahendra "

# print(s.strip())      # how are you guys
# print(s.upper())      # " HELLO WORLD "
# print(s.lower())      # " hello world "
# print(s.title())      # " Hello World "
# print(s.replace("vinay", "mahendra"))  # " hello Python "
# # print(s.replace("shehal", "riya"))  # " hello Python "




# 7. Searching in Strings
# python
# Copy
# # Edit
# s = "Python  is good"
# s1="python is very easy programing language and is interpreted laguage "
# print("easy" in s1)       #        m 59  s58 h 59 
# print(s1.find("is"))     # 7
# print(s1.index("laguage"))       # 
# print(s1.index("easy"))       # 13


# 8. String Formatting
# Old-style:
# python
# Copy
# # Edit
# name = "cat"
# age = 10
# print(" name is %s and I am %d years old" % (name, age))
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
# sentence = "Python is awesome and easy"
# words = sentence.split()  # ['Python', 'is', 'awesome']
# joined = "hs".join(words)  # "Python-is-awesome"
# print(sentence)
# print(words)
# print(joined)
# 🔹 Advanced String Concepts

# 10. String Immutability
# Strings in Python are immutable. You can't change them in-place:

# python
# Copy
# Edit
s = "Hello"
# s[0] = 'Y'  # ❌ Error
# s = "Y" s[1:]  # ✅ New string


# 11. String Encoding & Decoding
# python
# Copy
# Edit
# s = "hiral@123"
# encoded = s.encode('utf-8')   # b'hello'
# decoded = encoded.decode('utf-8')  # "hello"
# print(encoded)
# print(decoded)

# 12. Regular Expressions (regex) with strings
# python
# Copy
# Edit
# import re
# text = "The rain in Spain hiralllll  shehallll"
# result = re.findall(r"\b\w{9}\b", text)  # ['rain', 'Spain']
# print(result)

# 13. String Translation (Advanced Replace)
# python
# Copy
# Edit

# table = str.maketrans("aeiou", "56789")
# s = "aeiou"
# print(s.translate(table))  