#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: April 2022
# This is a is it a square or rectangle program


def main():
    # This is a square or rectangle program
    # input
    print("This progrma will tell you if your shape is a square or not!")
    print("Note: Do not input Letters, 'A', 'B', '...', etc")
    print("Note: Decimals DO work in this program")
    width_string = input("What is the length of your object?: ")
    length_string = input("What is the width of your object?: ")
    # process & output
    try:
        width = float(width_string)
        length = float(length_string)

        if width == length:
            print("\nYour object is a square!")
        else:
            print("\nYour object is a rectangle!")
    except Exception:
        print("Invalid Input")
    print("\nDone.")


if __name__ == "__main__":
    main()
