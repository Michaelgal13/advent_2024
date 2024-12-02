# Code by Michael Gallagher
# Advent Day 1
import sys
import os.path
from typing import List

#Test lists
#Difference between list 0 and 1 = 4 + 3 + 2 = 9
#Similarity between list 0 and 2 = 7 + 10 = 17
test_list_0 = [7, 5, 3]
test_list_1 = [-1, 9, 2]
test_list_2 = [7, 5, 5]

def list_distances(list_0: List[int], list_1: List[int], debug:int=None):
    if(debug):
        print("Before")
        print("\t" + str(list_0))
        print("\t" + str(list_1))
    # I feel like there must be a  faster way than just sorting, but I think I started late
    list_0.sort()
    list_1.sort()
    if(debug):
        print("After")
        print("\t" + str(list_0))
        print("\t" + str(list_1))
    if(len(list_0) != len(list_1)):
        raise Exception("Lists are not the same size")
    manhattan_distance = 0
    for count, _ in enumerate(list_0):
        manhattan_distance = manhattan_distance + (abs(list_0[count] - list_1[count]))
    return manhattan_distance

def list_similarity(list_0: List[int], list_1: List[int], debug:int=None):
    #Note the challenge does not talk about negative numbers
    data_dict = dict()
    for items in list_1:
        #Would have to check if dict serach is faster than sorting each time
        #Create new key if it does not exist, otherwise increment
        if items in data_dict.keys():
            data_dict[items] = data_dict[items] + 1
        else:
            data_dict[items] = 1
    if(debug):
        print("Temp Dictionary")
        print(data_dict)
    similarity_score = 0
    for items in list_0:
        if items in data_dict.keys():
            similarity_score = similarity_score + (items * data_dict[items])
    return similarity_score


def main():
    #Python doesn't have an argc :(
    if(len(sys.argv) <= 1):
        print("List Distances:")
        print(list_distances(test_list_0, test_list_1, None))
        print("List Similarity:")
        print(list_similarity(test_list_0, test_list_2, None))
    else:
        # print(str(sys.argv[1]))
        if(os.path.isfile(sys.argv[1])):
            list_0 = []
            list_1 = []
            with open(sys.argv[1]) as open_file:
                for line in open_file:
                    line_read = line.split()
                    list_0.append(int(line_read[0]))
                    list_1.append(int(line_read[1]))
        else:
            exception_str = "Could not find file: " + str(sys.argv[1])
            raise Exception(exception_str)
        print("List Distances:")
        print(list_distances(list_0, list_1, None))
        print("List Similarity:")
        print(list_similarity(list_0, list_1, None))

if __name__ == "__main__":
    main()
