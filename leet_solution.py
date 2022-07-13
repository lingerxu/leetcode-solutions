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

    
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Constants.
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # We need to convert both numbers to negatives
        # for the reasons explained above.
        # Also, we count the number of negatives signs.
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        # Count how many times the divisor has to be
        # added to get the dividend. This is the quotient.
        quotient = 0
        while dividend - divisor <= 0:
            quotient -= 1
            dividend -= divisor

        # If there was originally one negative sign, then
        # the quotient remains negative. Otherwise, switch
        # it to positive.
        return -quotient if negatives != 1 else quotient

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        left = 0
        letterset = set(s[0])
        right = 1
        curr_len = 0
        max_len = 1
        while right < n:
            ch = s[right]
            if ch not in letterset:
                letterset.add(ch)
                right += 1
            else:
                curr_len = right - left # becuase right is already +1, so no need to +1
                max_len = max(curr_len, max_len)
                letterset.remove(s[left])
                left += 1 # left > right won't happen, because when left == right, letterset will be empty

        return max_len

    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # make a helper function to check if previous word is a predecessor of next word
        def check_pred(word1, word2):
            count_diff = 0
            pointer1 = pointer2 = 0
            len1 = len(word1)
            len2 = len(word2)

            while pointer1 < len1 and pointer2 < len2:
                if word1[pointer1] == word2[pointer2]:
                    pointer1 += 1
                    pointer2 += 1
                    continue
                # 

        n = len(words)


    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        n = len(products)
        indices = [i for i in range(n)]
        res = [indices]
        for idx, c in enumerate(searchWord):
            indices = [i for i in indices if len(products[i]) > idx and products[i][idx] == c]                                                                
            res.append(products[i] for i in indices[:3])        
        return res
        
sol = Solution()
# times = [[2,1,1],[2,3,1],[3,4,1]]
# n = 4
# k = 2
# result = sol.networkDelayTime(times, n, k)
# s = "abcabcbb"
# result = sol.lengthOfLongestSubstring(s)
# word1 = "sea"
# word2 = "eat"
# result = sol.minDistance(word1, word2)
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
result = sol.suggestedProducts(products, searchWord)
print(result)
