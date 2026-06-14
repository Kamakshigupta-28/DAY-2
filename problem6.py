#Write a program to swap values of two numbers entered by the user
# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swapping
a, b = b, a

# Output after swapping
print("After swapping:")
print("First number =", a)
print("Second number =", b)