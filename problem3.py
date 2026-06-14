#Ask the user toenter two integers and one float.Convert them all to floats and print 
# the iraverage
# Ask the user to enter two integers and one float

num1 = float(int(input("Enter first integer: ")))
num2 = float(int(input("Enter second integer: ")))
num3 = float(input("Enter a float number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)