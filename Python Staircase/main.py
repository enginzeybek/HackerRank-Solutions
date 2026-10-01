#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for item in range(n):
        print(" " * (n - item - 1) + "#" * (item + 1))

    

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
