"""
Description: Demonstrates handling file related exceptions.
Author: Damien Altenburg
Date: 2023-10-1
Usage: python working_with_files.py
"""

from os import path

script_directory = path.dirname(path.realpath(__file__))
filename = "data.txt"
file_path = f"{script_directory}/{filename}"
data_file = None

try:
    with open(file_path, "r") as data_file:
        for record in data_file:
            print(record)
except FileNotFoundError:
    # Log error a file
    # SMS message
    print(f"The {filename} was not found.")
except PermissionError:
    print(f"The user you are logged in as does "
          "not have permission to the file.")

input("Press <enter> to continue...")
