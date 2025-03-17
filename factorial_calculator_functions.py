def get_non_negative_integer():
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                print("The number must be non-negative. Please try again.")
            else:
                return num
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

def calculate_factorial(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    number = get_non_negative_integer()
    result = calculate_factorial(number)
    print(f"The factorial of {number} is: {result}")

if _name_ == "_main_":
    main()