"""Demonstrates how to refactor to eliminate duplication.

Usage: python divide_numbers.py
"""

number = 5
message = ""

if number == 5:
    #print("*****")
    #print("Five")
    message = "Five"
    #print("*****")
elif number == 7:
    #print("*****")
    #print("Seven")
    message = "Seven"
    #print("*****")
else:
    #print("*****")
    #print("Not 5 or 7")
    message = "Not 5 or 7"
    #print("*****")

border_line = "*" * 5

print(border_line)
print(message)
print(border_line)
