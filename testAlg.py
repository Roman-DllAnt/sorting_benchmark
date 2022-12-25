import json
from bubblesort import bubblesort
from sorting import sortArray, fillNumberArray
from sorting2 import sortingWithSelection
from quick_sort import quicksortForTesting, localTest
import sys
from visualize import visualizeAll

def compareAll(loads, densities):
    localTest()
    data_for_densities = []
    
    for density in densities:
        
        data_for_loads = []
        for load in loads:
            print(f"next load: {load}")
            loop = 8

            times = {
                "r_sort": 0,
                "selection_sort": 0,
                "quick_sort": 0,
                "bubblesort": 0  
            }
            total_errors_in_load = {
                "r_sort": [],
                "selection_sort": [],
                "quick_sort": [],
                "bubblesort": []
            }
            
            for a in range(loop):
                array_to_sort = fillNumberArray(load, density)
                sys.setrecursionlimit(2000) # for quicksort
                
                if len(array_to_sort) == 100:
                    print(array_to_sort)

                try:
                    # Bubblesort called separately otherways it doesnt work
                    bubble_data = bubblesort(array_to_sort)
                    data_got_from_algs = [sortArray(array_to_sort), sortingWithSelection(array_to_sort), quicksortForTesting(array_to_sort), bubble_data]
                except BaseException as e:
                    print(e, f"the length of the array is {load}")
                    return

                # Get the data
                for a in data_got_from_algs:
                    times[a["name"]] += a["time"]/loop
                    if a["check"] != "all right":
                        total_errors_in_load[a["name"]]
                
            for a in total_errors_in_load:
                if total_errors_in_load[a] == []:
                    total_errors_in_load[a] = None

    # Check not optimal, better: error_counters and if error_counter_len and e._c_order == 0 then errors = None otherways errors = {"len": x, "order": y}

            data_for_loads.append({ "load": load,
                                    "time_r_sort": times["r_sort"],
                                    "error_1": total_errors_in_load["r_sort"],
                                    "time_selection_sort": times["selection_sort"],
                                    "errors_selection_sort": total_errors_in_load["selection_sort"],
                                    "time_quick_sort": times["quick_sort"],
                                    "errors_quick_sort": total_errors_in_load["quick_sort"],
                                    "time_bubblesort": times["bubblesort"],
                                    "errors_bubblesort": total_errors_in_load["bubblesort"]
                                    })

        data_for_densities.append({"density": density, "results": data_for_loads})                                  
    
    return data_for_densities

def saveRelult(data):
    with open("C:/Users/rdall/Desktop/python/sorting_vergleich/pool.json", "w") as pool:
        json.dump(data, pool)

def testAndAnalyze():
    range_to_test = 10
    # range_to_test = int(input("Range to test: "))
    densities = [1, 0.5, 0.1] #, 0.01
    loads = [] # 100-1000 in steps of 1000
    for a in range(range_to_test):
        loads.append(100 *(a + 1))
    #for a in range(3):
    #   loads.append(1000*(a+1)) 
    
    sorting_alg_data = {
        "naming": {"Romans Algorhytm": "r_sort",
                      "Selection Sort": "selection_sort",
                      "Quicksort": "quick_sort",
                      "Bubblesort": "bubblesort"},
        "densities": densities,
        "loads": loads,
    }

    sorting_alg_data["data"] = compareAll(loads, densities)

    saveRelult(sorting_alg_data)
    visualizeAll()

testAndAnalyze() 

