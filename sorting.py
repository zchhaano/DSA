#%%
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)
    print(alist)
def quickSortHelper(alist, first, last):
    """
    Helper function for quicksort algorithm.

    Parameters:
    alist (list): The list to be sorted.
    first (int): The index of the first element in the sublist to be sorted.
    last (int): The index of the last element in the sublist to be sorted.
    """
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)

def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

# %%
#使用三数取中法避免切分不均匀，即在选择 基准值时考虑列表的头元素、中间元素与尾元素
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = median_of_three(arr[0], arr[len(arr) // 2], arr[-1])
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quicksort(less) + equal + quicksort(greater)

def median_of_three(a, b, c):
    if (a - b) * (c - a) >= 0:
        return a
    elif (b - a) * (c - b) >= 0:
        return b
    else:
        return c

# %%
