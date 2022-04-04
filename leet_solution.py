class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # two pointers, from 0, n-1 to inward
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            tmpsum = nums[left] + nums[right]
            if tmpsum == target:
                return [left, right]
            elif tmpsum < target:
                left += 1
            else: # tmpsum > target:
                right -= 1

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # n = len(s)
        # sub_start = 0
        # sub_end = 0
        # idx_blank = 0
        # result = ""
        # for i in range(n):
        #     if s[i] == " " or i == n - 1:
        #         if idx_blank > 0:
        #             sub_start = idx_blank + 1
        #         idx_blank = i
        #         sub_end = idx_blank - 1 if i < n - 1 else i
        #         # reverse the string between sub_start and sub_end
        #         # and add to result
        #         sub_str = ""
        #         while sub_end >= sub_start:
        #             sub_str += s[sub_end]
        #             sub_end -= 1
        #         if i < n - 1:
        #             result = result + sub_str + " "
        #         else:
        #             result += sub_str

        # return result
        return ' '.join(x[::-1] for x in s.split())


sol = Solution()
nums = [2,7,11,15]
target = 9
s = "Let's take LeetCode contest"

result = sol.reverseWords(s)
print(result)