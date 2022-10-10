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
        high = n1
        while low <= high:
            print("---------------------")
            print(f"low:{low}, high:{high}")
            mid1 = low + (high - low) // 2 # medium of nums1
            mid2 = (n1 + n2 + 1)//2 - mid1 # so that we have almost equal number of elements on both sides of the cut points with two arrays together
            print(f"mid1:{mid1}, mid2:{mid2}")

            maxleft1 = nums1[mid1-1] if mid1 > 0 else MIN_INT
            minright1 = nums1[mid1] if mid1 < n1 else MAX_INT
            maxleft2 = nums2[mid2-1] if mid2 > 0 else MIN_INT
            minright2 = nums2[mid2] if mid2 < n2 else MAX_INT
            print(f"maxleft1:{maxleft1}, minright1:{minright1}, maxleft2:{maxleft2}, minright2:{minright2}")

            if maxleft1 > minright2:
                high = mid1 - 1 # move to the left side
            elif maxleft2 > minright1:
                low = mid1 + 1 # move to the right side
            else:
                return (max(maxleft1, maxleft2) + min(minright1, minright2)) / 2 if (n1+n2)%2 == 0 else max(maxleft1, maxleft2)        
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


    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        MOD = 10**9 + 7
        curr_dp = [[0] * n for _ in range(m)]
        curr_dp[startRow][startColumn] = 1
        result = 0
        
        for _ in range(maxMove):
            next_dp = [[0] * n for _ in range(m)]
            for ridx in range(m):
                for cidx in range(n):
                    neighbors = ((ridx + 1, cidx), (ridx, cidx + 1), (ridx - 1, cidx), (ridx, cidx - 1))
                    for newri, newci in neighbors:
                        if newri >= 0 and newri < m and newci >= 0 and newci < n:
                            next_dp[newri][newci] = (next_dp[newri][newci] + curr_dp[ridx][cidx]) %  MOD
                        else:
                            result = (result + curr_dp[ridx][cidx]) % MOD

            curr_dp = next_dp
        return result

    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        result = 0
        waiting = collections.defaultdict(list)
        for w in words:
            waiting[w[0]].append(iter(w[1:]))
        print(waiting)
        for c in s:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
            print(waiting)

        return len(waiting[None])

        
sol = Solution()
nums1 = [1, 2]
nums2 = [3, 4, 5, 6, 7, 8, 9]
result = sol.findMedianSortedArrays(nums1, nums2)
# times = [[2,1,1],[2,3,1],[3,4,1]]
# n = 4
# k = 2
# result = sol.networkDelayTime(times, n, k)
# s = "abcabcbb"
# result = sol.lengthOfLongestSubstring(s)
# word1 = "sea"
# word2 = "eat"
# result = sol.minDistance(word1, word2)
# products = ["mobile","mouse","moneypot","monitor","mousepad"]
# searchWord = "mouse"
# result = sol.suggestedProducts(products, searchWord)
# m = 1
# n = 3
# maxMove = 3
# startRow = 0
# startColumn = 1
# result = sol.findPaths(m, n, maxMove, startRow, startColumn)
# s = "abcde"
# words = ["a","bb","acd","ace"]
# result = sol.numMatchingSubseq(s, words)
# dominoes = ".L.R...LR..L.."
# result = sol.pushDominoes(dominoes)
print(result)