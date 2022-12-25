from copy import copy
from pstats import Stats
import time
from sorting import checkAll, fillNumberArray

def quicksort(array):
    smaller = []
    bigger = []
    pivots_counter = 1
    pivot = None

    if len(array) <= 1:
        return array
    else:
        pivot = array.pop(0)
        for a in array:
            if a == pivot:
                pivots_counter += 1
            elif a > pivot:
                bigger.append(a)
            elif a < pivot:
                smaller.append(a)

        sorted_smaller = quicksort(smaller)
        sorted_bigger = quicksort(bigger)

        # Get all into one
        all = []
        for a in sorted_smaller:
            all.append(a)  

        for a in range(pivots_counter):
            all.append(pivot)

        for b in sorted_bigger:
            all.append(b)

        return all 

def quicksortForTesting(array):
    original_array = copy(array)
    
    start = time.time()
    resulting_array = quicksort(array)
    time_taken =  time.time()- start
    
    stats = {
        "name": "quick_sort",
        "time": time_taken*1000,
        "array_to_sort_length": len(original_array),
        "check": checkAll(original_array, resulting_array)
    }

    return stats

#array_to_sort = [12, 34, 14, 1, 7, 77, 88, 33, 44, 67, 6, 45, 4, 5, 6, 4]
#print(quicksort(array_to_sort))

def localTest():
    array = fillNumberArray(1000, 1)
    if len(array) <= 2000:
        print(array)
    else: print("Array to sort was loaded")
    stats = quicksortForTesting(array)
    print(stats)

#localTest()
