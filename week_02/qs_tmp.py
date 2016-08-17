inp = open('QuickSort.txt','r')
L = inp.readlines()

for i in range(len(L)):
    L[i] = int(L[i])


def quicksort(A,begin,end) :
    count = 0
    if end - begin <= 1:
        return 0
    else :
        split = partition(A,begin,end)
        count = end - begin - 1
        lc = quicksort(A,begin,split)
        rc = quicksort(A,split+1,end)
        return count + lc + rc


def partition(A,begin,end) :
    pivot = A[begin]
    i = begin + 1

    for j in range(begin+1,end) :
        if A[j] < pivot :
            A[i], A[j] = A[j], A[i]
            i = i + 1

    A[i-1], A[begin] = A[begin], A[i-1]
    return i-1


print( len(L))
print(quicksort(L,0,len(L)))
