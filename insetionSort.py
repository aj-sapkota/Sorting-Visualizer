def insertion(element):
    for i in range(1,len(element)):
        anchor = element[i]
        j= i-1
        while j >= 0 and anchor<element[j]:
            element[j+1] = element[j]
            j = j-1
            element[j+1] = anchor
        
        
       
trial  =     [17, 28, 11, 39, 6, 22, 45, 9, 31]
insertion(trial)
print(trial)


test = [
    [17, 28, 11, 39, 6, 22, 45, 9, 31],
    [5, 3, 8, 1, 9, 2, 7, 6, 4],
    [20, 12, 35, 27, 16, 41, 32, 19, 24],
    [55, 89, 34, 76, 23, 10, 42, 67, 51]
]

for i in test:
    insertion(i)
    print(i)
    