class Solution(object):
    # def validPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     left = 0
    #     right = len(s) - 1
    #     while left < right:
    #         if s[left] != s[right]:
    #             tmp1 = s[left:right]
    #             tmp2 = s[left+1:right+1]
    #             return tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]
            
    #         left += 1
    #         right -= 1
        
    #     return True
    
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        n = len(s)
        nhalf = n // 2
        one = s[:nhalf]
        two = s[:nhalf:-1]
        i = 0
        j = 0
        counter = 0
        while i < nhalf and j < nhalf:
            if one[i] == two[j]:
                i += 1
                j += 1
            elif

sol = Solution()
s = "abcdeca"
k = 2

result = sol.isValidPalindrome(s, k)
print(result)