print("Select an operation")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. REMAINDER")

operation = input()
if operation == "1":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The sum is {num1 + num2}")
elif operation == "2":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"The difference is {num1 - num2}")
elif operation == "3":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The product is {num1 * num2}")
elif operation == "4":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The division is {num1 / num2}")
elif operation == "5":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The remainder is {num1%num2}")
else:
    print("invalid operation")
