tutor = True
 
def findMax(arr, n): 
    mi = 0
    for i in range(n): 
        if arr[i] > arr[mi]: 
            mi = i
    return mi 

def pancakesort(A):
    assert len(A) > 1
    i = len(A) 
    while(i > 1):
        indx = findMax(A, i)
        ind = indx+1
        if ind != i:
            A[:ind] = reversed(A[:ind])
            print(A[:ind])
            A[:i] = reversed(A[:i])
            print(A[:i])
        i -= 1
    return A

l = [5,2,4,3,1]
s = pancakesort(l)
print(s)
