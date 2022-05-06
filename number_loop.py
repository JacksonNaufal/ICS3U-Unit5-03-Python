#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: March 2022
# This is fahrenheit to celsius converter


def area_function(width, length):

    area = round((width * length) / 2)

    # output
    print("The area is {0}, base = {1}, height = {2}!".format(area, length, width))


def main():

    # call function

    width_string = input("Enter Your width (mm): ")
    length_string = input("Enter Your length (mm): ")
    try:

        width = int(width_string)
        length = int(length_string)
        area_function(width, length)

    except Exception:
        print("\nThat was not an integer!")

    print("\nDone.")


if __name__ == "__main__":
    main()
