# Precision-Calculator
Python-based tool that performs basic math operations- addition, subtraction, multiplication, and division  with reliable input validation and error handling to ensure accurate and safe calculations every time.

Features:
- Addition, Subtraction, Multiplication, and Division operations
- Input validation for numbers and operation choice
- Handles common errors such as:
ValueError → when input is not a number
ZeroDivisionError → when trying to divide by zero
- User-friendly error messages
- Structured using functions for better code readability

Purpose:
The purpose of this program is to perform basic arithmetic operations (addition, subtraction, multiplication, and division) while ensuring input validation and robust error handling.
It allows users to enter two numbers and choose an operation, with safeguards against:
- Invalid inputs (non-integers)
- Invalid operation choices
- Division by zero
This makes it a reliable and beginner-friendly calculator program for learning user-defined methods and exception handling in Python.

Example Usage:
- Valid Input
Enter first number: 12
Enter second number: 4
Choose an operation [a] Add [b] Subtract [c] Multiply [d] Divide: c
Result: Product of 12 and 4 is 48

- Invalid Input (non-integer)
Enter first number: ten
Enter second number: 5
Error message: Invalid input data.
Input must be an integer value.

- Division by Zero
Enter first number: 10
Enter second number: 0
Choose an operation [a] Add [b] Subtract [c] Multiply [d] Divide: d
Error: cannot divide by zero.

