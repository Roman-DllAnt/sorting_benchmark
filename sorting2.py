import time
from sorting import checkAll

def sortingWithSelection(array):
    start = time.time()
    
    array_at_start = array.copy()
    
    fixed_values = 0
    while fixed_values < len(array):
        index = 0 + fixed_values
        for a in array:
            if index > len(array)-1:
                continue 
            value_in_the_front = array[fixed_values]
            actual_value = array[index]
            if  actual_value < value_in_the_front:
                
                # Swap dynamic value
                array.remove(actual_value)
                array.insert(index, value_in_the_front)

                # Swap value in the front
                array.remove(value_in_the_front)
                array.insert(fixed_values, actual_value)
            
            index += 1
        fixed_values += 1  
    
    timer = time.time() - start
    
    #print(array)

    return {
        "name": "selection_sort",
        "time": timer*1000,
        "array_to_sort_length": len(array),
        "check": checkAll(array_at_start, array)
    }

