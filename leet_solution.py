import math

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

    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # use two pointers, one from start one from end
        left = 0
        right = len(nums) - 1

        if right < 1:
            return nums

        while left < right:
            while nums[left] % 2 == 0 and left < right:
                left += 1
            while nums[right] % 2 == 1 and left < right:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]

        return nums



sol = Solution()
# nums1 = [1,3]
# nums2 = [2]
nums = [0,2]
result = sol.sortArrayByParity(nums)
print(result)
