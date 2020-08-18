# TO-DO: Complete the selection_sort() function below
arr = [3,1,5,4,2]
curr_index = 0
smallest_index = curr_index


def selection_sort(items):
    # loop through n-1 elements
    for i in range(0, len(items) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index + 1, len(items)):
            if items[j] < items[smallest_index]:
                smallest_index = j

        items[smallest_index], items[cur_index] = items[cur_index], items[smallest_index]

    return items

def selection_sort2(items):
    # loop through n-1 elements
    for i in range(0, len(items) - 1):
        cur_index = i
        smallest_index = cur_index
        #find the next smallest element
        for n in range(cur_index, len(arr)):
            #compare each element with the smallest one found
            if arr[n] < arr[smallest_index]:
                smallest_index = n
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    has_swapped = True

    while(has_swapped):
        has_swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                
                arr[i], arr[i+1] = arr[i+1], arr[i]
                has_swapped = True
           
    return arr
            # if arr[i]>arr[i+1]:
            #     temp = arr[i]
            #     arr[i] = arr[i+1]
            #     arr[i+1] = temp

    # counter = 30
    # while counter != 0:               
    #     for idx in range(1, len(arr)) :
    #         current_element = arr[idx]
    #         current_index = idx      
    #         if current_index == len(arr):
    #                 current_index = 0
    #                 counter -= 1
    #         elif current_element > current_element + 1:
    #             arr[current_index], arr[current_index + 1] = arr[current_index], arr[current_index + 1]
    #             current_index += 1
    #         elif current_element < current_element + 1:
    #             current_index += 1


    # else:
    #     counter -= 1 





    # return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
