import collections
import heapq
import random

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # the logic is to first build a frequency map for nums
        # then maintain a heap of frequencies with k elements
        n = len(nums)
        if k == n:
            return nums

        dict_freq = collections.Counter(nums)
        unique = list(dict_freq.keys())

        def partition(left, right, pivot):
            pivot_freq = dict_freq[unique[pivot]]
            unique[pivot], unique[right] = unique[right], unique[pivot]

            store_index = left
            for i in range(left, right):
                if dict_freq[unique[i]] < pivot_freq:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1
            
            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index

        # Sort a list within left..right till kth less frequent element takes its place. 
        def quickselect(left, right, k_smallest):
            if left == right:
                return # no sorting needed
            
            pivot = random.randint(left, right)
            pivot = partition(left, right, pivot)

            if k_smallest == pivot:
                return
            elif k_smallest < pivot:
                quickselect(left, pivot-1, k_smallest)
            else:
                quickselect(pivot+1, right, k_smallest)

        n = len(unique)  
        quickselect(0, n - 1, n - k)
        return unique[n-k:]

sol = Solution()
nums = [1,1,1,2,2,3]
k = 2

result = sol.topKFrequent(nums, k)
print(result)