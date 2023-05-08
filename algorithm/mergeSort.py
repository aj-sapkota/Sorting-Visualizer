
import time
from color import *

def merge(data, start, mid, end, drawData, timeValue):
    p = start
    q = mid + 1
    tempArray = []
    i = 0

    while p <= mid and q <= end:
        if data[p] < data[q]:
            tempArray.append(data[p])
            p += 1
        else:
            tempArray.append(data[q])
            q += 1
        i += 1

    while p <= mid:
        tempArray.append(data[p])
        p += 1
        i += 1

    while q <= end:
        tempArray.append(data[q])
        q += 1
        i += 1

    for j in range(i):
        data[start+j] = tempArray[j]

    drawData(data, [ORANGE if x >= start and x < mid 
                    else RED if x == mid 
                    else YELLOW if x > mid and x <=end
                    else BLUE for x in range(len(data))])
    time.sleep(timeValue)


def mergeSort(data, start, end, drawData, timeValue):
    if start < end:
        mid = int((start + end) / 2)
        mergeSort(data, start, mid, drawData, timeValue)
        mergeSort(data, mid+1, end, drawData, timeValue)
        merge(data, start, mid, end, drawData, timeValue)

    drawData(data, [BLUE for x in range(len(data))])








