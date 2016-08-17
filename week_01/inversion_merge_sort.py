'''
This file contains all of the 100,000 integers between 1 and 100,000
(inclusive) in some order, with no integer repeated.

Your task is to compute the number of inversions in the file given, where the
ith row of the file indicates the ith entry of an array.

Because of the large size of this array, you should implement the fast
divide-and-conquer algorithm covered in the video lectures.

The numeric answer for the given input file should be typed in the space below.

So if your answer is 1198233847, then just type 1198233847 in the space
provided without any space / commas / any other punctuation marks. You can make
up to 5 attempts, and we'll use the best one for grading.

(We do not require you to submit your code, so feel free to use any programming
language you want --- just type the final numeric answer in the following
space.)

[TIP: before submitting, first test the correctness of your program on some
small test files or your own devising. Then post your best test cases to the
discussion forums to help your fellow students!]
'''

#L = [1,3,5,2,4,6]

inp = open('IntegerArray.txt','r')
L = inp.readlines()

for i in range(len(L)):
    L[i] = int(L[i])

def merge_sort(L,inv):
    if len(L) < 2:
        return L[:], inv
    else:
        i = int(len(L) / 2)
        left    = merge_sort(L[:i], inv)
        right   = merge_sort(L[i:], inv)
        inv += left[1] + right[1]
        print str(left[0]) + ' ' + str(right[0])
        return merge(left[0],right[0], inv)

def merge(left, right, inv):
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            # split inversion happens here
            inv += len(left)-i
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result, inv

#print merge_sort(L,0)[1]
print merge_sort([5, 3, 8, 9, 1, 7, 0, 2, 6, 4],0)
#print merge_sort([6,5,4,3,2,1],0)
#print merge(L[:len(L)/2], L[len(L)/2:],0)[1]
