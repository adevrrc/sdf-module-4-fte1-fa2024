"""Demonstrates using exception handling for the purpose of logic.

Usage: python divide_numbers.py
"""

try:
    dividend = int(input("Enter the dividend: "))

    divisor = int(input("Enter the divisor: "))

    if divisor == 0:
        print("The divisor cannot be zero.")
    else:
        quotient = dividend / divisor

        print(f"The quotient is {quotient}.")
except Exception:
    print("You must enter numeric values for both dividend "
          "and divisor.")
