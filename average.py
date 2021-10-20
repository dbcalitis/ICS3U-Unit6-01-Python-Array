#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Oct 2021
# This program calculates the average of 10 random numbers

import random


def main():
    # This function calculates the average 10 random numbers
    num_list = []
    average = 0

    # process & output
    for counter in range(0, 10):
        num = random.randint(1, 100)
        num_list.append(num)
        average += num

        print("The random number is: {0}".format(num))

    average /= len(num_list)
    print("\nThe average is {0}.".format(average))

    print("\nDone.")


if __name__ == "__main__":
    main()
