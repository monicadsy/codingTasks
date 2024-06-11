# Creating recursion to add up numbers in a list of integers
def adding_up_to(list_integers, index_num):
    if index_num == 0:  # when length of integer list is 0, the program returns 0
        return list_integers[0]
    elif index_num >= len(list_integers): # when index number >= lenght of integer list, the program returns 0
        return 0
    else:
        return list_integers[0] + adding_up_to(list_integers[1:], index_num-1) # add all the integers up to the give index point by recursion

#Print the result accordingly
print(adding_up_to([1,4,5,3,12,16], 4))
print(adding_up_to([4,3,1,5], 1))
print(adding_up_to([4,3,1,5], 5))
print(adding_up_to([4,3,1,5], 0))
