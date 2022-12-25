from random import randint
import time

def fillNumberArray(length, density):
    array_to_fill = []
    number_pool = []
    dens_value = pow(density, (-1))
    for a in range(int(length/density)):
        # print(length, density, (length/density))
        number_pool.append(a+1)

    trigger = True
    while trigger:
        new_num_index = int(randint(0, (len(number_pool)-1)))
        
        new_num = number_pool[new_num_index]
        
        if length >= 10000 and new_num%1000==0:
            print(new_num)

        array_to_fill.append(new_num)
        number_pool.remove(new_num)
        if len(array_to_fill) >= length:
            trigger = False

    return array_to_fill

def checkAll(start_array, end_array):

    error_data={"len":"error accessing", "order": "error accessing"}
    if len(start_array) == len(end_array):
        length_correct = True
    else: 
        length_correct = False

    for numb in end_array:
        try:
            next_numb = end_array[end_array.index(numb) + 1]
            if numb < next_numb:
                continue
            else: 
                raise BaseException("order wrong")
        except BaseException as e: 
            if e == BaseException("order wrong"): 
                order_correct = False
                return error_data
            else: continue
    order_correct = True
    
    if order_correct and length_correct:
        error_data = "all right"
    elif order_correct == False and length_correct == False:
        error_data == "all wrong"
    elif order_correct == False:
        error_data = "wrong order"
    elif length_correct == False:
        error_data = f"wrong length ({len(end_array)} instead of {len(start_array)})"

    return error_data

def sortArray(array_to_sort):
    
    start = time.time()

    array = array_to_sort

    smallest_num = array[0]
    biggest_num = array[0]

    for numbere in array:
        if numbere < smallest_num: smallest_num = numbere
        if numbere > biggest_num: biggest_num = numbere

    range_array = biggest_num - smallest_num + 1
    #print(biggest_num, smallest_num, range_array)

    array_to_insert = []

    # Add placeholders
    for wanted_didgit in range(range_array):
        array_to_insert.append(f"{wanted_didgit}")

    for numbere in array: 
        new_index = (numbere - smallest_num)
        array_to_insert[new_index] = numbere
        
        
    # Delete remaining placeholders    
    indexus = 0
    for numbere in range(len(array_to_insert)):
        if type(array_to_insert[indexus]) == str:
            array_to_insert.remove(array_to_insert[indexus])
        else: indexus += 1
            
    #print(array_to_insert)

    end = time.time()

    time_taken = end - start
    
    return {
        "name": "r_sort",
        "time": time_taken*1000,
        "array_to_sort_length": len(array),
        "check": checkAll(array, array_to_insert)
    }

#name = __name__
#
#filled_array = fillNumberArray(10000, 1)
#st = sortArray(filled_array)
#print(st)
