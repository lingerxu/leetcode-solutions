class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        # find the first number that is smaller than its right neighbor
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        # swap the earliest numnber that's smaller with the number at current i
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # reserve the sequence after i+1
        # since we already know that its in descending order from i+1
        a = i + 1
        b = n - 1
        while a < b:
            nums[a], nums[b] = nums[b], nums[a]
            a += 1
            b -= 1

        return nums

sol = Solution()
nums = [1, 2, 3, 5, 4]

result = sol.nextPermutation(nums)
print(result)