#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
absnum = abs(number) % 10

if (number < 0):
    absnum = -absnum

if (absnum > 5):
    print("Last digit of {} is {} and is greater than "
          "5".format(number, absnum))
elif (absnum == 0):
    print("Last digit of {} is {} and is 0".format(number, absnum))
elif (absnum < 6 and absnum != 0):
    print(f"Last digit of {number} is {absnum} and is less than 6 and not 0")
