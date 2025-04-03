





# Arithmetic operators (+, -, *, /, %, **, //)
# print(2 ** 3) # Exponentiation
# print(16 // 3) # floor division
# Assignment operators  ==
# Comparison operators ===
# Logical operators -> and, or, not
# Identity operators -> is, is not
# Membership operators -> in, not in
# Bitwise operators

# Arithmetic Operators
# python
# Copy
# Edit
# print(3 + 3)    # Addition: 6
# print(15 - 4)   # Subtraction: 11
# print(6 * 3)    # Multiplication: 18
# print(10 / 5)   # Division: 2.0
# print(100 % 2)   # Modulus: 0
# print(2 ** 2)   # Exponentiation: 4  2*2*2*2*2*2*2*2* = 256
# print(12 // 2)  # Floor Division:6 
# =================================================================

# Assignment Operators
# python

# multi  line code  shurtcut  ctrl +alt
# x = 5  # Assign value
# x += 3 # Equivalent to x = x + 3 (x becomes 8)
# print(x)

# x = 5  # Assign value

# x -= 2 # Equivalent to x = x - 2 (x becomes 6)
# print(x)
# x = 5  # Assign value

# x *= 2 # Equivalent to x = x * 2 (x becomes 12)
# print(x)

# x /= 3 # Equivalent to x = x / 3 (x becomes 4.0)
# print(x)
# x = 15  # Assign value

# x %= 7 # Equivalent to x = x % 3 (x becomes 1.0)  
# print(x)

# ========================================================================
# Comparison Operators
# python
# Copy
# Edit
# a = 25
# b = 41
# print(a == b)  
# print(a != b)  
# print(a > b)   
# print(a < b)   
# print(a >= 10) 
# print(b <= 15)

# ===============================================================================
# Logical Operators
# python
# Copy
# Edit

# AND (and) → Both must be true ✅✅ → True, otherwise False.     

# Example: "I will go outside if it's sunny AND I have free time."

# OR (or) → At least one must be true ✅❌ or ❌✅ or ✅✅ → True.    

# Example: "I will eat ice cream if it's hot OR I feel like it."

# NOT (not) → Reverses the truth.

# Example: "If I am NOT tired, I will study."
x = False
y = False
# print(x and y) # False 
print(x or y)  # True
# print(not x)   # False

"""========================================================================================
Identity Operators
python
Copy
Edit
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a is c)    # True (same object in memory)
print(a is b)    # False (different objects, even with same values)
print(a is not b) # True
==========================================================================================
Membership Operators
python
Copy
Edit
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)    # True
print(6 not in numbers) # True
==============================================================================================
Bitwise Operators
python
Copy
Edit
a = 5  # 0101 in binary
b = 3  # 0011 in binary

print(a & b)  # 1 (0001) - AND
print(a | b)  # 7 (0111) - OR
print(a ^ b)  # 6 (0110) - XOR
print(~a)     # -6 (inverts bits)
print(a << 1) # 10 (shifts left by 1)
print(a >> 1) # 2 (shifts right by 1)
======================================================================================================
"""