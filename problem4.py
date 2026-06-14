#The user enters a string containing a number(e.g.,).Convert it to:"45"
# an integer
# a float
# a string again 
# Print all three values with their types
# User enters a number as string
num_str = input("Enter a number: ")  

# Convert to integer
num_int = int(num_str)

# Convert to float
num_float = float(num_str)

# String again
num_string = str(num_str)

# Print values with their types
print(num_int, type(num_int))
print(num_float, type(num_float))
print(num_string, type(num_string))