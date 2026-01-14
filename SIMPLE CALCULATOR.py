def main(): 
    print("Welcome to the Simple Calculator!")
    while True:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = num1 + num2
                operation = '+'
            elif choice == '2':
                result = num1 - num2
                operation = '-'
            elif choice == '3':
                result = num1 * num2
                operation = '*'
            elif choice == '4':
                if num2 != 0:
                    result = num1 / num2
                    operation = '/'
                else:
                    print("Error! Division by zero.")
                    continue

            print(f"{num1} {operation} {num2} = {result}")
        else:
            print("Invalid input. Please select a valid operation.")
            main()
        




