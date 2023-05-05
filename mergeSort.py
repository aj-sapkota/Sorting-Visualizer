def merge(arr):
    if len(arr) <= 1:
        return arr
    
    mid   = len(arr)//2
    left  = arr[:mid]
    right = arr[mid:]
    
    merge(left)
    merge(right)
    mergeSort(left,right,arr)

def mergeSort(left,right,arr):
    len_left = len(left)
    len_right = len(right)
    i = j = k = 0
    
    while i <len_left and j < len_right:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:           
            arr[k] = right[j]
            j += 1
        k += 1
        
    while i<len_left:
        arr[k] = left[i]
        i +=1
        k += 1

    while j<len_right:
        arr[k] = right[j]
        j +=1
        k += 1


test = [
    [17, 28, 11, 39, 6, 22, 45, 9, 31],
    [5, 3, 8, 1, 9, 2, 7, 6, 4],
    [20, 12, 35, 27, 16, 41, 32, 19, 24],
    [55, 89, 34, 76, 23, 10, 42, 67, 51]
]

for i in test:
    merge(i)
    print(i)




