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
    
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = []

        def backtrack(remain, comb, next_start):
            # print(f"remain is {remain}, comb is {comb}")
            if remain == 0 and len(comb) == k:
                # make a copy of current combination
                # Otherwise the combination would be reverted in other branch of backtracking.
                results.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                # exceed the scope, no need to explore further.
                return

            # Iterate through the reduced list of candidates.
            for i in range(next_start, 9):
                comb.append(i+1)
                backtrack(remain-i-1, comb, i+1)
                # backtrack the current choice
                comb.pop()

        backtrack(n, [], 0)

        return results

    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [[0] * 5 for i in range(n)]
        
        for vowels in range(0, 5):
            memo[0][vowels] = vowels+1
        
        for i in range(1, n):
            memo[i][0] = 1
            for vowels in range(1, 5):
                memo[i][vowels] = memo[i][vowels-1] + memo[i-1][vowels]
        
        return memo[n-1][4]
        
        

sol = Solution()
n = 2
result = sol.combinationSum3(3, 9)
print(result)
