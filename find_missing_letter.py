# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.
# move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]


# First solution
def move_zeros(array):
    for i in range(len(array), 1, -1):
        for j in range(1, i):
            if not isinstance(array[j-1], bool) and array[j-1] == 0:
                array[j-1], array[j] = array[j], array[j-1]
    return array


# Second solution
def move_zeros_sort(array):
    return sorted(array, key=lambda x: x == 0 and type(x) is not bool)
