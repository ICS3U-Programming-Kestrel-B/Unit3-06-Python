#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Oct. 17, 2022
# This program asks for a number
# between 0 and 9 and tells you
# if your guess is correct

import random
import math


def main():
    # input
    print("This program asks for a number")
    print("between 0 and 9 and tells you")
    print("if your answer is correct")
    print("")
    user_num = input("Enter a number between 0 and 9: ")

    # process/output
    # generating random correct answer
    random_num = random.randint(0, 9)

    # checking that user_num is an integer
    try:
        user_num = int(user_num)
    except ValueError:
        print("\n")
        print(("Please enter a valid number. {} is not valid.\n").format(user_num))
    finally:
        print("")

    # checking that user_num is in the right range
    if user_num > 9:
        print(("Please enter a valid number. {} is not valid.\n").format(user_num))
    elif user_num < 0:
        print(("Please enter a valid number. {} is not valid.\n").format(user_num))
    else:
        print("")

    # checking if user_guess is correct
    if user_num == random_num:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly. The correct number was {}.".format(random_num))


if __name__ == "__main__":
    main()
