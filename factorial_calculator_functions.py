def get_non_negative_integer() -> int:
    """
    Prompts the user to enter a non-negative integer.
    Validates the input to ensure it is a valid non-negative integer.
    Returns:
        int: The validated non-negative integer input from the user.
    """
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                print("Error: Please enter a non-negative integer.")
            else:
                return num
        except ValueError:
            print("Error: Invalid input. Please enter an integer.")

def calculate_factorial(n: int) -> int:
    """
    Calculates the factorial of a given non-negative integer.
    Args:
        n (int): The non-negative integer whose factorial is to be calculated.
    Returns:
        int: The factorial of the given number.
    """
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    """
    Main function to execute the factorial calculation program.
    """
    number = get_non_negative_integer()
    result = calculate_factorial(number)
    print(f"The factorial of {number} is: {result}")

if __name__ == "__main__":
    main()
