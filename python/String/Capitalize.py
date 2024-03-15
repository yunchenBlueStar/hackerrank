#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    result_str = ""
    s_list = s.split(" ")
    for i in s_list:
        result_str+= f'{i[:1].upper()}{i[1:]} '
    return result_str

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
