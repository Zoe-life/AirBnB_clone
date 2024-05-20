#!/usr/bin/python3

"""
The implementation of this script introduces a simple
"text-based user interface for the Airbnb clone."
The users are able to engage with features such as:
a.) User registration
b.) Login
c.) Listing operations e.g listing searchers
"""


def main():
    """
    The Airbnb clone console's entry point
    """
    print("Welcome to the Airbnb Clone console")
    print("(hbnb) ", end="")

    while True:
        user_input = input()
    # Handles user input (to be implemented)
    if user_input.lower() == "quit":
        break
    print("(hbnb) ", end="")


if __name__ == "__main__":
    main()
