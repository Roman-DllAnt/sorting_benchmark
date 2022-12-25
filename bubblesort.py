import time
from sorting import checkAll, fillNumberArray

def bubblesort(array_to_sort): 
    original_array = array_to_sort.copy()
    start = time.time()
    condition = True
    cycles = 0
    while condition == True:
        swaps = 0 
        for a in range(len(array_to_sort)-1):
            if array_to_sort[a] > array_to_sort[a+1]:
                mem = array_to_sort[a]
                array_to_sort[a] = array_to_sort[a+1]
                array_to_sort[a+1] = mem

                swaps += 1
        print(time.time())
        if swaps == 0:
            condition = False
        else:cycles += 1

    if len(array_to_sort) < 200:
        print(f"bubblesorted array: {array_to_sort}")

    end = time.time()
    timer = (end - start)*1000
    
    print(f"Start: {start}, end: {end}")
    print(f"bs took {timer} ms")
    print(cycles)
    
    test_array = checkAll(original_array, array_to_sort)
    print(test_array)
    return {
        "name": "bubblesort",
        "time": timer,
        "array_to_sort_length": len(array_to_sort),
        "check": test_array
    }

def localTest():
    array = fillNumberArray(1000, 1)
    if len(array) <= 2000:
        print(array)
    else: print("Array to sort was loaded")
    stats = bubblesort(array)
    print(stats)

localTest()