import math
import time
from math import prod  # Python 3.8+

def multiply_list(lst):
    return prod(lst)

def delayed_sqrt(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)