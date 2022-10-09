def mergeSort(nums):
    if len(nums) > 1:
        middle = len(nums) // 2
        # create copies
        L = nums[:middle]
        R = nums[middle:]
        
        mergeSort(L)
        mergeSort(R)

        n1 = len(L)
        n2 = len(R)

        # Merge the temp arrays back into arr[l..r]
        i = 0     # Initial index of first subarray
        j = 0     # Initial index of second subarray
        k = 0     # Initial index of merged subarray
    
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1
    
        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            nums[k] = L[i]
            i += 1
            k += 1
    
        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            nums[k] = R[j]
            j += 1
            k += 1
 
# Driver code to test above
array_origin = [12, 11, 13, 5, 6, 7]
n = len(array_origin)
print("Given array is")
for i in range(n):
    print("%d" % array_origin[i],end=" ")
 
mergeSort(array_origin)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % array_origin[i],end=" ")
print("\n")