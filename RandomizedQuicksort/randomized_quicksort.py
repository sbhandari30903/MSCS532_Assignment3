import random
import numpy as np
import time
import matplotlib.pyplot as plt


def randpartitation(arr, low, high):
    # get random index as pivot
    rand_index = random.randint(low, high)
    # put the random element at the end of array
    arr[rand_index], arr[high] = arr[high], arr[rand_index]
    i = low - 1
    for j in range(low,high):
        # swap i and j if any ele is smaller than pivot element 
        if arr[j] <= arr[high]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

# random quick sort that calculates the recurssion depth
def randquicksort(arr, low, high, depth=0):
    if low < high:
        pivot = randpartitation(arr, low, high)
        ldepth = randquicksort(arr, low, pivot-1, depth+1)
        rdepth = randquicksort(arr, pivot+1, high, depth+1)
        return max(ldepth, rdepth)
    return depth

def rightpartitation(arr, low, high):
    # Last element as pivot
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

# quick sort that calculates the recurssion depth
def quicksort(arr, low, high, depth=0):
    if low < high:
        pivot = rightpartitation(arr, low, high)
        ldepth = quicksort(arr, low, pivot-1, depth+1)
        rdepth = quicksort(arr, pivot+1, high, depth+1)
        return max(ldepth, rdepth)
    return depth

# calculate time and depth of quicksort algo
def getdepthtime(arr, pivottype):
    if pivottype == "random":
        t1 = time.time()
        depth = randquicksort(arr, 0, len(arr)-1, 0)
        t2 = time.time()
        return t2-t1, depth
    else:
        t1 = time.time()
        depth = quicksort(arr, 0, len(arr)-1, 0)
        t2 = time.time()
        return t2-t1, depth

# creates a graph for time and depth and compare for random and last element pivot
def get_time_depth_graph(randtime, randdepth, lasttime, lastdepth, arrtype):
    plt.figure(figsize=(8,6))
    plt.plot(arrtype, randtime, label='Time taken - random pivot')
    plt.plot(arrtype, lasttime, label='Time taken - last pivot')
    plt.xlabel('Array type')
    plt.ylabel('Time taken')
    plt.title('Time - Random pivot Vs Last pivot')
    plt.legend()
    plt.savefig('quicksorttime.png')

    plt.figure(figsize=(8,6))
    plt.plot(arrtype, randdepth, label='Recurssion Depth - random pivot')
    plt.plot(arrtype, lastdepth, label='Recurssion Depth - last pivot')
    plt.xlabel('Array type')
    plt.ylabel('Rec Depth')
    plt.title('Recurssion depth - Random pivot Vs Last pivot')
    plt.legend()
    plt.savefig('quicksortdepth.png')

# calculates the time and depths for different types of array for different types of sorts
def clacluate_time_depth(pivottype):
    unsorted_array_list = np.random.randint(1, 10000, 990).tolist() 
    print("Printing first 10 elements of unsorted_array_list before and after:") 
    print(unsorted_array_list[:10]) 
    t1, d1 = getdepthtime(unsorted_array_list, pivottype)
    print(unsorted_array_list[:10]) 
    
    sorted_array_list = np.arange(1,991).tolist()
    print("Printing first 10 elements of sorted_array_list before and after:") 
    print(sorted_array_list[:10]) 
    t2, d2 = getdepthtime(sorted_array_list, pivottype)
    print(sorted_array_list[:10]) 
    
    reverse_sorted_array_list = np.arange(990, 0, -1).tolist()
    print("Printing first 10 elements of reverse_sorted_array_list before and after:")
    print(reverse_sorted_array_list[:10]) 
    t3, d3 = getdepthtime(reverse_sorted_array_list, pivottype)
    print(reverse_sorted_array_list[:10])
    
    repeated_array_list = np.random.randint(1, 71, size=990).tolist()
    print("Printing first 10 elements of repeated_array_list before and after:")
    print(repeated_array_list[:10]) 
    t4, d4 = getdepthtime(repeated_array_list, pivottype)
    print(repeated_array_list[:10])

    t = [t1, t2, t3, t4]
    d = [d1, d2, d3, d4]
    return t, d



if __name__ == "__main__": 

    arr_type = ['random', 'sorted', 'reverse_s', 'repeated']

    ###############################
    # Random pivot quick sort
    ###############################
    print('Calculating for random index element as pivot')
    rand_t, rand_d = clacluate_time_depth('random')
    
    ###############################
    # Last element pivot quick sort
    ###############################
    print('\n\nCalculating for last index element as pivot')
    last_t, last_d = clacluate_time_depth('last')

    get_time_depth_graph(rand_t, rand_d, last_t, last_d, arr_type)