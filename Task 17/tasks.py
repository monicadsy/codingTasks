# Use recursion to return the largest number in a list of integers 
def find_max(array):  
    """Find the maximum number in an array by recursion"""
    if array == []: # if array is empty
        return 0
    elif len(array) == 1: # if array has only one element
        return array[0]
    else: #get max of first integers compared to other integers recursively
        return max(array[0], find_max(array[1:])) # 

# Test
# print(find_max([1]))  # Print 1
# print(find_max([3,1,6,8,2,4,5]))  # Print 8
# print(find_max ([]))  # Print None



