'''This sortes a list by sinking down the smallest elements to the beginning of the list.
Those bubbles are heavier than water so they sink to the bottom.'''

def bubbleSortVone(list):
    """
    ## Sorts a list of integers using a variant of BubbleSort.

    Args:
        `list`(int): The list of integers to be sorted.

    Returns:
        `list`(int): The sorted list.
    """

    for outer in range(len(list)):
        for inner in range(outer+1, len(list)):
            print(list)
            if list[inner] < list[outer]:
                tmp = list[inner]
                list[inner] = list[outer]
                list[outer] = tmp
    return list




'''Execution examples'''
# A = [4,2,7,12,3]
# bubbleSortVone(A)