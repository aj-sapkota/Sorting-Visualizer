import time
from color import *


def bubbleSort(elements,drawData,timeValue):
    size = len(elements)
    for k in range(size-1):
        swapped = False
        for i in range (size-1-k):
            if  elements[i] > elements[i+1]:
                # Swap the two elements
                tmp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = tmp
                swapped =True
                # Visualize the swapping process
                drawData(elements,[RED if x ==i or x ==i+1 else BLUE for x in range(len(elements))])
                time.sleep(timeValue)
        # If no elements were swapped in the previous iteration, the array is already sorted
        if not swapped:
            break
    
    # Visualize the final sorted array
    drawData(elements, [BLUE for x in range(len(elements))])

     

