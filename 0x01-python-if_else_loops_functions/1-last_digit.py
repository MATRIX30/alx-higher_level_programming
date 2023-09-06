#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    temp = -1 * number
    flag = 1
else:
    temp = number
    flag = 0
while (temp > 10):
    temp %= 10
if flag == 1:
    temp = -1 * temp
if (temp > 5):
    print(f"Last digit of {number} is {temp} and is greater than 5")
elif (temp == 0):
    print(f"Last digit of {number} is {temp} and is 0")
elif (temp < 6 and temp != 0):
    print(f"Last digit of {number} is {temp} and is less than 6 and not 0")
