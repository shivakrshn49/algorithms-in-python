from time import time, strftime, localtime
from datetime import timedelta


def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))

def selection_sort(array_list):
    final_list = []
    start_time = time()
    for i in range(len(array_list)):
        smallest_ele = array_list[0]
        for index, ele in enumerate(array_list[1:]):
            if ele < smallest_ele:
                smallest_ele = ele
        array_list.remove(smallest_ele)
        final_list.append(smallest_ele)
        
    end_time = time()
    print "Total time to run is {0}".format(secondsToStr(end_time - start_time))
    return final_list

print selection_sort([3,2,5,8,1,9,7,4,6])