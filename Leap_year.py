#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 11, 2021
# Determines if a given year is leap or not


def main():

    # Input
    user_input = (input("Enter a year: "))
    try:
        user_year = int(user_input)
        # Process
        operation1 = user_year % 4  # Make into constant
        operation2 = user_year % 100
        operation3 = user_year % 400
        if (operation1 == 1):
            print("{} is a common year".format(user_year))
            exit()
            if (operation2 == 1):
                print("{} is, in fact, a leap year".format(user_year))
                exit()
                if (operation3 == 1):
                    print("{} is a common year".format(user_year))
                    exit()
                else:
                    print("{} is, in fact, a leap year".format(user_year))
            else:
                print("{} is, in fact, a leap year".format(user_year))
        else:
            print("{} is, in fact, a leap year".format(user_year))
    except Exception:
        print("{} is not a year".format(user_input))
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
