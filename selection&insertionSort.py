def Selection_sort(sequence):
    length = len(sequence)
    for i in range(length):
        for j in range(i+1,length):
            if(sequence[i] > sequence[j]):
                sequence[i], sequence[j] = sequence[j], sequence[i]
    return sequence

seq = [45,78,12,23,100,34,20,67]
print(seq)
print(Selection_sort(seq))

def insertion_sort(sequence):
    length = len(sequence)
    for i in range(1,length):
        if ( sequence[i] < sequence[i-1]):
            sequence[i], sequence[i-1] = sequence[i-1], sequence[i]
            j = i - 1
            while(j != 0 and sequence[j] < sequence[j-1] ):
                sequence[j], sequence[j-1] = sequence[j-1], sequence[j]
                j = j-1
    return sequence



list1 = [34,56,21,66,32,69,13,46,21,90,34,23,79]
print(list1)
print(insertion_sort(list1))


