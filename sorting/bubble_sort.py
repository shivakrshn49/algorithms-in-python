########################################################################################
def sort_method_one(data_sequence):
    """
    for n items, we should do n-1 comparisions
    Ex: If there are 5 items in a list, then we need to 5-1 = 4 comparisions with other elements and so on
    """
    print "Started sorting the list {0} with length {1}".format(data_sequence, len(data_sequence))
    comparision_count = 0
    print "\n The comparisions should be n-1, i.e., len(sequence)-1 --> {0}-1={1}, and so the range will be {2}\n".format(len(data_sequence), len(data_sequence)-1, range(len(data_sequence)-1))
    for item in range(len(data_sequence)):
        for i in range(len(data_sequence)-1):
            comparision_count += 1
            print  "comparing data_sequence[{0}] > data_sequence[{1}+1]".format(i,i), "for sequence {0}".format(data_sequence)
            if data_sequence[i] > data_sequence[i+1]:
                print  "===================>data_sequence[{0}] > data_sequence[{1}+1]".format(i,i)  + " ==> " + str(data_sequence[i]) + " > " + str(data_sequence[i+1]), " and the comparision_count is ---> " + str(comparision_count)
                data_sequence[i], data_sequence[i+1] = data_sequence[i+1], data_sequence[i]
                print  "======================================>and the result after swap is {0}".format(data_sequence)
        print "<========Final sorted list =========>", data_sequence
        print "<========Number of comparisions =========>", comparision_count


def sort_method_two(data_sequence):
    """
    for n items, we should do n-1 comparisions
    Ex: If there are 5 items in a list, then we need to 5-1 = 4 comparisions with other elements and so on
    """
    print "Started sorting the list {0} with length {1}".format(data_sequence, len(data_sequence))
    comparision_count = 0
    print "\n The comparisions should be n-1, i.e., len(sequence)-1 --> {0}-1={1}, and so the range will be {2}\n".format(len(data_sequence), len(data_sequence)-1, range(len(data_sequence)-1))
    for item in range(len(data_sequence), 0, -1):
        for i in range(item-1):
            comparision_count += 1;
            print  "comparing data_sequence[{0}] > data_sequence[{1}+1]".format(i,i), "for sequence {0}".format(data_sequence)
            if data_sequence[i] > data_sequence[i+1]:
                print  "===================>data_sequence[{0}] > data_sequence[{1}+1]".format(i,i)  + " ==> " + str(data_sequence[i]) + " > " + str(data_sequence[i+1]), " and the comparision_count is ---> " + str(comparision_count)
                data_sequence[i], data_sequence[i+1] = data_sequence[i+1], data_sequence[i]
                print  "======================================>and the result after swap is {0}".format(data_sequence)
        print "<========Final sorted list =========>", data_sequence
        print "<========Number of comparisions =========>", comparision_count

def sort_method_three(data_sequence):
    """
    for n items, we should do n-1 comparisions
    Ex: If there are 5 items in a list, then we need to 5-1 = 4 comparisions with other elements and so on
    """
    print "Started sorting the list {0} with length {1}".format(data_sequence, len(data_sequence))
    comparision_count = 0
    print "\n The comparisions should be n-1, i.e., len(sequence)-1 --> {0}-1={1}, and so the range will be {2}\n".format(len(data_sequence), len(data_sequence)-1, range(len(data_sequence)-1))
    for item in range(len(data_sequence)-1, 0, -1):
        for i in range(item):
            comparision_count += 1
            print  "comparing data_sequence[{0}] > data_sequence[{1}+1]".format(i,i), "for sequence {0}".format(data_sequence)
            if data_sequence[i] > data_sequence[i+1]:
                print  "===================>data_sequence[{0}] > data_sequence[{1}+1]".format(i,i)  + " ==> " + str(data_sequence[i]) + " > " + str(data_sequence[i+1]), " and the comparision_count is ---> " + str(comparision_count)
                data_sequence[i], data_sequence[i+1] = data_sequence[i+1], data_sequence[i]
                print  "======================================>and the result after swap is {0}".format(data_sequence)
        print "<========Final sorted list =========>", data_sequence
        print "<========Number of comparisions =========>", comparision_count
########################################################################################

data_sequence = [5,4,3,2,1]
data_sequence1 = [5,2,4,3,1]
# sort_method_one(data_sequence)
sort_method_two(data_sequence1)