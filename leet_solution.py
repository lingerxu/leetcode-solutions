class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        from collections import defaultdict
        # the logic is to find a consecutive substring in s2 that contains all the characters in s1
        # the brute force solution is to go through s2, check every n1 length of substring, 
        # edge case; n2 < n2, return false
        n1 = len(s1)
        n2 = len(s2)
        if n2 < n1:
            return False
        i = 0
        j = 0

        # creat dict of s1
        dict1 = defaultdict(lambda:0)
        for i, val in enumerate(s1):
            dict1[val] += 1
        
        for key in dict1:
            print(f"{key}: {dict1[key]}")


sol = Solution()
s1 = "ab"
s2 = "eidboaoo"

result = sol.checkInclusion(s1, s2)
print(result)