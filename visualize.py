import matplotlib.pyplot as plt
import pandas as pd
import json

def makeTableForLoad():
    a = 0

def initialize():
    global all_data, algorithms, full_names, data, densities, loads
    with open("C:/Users/rdall/Desktop/python/sorting_vergleich/pool.json", "r") as pool:
        all_data = json.load(pool)
        naming = all_data["naming"]
        algorithms = []
        full_names = []
        for a in naming:
            algorithms.append(naming[a])
            full_names.append(a)  
        
        data = all_data["data"]
        densities = all_data["densities"]
        loads = all_data["loads"]

def findRightDensityData(density):
    initialize()

    for a in data:
        if a["density"] == density:
            return a["results"]
    

def getYXAxis(density, algorithm):
    
    results_for_given_density = findRightDensityData(density) 

    x_axis = []
    y_axis = []

    key = f"time_{algorithm}"
    for a in results_for_given_density:
        x_axis.append(a["load"])
        y_axis.append(a[key])
    
    return {"x": x_axis,
            "y": y_axis}

def visualizeAllForAlgsAndDensityAsTable(alg_names, density):

    results_for_given_density = findRightDensityData(density)
    
    # Create the dict that ist displayed by pandas -> Gets fill out below
    data_frame_dict = {"Loads": loads}

    for alg in alg_names:
        # Check existence
        if alg not in algorithms:
            print(f"algorithm '{alg}' not in existing algorithms")
            continue
        
        # Create entry for this algorithm
        data_frame_dict[alg] = []     
        key = f"time_{alg}"
        
        # Get every time for the array
        try:    
            for load in results_for_given_density:
                data_frame_dict[alg].append(load[key])
        except BaseException as e:
            print(f"making of time load dict failed: {e}")

        try:
            if len(loads) != len(data_frame_dict[alg]):
                raise BaseException(f"Arrays Loads and times dont have the same length: {loads, data_frame_dict[alg]}")
        except BaseException as e:
            print(e)
    
    print(f"Density: {density}")
    print(pd.DataFrame(data_frame_dict))

def visualizeAllForAlgsAndDensityAsGraphs():

    a = 0 

def visualizeAll():
    initialize()
    
    for a in densities:
        visualizeAllForAlgsAndDensityAsTable(algorithms, a)
        print("\n")

def graphAlgs(dens, algs):
    for alg in algs:
        axes = getYXAxis(dens, alg)
        plt.plot(axes["x"], axes["y"], label = alg)

    plt.xlabel("Loads")
    plt.ylabel(f"Times")
    plt.title(f"Times of {algs} for different loads")
    plt.legend()
    plt.show() 

def graphAll(dens):
    initialize()
    graphAlgs(dens, algorithms)



def graphAllForAllDensities():
    # further: https://www.geeksforgeeks.org/graph-plotting-python-set-2/
    
    initialize()
    
    # Starting with figure
    fig = plt.figure()

    # Make dynamic variables for subplots
    dens_graphs = {}

    dens_graphs_counter = 1 
    subplot_count = 221
    
    for dens in densities:
        #dens_graph_name = f"plt{dens_graphs_counter}"
        #dens_graphs[dens_graph_name] = fig.add_subplot(subplot_count)
        #
        ## Increase the names and plots
        #subplot_count += 1
        #dens_graphs_counter += 1 
        for alg in algorithms:
            xy = getYXAxis(dens, alg)
            fig.add_subplot(subplot_count).plot(xy["x"], xy["y"], label = alg)
            fig.add_subplot(subplot_count).set_title(f"Density = {dens}")
    
    fig.subplots_adjust(hspace=.5,wspace=0.5) # Copied
    plt.show()

