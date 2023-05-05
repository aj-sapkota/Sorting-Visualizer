import time
from color import *


def bubbleSort(elements):
    size = len(elements)
    for k in range(size-1):
        swapped = False
        for i in range (size-1-k):
            if  elements[i] > elements[i+1]:
                tmp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = tmp
                swapped =True
        if not swapped:
            break
    return elements
     


elements = [5, 12, 8, 1, 10]
sorted_elements = bubbleSort(elements)
print(sorted_elements)