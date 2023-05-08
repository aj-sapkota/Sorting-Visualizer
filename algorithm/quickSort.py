
import time
from color import *

def swap(start,end,elements):
    temp = elements[start]
    elements[start] = elements[end]
    elements[end] = temp
    
def partition(start,end,elements):
    pivot = start   
     
    while start < end:
        while start <len(elements) and  elements[start] <= elements[pivot] :
            start +=1
        
        while elements[pivot] < elements[end]:
            end -= 1
            
        if start < end:
            swap(start,end,elements)
    swap(pivot,end,elements)
    return end
    
    
def quickSort(start,end,elements,drawData,timeValue) :
    if start < end:
        partition_index = partition (start,end,elements)
        quickSort(start,partition_index-1,elements,drawData,timeValue)
        quickSort(partition_index+1,end,elements,drawData,timeValue)
    
        drawData(elements, [ORANGE if x >= start and x < partition_index 
                            else RED if x == partition_index 
                            else YELLOW if x > partition_index and x <=end
                            else BLUE for x in range(len(elements))])
        time.sleep(timeValue)

    drawData(elements, [BLUE for x in range(len(elements))])
