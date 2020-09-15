#return index

def linear_search(arr, target):
    # Your code here
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    # for x in arr:
    #     if x == target:
    #         return arr.index(target)

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(my_list, search_item):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = my_list[middle]
        if guess == search_item:
            return middle
        if guess > search_item:
            high = middle - 1
        else:
            low = middle + 1
    return -1
    # Your code here # not found
