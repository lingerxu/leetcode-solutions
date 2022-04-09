# python code for building heap from array, aka heap sort

def max_heapify(nums, heap_size, i):
    largest = i # init i as root
    left = 2 * i + 1
    right = 2 * i + 2
    # if left child is larger than root
    if left < heap_size and nums[left] > nums[largest]:
        largest = left
    # if right child is larger than root
    if right < heap_size and nums[right] > nums[largest]:
        largest = right
    # swap value in nums if root is not largest
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        # Recursively heapify the affected sub-tree 
        # with largest as the root
        max_heapify(nums, heap_size, largest)

def build_heap(nums):
    heap_size = len(nums)
    last_nonleaf = heap_size // 2 - 1
    for i in range (last_nonleaf, -1, -1):
        max_heapify(nums, heap_size, i)

def heapsort(nums):
    heap_size = len(nums)
    build_heap(nums)
    print(f"nums after initial heapify: {nums}")
    for i in range(heap_size-1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        max_heapify(nums, i, 0)
        print(f"nums after {i}th heapify: {nums}")

nums = [2,8,1,4,14,7,16,10,9,3]
heapsort(nums)
print(nums)

# # importing "heapq" to implement heap queue
# import heapq
  
# # initializing list
# li = [5, 7, 9, 1, 3]
  
# # using heapify to convert list into heap
# heapq.heapify(li)
  
# # printing created heap
# print ("The created heap is : ",end="")
# print (list(li))
  
# # using heappush() to push elements into heap
# # pushes 4
# heapq.heappush(li,4)
  
# # printing modified heap
# print ("The modified heap after push is : ",end="")
# print (list(li))
  
# # using heappop() to pop smallest element
# print ("The popped and smallest element is : ",end="")
# print (heapq.heappop(li))