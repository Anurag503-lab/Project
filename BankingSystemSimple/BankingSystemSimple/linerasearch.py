#Linear search in ptyhon
from array import array
from re import M


def linearSearch(array,n,x):
    for i in range (0,n):
        if(array[i] == x):
                return i
    return -1
array = [2,4,0,1,9]
x = 1
M= len(array)
result = linearSearch(array,M,x)
if(result == -1)
print("Element not found")
else:
    printO("element")
