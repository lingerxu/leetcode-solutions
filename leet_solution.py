from bisect import bisect_left
from collections import defaultdict
from functools import cache
import heapq
import math
from sre_constants import MIN_REPEAT_ONE

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        MIN_INT = -10**6 - 1
        MAX_INT = 10**6 + 1

        n1 = len(nums1)
        n2 = len(nums2)
        # it is more efficient to cut from the shorter array
        # since high won't be larger than shorter len * 2
        if n1 > n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
        
        low = 0
        high = n1 * 2
        while low <= high:
            print("---------------------")
            print(f"low:{low}, high:{high}")
            mid1 = low + (high - low) // 2
            mid2 = n1 + n2 - mid1 # calculate cut position based on the shorter array
            print(f"mid1:{mid1}, mid2:{mid2}")

            L1 = nums1[(mid1 - 1) // 2] if mid1 > 0 else MIN_INT
            L2 = nums2[(mid2 - 1) // 2] if mid2 > 0 else MIN_INT
            R1 = nums1[mid1 // 2] if mid1 < n1 * 2 else MAX_INT
            R2 = nums1[mid2 // 2] if mid2 < n1 * 2 else MAX_INT
            print(f"L1:{L1}, L2:{L2}, R1:{R1}, R2:{R2}")

            if L1 > R2:
                high = mid1 - 1
            elif L2 > R1:
                low = mid1 + 1
            else:
                return (max(L1, L2) + min(R1, R2) / 2)
            
        return None # should not happen

    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)
        for src, dst, weight in times:
            graph[src].append((dst, weight)) 

    
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # sort increasing in first dimension and decreasing on second
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        print(envelopes)

        def lis(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)
        
        # extract the second dimension and run the LIS
        return lis([i[1] for i in envelopes])

        
sol = Solution()
# times = [[2,1,1],[2,3,1],[3,4,1]]
# n = 4
# k = 2
# result = sol.networkDelayTime(times, n, k)
strs = ["10","0001","111001","1","0"]
m = 5
n = 3
envelopes = [[5,4],[6,4],[6,7],[2,3]]
result = sol.maxEnvelopes(envelopes)
print(result)
