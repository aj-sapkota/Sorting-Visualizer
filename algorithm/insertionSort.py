import time
from color import *


def insertionSort(elements,drawData,timeValue):
    for i in range(1,len(elements)):
        anchor = elements[i]
        j= i-1
        while j >= 0 and anchor<elements[j]:
            elements[j+1] = elements[j]
            j = j-1
            elements[j+1] = anchor
            # Visualize the  process
            drawData(elements,[RED if x ==i or x ==j else BLUE for x in range(len(elements))])
            time.sleep(timeValue)
              
    # Visualize the final sorted array
    drawData(elements, [BLUE for x in range(len(elements))])
        
     

    