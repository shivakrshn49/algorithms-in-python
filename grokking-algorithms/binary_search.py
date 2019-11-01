from time import time, strftime, localtime
from datetime import timedelta

def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))

def binary_search(input_sorted_list, target_element):
    """
    Binary Search using While
    """
    start_time = time()
    print "\nRunning binary_search using While....................."
    start_index = 0
    end_index = len(input_sorted_list) - 1
    while start_index <= end_index:
        middle_index = (start_index + end_index)/2
        middle_element = input_sorted_list[middle_index]
        if target_element == middle_element:
            end_time = time()
            print "Time take to execute using while loop is {0}".format(end_time - start_time)
            print "Time take to execute using while loop is {0}".format(secondsToStr(end_time - start_time))
            return "Found the target element {0} at index {1}".format(target_element, input_sorted_list.index(middle_element))
        elif target_element < middle_element:
            # Search in the left part
            end_index = middle_index - 1
        elif target_element > middle_element:
            # Search in the right part
            start_index = middle_index + 1
        else:
            return "Not found"


def binary_search_recursive(alist, start, end, key):
    """Search key in alist[start... end - 1]."""
    print "\nUsing recursive algorith,........."
    if not start <= end:
        return -1
 
    mid = (start + end)//2
    if key < alist[mid]:
        return binary_search_recursive(alist, start, mid-1, key)
        # return binary_search_recursive(alist, mid + 1, end, key)
    elif key > alist[mid]:
        return binary_search_recursive(alist, mid+1, end, key)
        # return binary_search_recursive(alist, start, mid, key)
    else:
        return "Found the target element {0} at index {1}".format(key, mid)
        return mid


print binary_search(list(range(0, 101)), 71)
start_time = time()
print binary_search_recursive(list(range(0, 101)), 0, len(list(range(0, 101))), 71)
end_time = time()
print end_time-start_time

