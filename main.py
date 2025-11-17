def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Goodbye! 👋")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            print("Answer:",add(num1, num2))
        elif choice == '2':
            print( subtract(num1, num2))
        elif choice == '3':
            print(multiply(num1, num2))
        elif choice == '4':
            print( divide(num1, num2))
    else:
        print("Invalid choice. Please select a valid option.")
        # getting inputs
    """
rent= int(input("Enter the total rent of the Flat :"))
food= int(input("Total amount spent on food: "))
energy=int(input("Total units of energy consumed: "))
unit=int(input("Enter the charge per unit: "))
mate=int(input("Enter the number of flatmates: "))
lightbill = energy*unit
share = (food+rent+lightbill)/mate 
print("Each person has to give: ",share)  
"""

