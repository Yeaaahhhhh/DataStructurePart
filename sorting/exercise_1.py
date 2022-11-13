#******************
# Lab 9: Exercise 1
# Author: Dexter
# Collaborators/References:
#******************

import random
import time
import math

def recursive_selection_sort(data, data_len, index = 0): 
    '''
    Use Selection Sort to arrange the integers in a list (data) in descending order
    Inputs:
       data (list) - list of integers to be sorted
       data_len (int) - number of elements in the data
       index (int) - index of starting element
    Returns: None
    '''
    
    # TODO-Remove pass and fill out the rest. 
    #You may use additional user-defined functions if required.
    # set base case

    if index < data_len - 1:
        minNumIndex = 0
        while index < data_len:
            if data[minNumIndex] > data[index]:
                minNumIndex = index   # find the mini position
            else:
                pass
            index += 1
    
        temp = data[data_len-1]
        data[data_len-1] = data[minNumIndex]
        data[minNumIndex] = temp     # change those two variable
    
        recursive_selection_sort(data, data_len-1)
    else:
        return None

  
def recursive_merge_sort(data): 
    '''
    Use MergeSort to arrange the integers in a list (data) in descending order
    Inputs:  data (list) - list of integers to be sorted
    Returns: sorted data list
    '''
    
    # TODO-Remove pass and fill out the rest. 
    #You may use additional user_defined functions if required.

    if len(data) <= 1:
        return data
    else:
        midNum = len(data)//2
        left = recursive_merge_sort(data[:midNum])
        right = recursive_merge_sort(data[midNum:])
        return mergeThem(left, right)
    
    # merge the two halfs fo the data list and return the data list

def mergeThem(left, right):
  
    finalList = []

    leftF = 0     # left first
    rightF= 0     # right first
    leftLen = len(left) 
    rightLen = len(right) 

    while not leftF >= leftLen and not rightF >= rightLen:
        if left[leftF] >= right[rightF]:
            finalList.append(left[leftF])
            leftF += 1
        else:
            finalList.append(right[rightF])
            rightF += 1

    
    while not leftF >= leftLen:  # make sure the rest of (every element in the original list) element appended
        finalList.append(left[leftF])
        leftF += 1

    while not rightF >= rightLen:
        finalList.append(right[rightF])
        rightF += 1
        
    return finalList

if  __name__== "__main__":
     # Define the list of random numbers
    random_list = [random.randint(1,1000) for i in range(500)]
    list_len = len(random_list) 
    ascending_list = sorted(random_list)
    descending_list = sorted(random_list, reverse=True)
      
    # Calculate the execution time to sort a list of random numbers #
    start_sel = time.time()
    recursive_selection_sort(random_list, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(random_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of random numbers
    print('The execution time: to sort a random list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))
    
    
    # Calculate the execution time to sort a list of intergers already sorted in ascending order #
    start_sel = time.time()
    recursive_selection_sort(ascending_list, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(ascending_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of intergers already sorted in ascending order 
    print('The execution time: to sort a ascending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))      
    
    
    # Calculate the execution time to sort a list of intergers already sorted in descending order #
    start_sel = time.time()
    recursive_selection_sort(descending_list, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(descending_list)
    end_merge = time.time()
    
    # Print the results execution time to sort a list of intergers already sorted in descending order 
    print('The execution time: to sort a descending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))    
