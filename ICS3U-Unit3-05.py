# Copyright (c) 2022 Emmanuel Fofeyin All rights reserved

# Created by: Emmanuel
# Created on: October 2022
# ICS3U-Unit3-05.py File, learning  about select cases in python (^_^).


def main():

    # input and variables
    month_number = int(input("Enter the number of the month(ex: 12 for December): "))

    # process and output
    print("")
    match month_number:
        case 1:
            print("January".format(month_number))
        case 2:
            print("February".format(month_number))
        case 3:
            print("March".format(month_number))
        case 4:
            print("April".format(month_number))
        case 5:
            print("May".format(month_number))
        case 6:
            print("June".format(month_number))
        case 7:
            print("July".format(month_number))
        case 8:
            print("August".format(month_number))
        case 9:
            print("September".format(month_number))
        case 10:
            print("October".format(month_number))
        case 11:
            print("November".format(month_number))
        case 12:
            print("December".format(month_number))
        case _:
            print("The number has to be between 1 and 12.")

    print("\n\nDone.")


if __name__ == "__main__":
    main()
