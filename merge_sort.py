def merge(array_input, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = array_input[left + i]
 
    for j in range(0, n2):
        R[j] = array_input[middle + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = left     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array_input[k] = L[i]
            i += 1
        else:
            array_input[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        array_input[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        array_input[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(array_input, left, right):
    if left < right:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        middle = left+(right-left)//2
 
        # Sort first and second halves
        mergeSort(array_input, left, middle)
        mergeSort(array_input, middle+1, right)
        merge(array_input, left, middle, right)
 
 
# Driver code to test above
array_origin = [12, 11, 13, 5, 6, 7]
n = len(array_origin)
print("Given array is")
for i in range(n):
    print("%d" % array_origin[i],end=" ")
 
mergeSort(array_origin, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % array_origin[i],end=" ")