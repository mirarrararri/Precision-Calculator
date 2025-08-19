# MATH OPERATIONS IMPLEMENTING USER-DEFINED METHOD (Simple Calculator with Exception Handling)
# Exceptions: ZeroDivisionError, ValueError

#validate if input are integers
def validate_integers(val1, val2):
    if not (val1.isdigit() and val2.isdigit()):
        print("Error message: Invalid input data.\nInput must be an integer value.")
        return False
    return True

#validate operation input
def validate_operation(op):
    if not (op.isalpha() and op.lower() in ['a', 'b', 'c', 'd']):
        print("Error message: Invalid operation.\nInput operation must be frm a to d only.")
        return False
    return True

#Calculate sum and return result
def calcSum(a, b):
    return a + b

#Calculate difference and print result
def calcDifference(a, b):
    print(f"Result: Difference of {a} and {b} is {a - b}")

# Calculate product and print result
def calcProduct(a, b):
    print(f"Result: Product of {a} and {b} is {a * b}")

# Calculate quotient and return result
def calcQuotient(a, b):
    return a / b

#input
def main():
    try:
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")

        if not validate_integers(num1, num2):
            return

        a = int(num1)
        b = int(num2)

        operation = input("Choose an operation [a] Add [b] Subtract [c] Multiply [d] Divide: ")

        if not validate_operation(operation):
            return

        op = operation.lower()

        if op == 'a':
            result = calcSum(a, b)
            print(f"Result: Sum of {a} and {b} is {result}")
        elif op == 'b':
            calcDifference(a, b)
        elif op == 'c':
            calcProduct(a, b)
        elif op == 'd':
            try:
                result = calcQuotient(a, b)
                print(f"Result: Quotient of {a} and {b} is {result}")
            except ZeroDivisionError:
                print("Error: cannot divide by zero.")

    except ValueError:
        print("Error: Invalid input. Please enter whole numbers only.")

#output To run the program
main()




