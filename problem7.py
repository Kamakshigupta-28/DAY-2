#Ask the user for a temperature in Celsius (string input).Convert it to float,then calculate and print temperature in Fahrenheit.
#Conversion formula : Fahrenheit Temp = (Celsius Temp∗(9/5))+32
# Ask user for temperature in Celsius (as string)
celsius_str = input("Enter temperature in Celsius: ")

# Convert string to float
celsius = float(celsius_str)

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * (9 / 5)) + 32

# Print result
print("Temperature in Fahrenheit:", fahrenheit)