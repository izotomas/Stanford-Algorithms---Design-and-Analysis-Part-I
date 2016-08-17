inp = open('QuickSort.txt','r')
L = inp.readlines()

for i in range(len(L)):
    L[i] = int(L[i])

# QuickSort implementation starts here

def QS(A):
    return sort(A, 0, len(A))

def sort(A, lo, hi):
    count = 0
    if hi - lo <= 1:
        return 0
    else:
        i = partition(A, lo, hi)
        count = hi - lo - 1
        l = sort(A, lo, i)
        r = sort(A, i + 1, hi)
        return count + l + r

def median(A, lo, hi):
    a = A[lo]
    m = lo + (hi - lo + 1)/2 - 1
    b = A[m]
    c = A[hi - 1]
    if (a <= b and b <= c) or (c <= b and b <= a):
        A[lo], A[m] = A[m], A[lo]
    elif(a <= c and c <= b) or (a >= c and b <= c):
        A[lo], A[hi - 1] = A[hi - 1], A[lo]

def partition(A, lo, hi):
    # median element get here
    median(A,lo,hi)
    p = A[lo]    # pivot element
    i = lo + 1   # index of last element smaller than pivot

    for j in range(lo + 1, hi):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[lo], A[i - 1] = A[i - 1], A[lo]
    return i - 1

# sorting
print 'Expected : 138382'
print QS(L)


