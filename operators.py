





# Arithmetic operators (+, -, *, /, %, **, //)
# print(2 ** 3) # Exponentiation
# print(16 // 3) # floor division
# Assignment operators  ==
# Comparison operators ===
# Logical operators -> and, or, not
# Identity operators -> is, is not
# Membership operators -> in, not in
# Bitwise operators
"""
Arithmetic Operators
python
Copy
Edit
print(2 + 3)    # Addition: 5
print(10 - 4)   # Subtraction: 6
print(5 * 3)    # Multiplication: 15
print(10 / 2)   # Division: 5.0
print(10 % 3)   # Modulus: 1
print(2 ** 3)   # Exponentiation: 8
print(16 // 3)  # Floor Division: 5
=================================================================
Assignment Operators
python
Copy
Edit
x = 5  # Assign value
x += 3 # Equivalent to x = x + 3 (x becomes 8)
x -= 2 # Equivalent to x = x - 2 (x becomes 6)
x *= 2 # Equivalent to x = x * 2 (x becomes 12)
x /= 3 # Equivalent to x = x / 3 (x becomes 4.0)
x %= 3 # Equivalent to x = x % 3 (x becomes 1.0)
========================================================================
Comparison Operators
python
Copy
Edit
a = 10
b = 20
print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= 10) # True
print(b <= 15) # False
===============================================================================
Logical Operators
python
Copy
Edit
x = True
y = False
print(x and y) # False
print(x or y)  # True
print(not x)   # False
========================================================================================
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