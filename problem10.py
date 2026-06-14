#Take a decimal number as input (like 45.78) and output its :
#integer part-45
#fractional part-.78

# Take decimal number as input
num = float(input("Enter a decimal number: "))

# Get integer part
integer_part = int(num)

# Get fractional part
fractional_part = num - integer_part

# Print results
print("Integer part =", integer_part)
print("Fractional part =", fractional_part)