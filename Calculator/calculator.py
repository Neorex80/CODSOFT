from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def get_operation_choice():
    print(Fore.CYAN + "\nChoose an operation:")
    print(Fore.CYAN + "1. Addition (+)")
    print(Fore.CYAN + "2. Subtraction (-)")
    print(Fore.CYAN + "3. Multiplication (*)")
    print(Fore.CYAN + "4. Division (/)")
    return input(Fore.YELLOW + "Enter your choice (1/2/3/4): ")

def main():
    print(Fore.CYAN + "Welcome to the Simple Calculator!" + Style.RESET_ALL)

    while True:
        try:
            num1 = float(input(Fore.YELLOW + "Enter the first number: "))
            num2 = float(input(Fore.YELLOW + "Enter the second number: "))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter numeric values.")
            continue

        choice = get_operation_choice()

        if choice == '1':
            result = add(num1, num2)
            operation = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "*"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "/"
        else:
            print(Fore.RED + "Invalid choice. Please select a valid operation.")
            continue

        print(Fore.GREEN + f"\nResult: {num1} {operation} {num2} = {result}" + Style.RESET_ALL)

        play_again = input(Fore.CYAN + "Do you want to perform another calculation? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print(Fore.GREEN + "Exiting the calculator. Thanks for using it!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()
