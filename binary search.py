def binarysearch(array,element):
    mid_index = len(array)//2
    if len(array) == 1 and array[0] == element:
        return element
    elif len(array) == 1 and array[0] != element:
        return False
    else:
        if element == array[mid_index]:
            return element
        elif element > array[mid_index]:
            array = array[mid_index::]
            return binarysearch(array,element)
        else:
            array = array[0:mid_index]
            return binarysearch(array,element)

print(binarysearch([17,20,26,31,44,54,55,65,77,93],1))
