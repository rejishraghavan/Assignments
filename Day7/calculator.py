def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def main():
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    print("Addition:", add(first, second))
    print("Subtraction:", subtract(first, second))
    print("Multiplication:", multiply(first, second))
    quotient = divide(first, second)
    if quotient is None:
        print("Division: undefined (cannot divide by zero)")
    else:
        print("Division:", quotient)


if __name__ == "__main__":
    main()
