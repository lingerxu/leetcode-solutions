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

    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # strategy: using two stacks cause python string immutable
        subendi = 0
        stack = []
        counts = []
        n = len(s)
        result = ""
        for val in s:
            if not stack or stack[-1] != val:
                stack.append(val)
                counts.append(1)
            elif stack[-1] == val:
                counts[-1] += 1
            # when reach k
            if counts[-1] == k:
                counts.pop()
                stack.pop()

        for i in range(len(stack)):
            result += stack[i]*counts[i]

        return result
    
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 3:
            return False
        stack = []
        min_array = [-1] * n
        min_array[0] = nums[0]
        for i in range(1, n):
            min_array[i] = min(min_array[i-1], nums[i])
        
        for j in range(n-1, -1, -1):
            if nums[j] <= min_array[j]:
                continue
            while stack and stack[-1] <= min_array[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])
        return False


sol = Solution()
# nums1 = [1,3]
# nums2 = [2]
nums = [1,2,3,4]
result = sol.find132pattern(nums)
print(result)
