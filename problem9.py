#Ask the user for: Principal (P), Rate(R), Time(T).Convert all to float and compute simple interest :
# SI=(P∗R∗T)/100
# Ask user for Principal, Rate, and Time
P = float(input("Enter Principal (P): "))
R = float(input("Enter Rate (R): "))
T = float(input("Enter Time (T): "))

# Calculate Simple Interest
SI = (P * R * T) / 100

# Print result
print("Simple Interest =", SI)