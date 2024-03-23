#  Also there is Heap sort algorithm

def quickSort(lst, left, right):
    # To quick sort a given list along with it's first index and no. of elements 
    # lst[left : right]
    if(right - left) <= 1:
        return()
    yellow = left + 1
    for green in range(left + 1, right):
        if(lst[green] <= lst[left]):
            lst[yellow], lst[green] = lst[green], lst[yellow]
            yellow += 1
    lst[left], lst[yellow-1] = lst[yellow-1], lst[left]
    quickSort(lst, left, yellow-1)
    quickSort(lst, yellow, right)

seq1 = [1,21,41,89,21,14,73]
print(seq1)
quickSort(seq1, 0, len(seq1))
print(seq1)