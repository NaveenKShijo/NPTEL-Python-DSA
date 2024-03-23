
def merge(lst1, lst2):
    #  To merge two sorted(ascending) lists in ascending order
    m = len(lst1)
    n = len(lst2)
    i =0
    j = 0
    
    result_lst = []
    while i < m or j < n:
        if (i == m):
            while(j != n):
                result_lst.append(lst2[j])
                j += 1
        elif (j == n):
            while(i != m):
                result_lst.append(lst1[i])
                i += 1
        elif (lst1[i] < lst2[j]):
            result_lst.append(lst1[i])
            i += 1
        else:
            result_lst.append(lst2[j])
            j += 1
    return result_lst

def mergeSort(lst, left, right): 
    # Here left is the left index and right value for the main list is the no. of total elements in the list
      # To merge sort the given array
    if (right - left) <= 1:
        return lst[left : right]
    else:
        mid = (left + right) // 2
        L = mergeSort(lst, left, mid)
        R = mergeSort(lst, mid, right)
        return merge(L,R)
      
def unionMerge(lst1,lst2):
    # To remove the duplicated and print union of two lists
    result = []
    i = j = 0
    while(i < len(lst1) or j < len(lst2)):
        if(i == len(lst1)):
            while(j < len(lst2)):
                result.append(lst2[j])
                j += 1
        elif(j == len(lst2)):
            while(i<len(lst1)):
                result.append(lst1[i])
                i += 1
        elif(lst1[i] < lst2[j]):
            if lst1[i] in result:
                i += 1
                continue
            result.append(lst1[i])
            i += 1
        elif(lst2[j] < lst1[i]):
            if lst2[j] in result:
                j += 1
                continue
            result.append(lst2[j])
            j += 1
        elif(lst1[i] == lst2[j]):
            result.append(lst1[i])
            i += 1
            j += 1
    return result

def intersectionSort(lst1,lst2):

seq1 = [i for i in range(10,0,-1)]
print(seq1)
print(mergeSort(seq1,0,10))

seq2 = [3,6,7,9,9,13,21,25]
seq3 = [10,13,21,21]
print(unionMerge(seq2, seq3))


