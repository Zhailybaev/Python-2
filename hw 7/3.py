import numpy as np

def count(arr):
    counter = 0
    current = 1
    if arr[0] == 0: 
        return counter
    else: 
        for i in range(len(arr)):
            if arr[i] == current: 
                continue
            else: 
                if current == 1:
                    current = 0 
                else: 
                    current=1
                counter += 1

    return counter + 1


print(count([1, 1, 0, 0, 0, 1, 0]))
print(count([1, 1, 1]))
print(count([0, 0, 0]))
print(count([0, 1, 1, 1]))