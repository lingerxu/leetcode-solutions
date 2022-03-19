class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        shared = {}
        for val in nums1:
            if val in shared:
                shared[val] += 1
            else:
                shared[val] = 1

        result = []
        for val in nums2:
            if val in shared and shared[val] > 0:
                shared[val] -= 1
                result.append(val)
        
        return result



sol = Solution()
nums1 = [4,9,4]
nums2 = [9,4,9,8,4]

result = sol.intersect(nums1, nums2)
print(result)

import math
print(math.sqrt(3))