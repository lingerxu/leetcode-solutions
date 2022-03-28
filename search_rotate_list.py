class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2 # yes, OCD
            if target == nums[middle]:
                return True
            # if nums[middle] > nums[left], then it is sorted between left and middle
            elif nums[middle] > nums[left]:
                if target >= nums[left] and target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            # if nums[middle] < nums[left], then it is sorted between middle and right
            elif nums[middle] < nums[left]:
                if target <= nums[right] and target > nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
            # when it is equal, we need to move left or middle to a place where they are not equal
            else:
                while left <= middle and nums[left] == nums[middle]:
                    left += 1
                if left == middle: # meaning that all numbers between left and middle is the same
                    left = middle + 1

        return False
        
sol = Solution()
nums = [1, 0, 1, 1, 1]
target = 0

result = sol.search(nums, target)
print(result)