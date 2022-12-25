def insertionSort(arr: list):
    for a in range(1, len(arr)):
        key = arr[a]
        j = a-1 
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
    	
        arr[j+1] = key
    
    return arr

array_to_sort = [5, 7, 3, 6, 1, 8, 4, 9, 5, 32, 32, 35, 76, 31, 4, 64, 24, 29,77]
print(insertionSort(array_to_sort))