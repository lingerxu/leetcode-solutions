class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 1. find the index of the last negative number and first non-negative number O(n)
        # 2. with a while loop with pointer_pos goes up and poinster_neg goes down
        #   - for every number pointed by the two pointers, compare their squared value
        #   - if pos**2 is smaller, then result.append(pos**2) and pointer_pos++
        #   - if neg**2 is smaller, then result.append(neg**2) and pointer_neg--
        # pointer_pos should be < len(nums), pointer_neg should be larger or equal to 0
        # 3. return result
        # Edge cases: nums has only 1 element, and nums have all pos or neg values

        len_nums = len(nums)
        if len_nums == 1:
            return [nums[0]**2]

        pointer_pos = 0
        pointer_neg = 0
        if nums[0] < 0:
            for i in range(1, len_nums):
                if nums[i] < 0:
                    pointer_neg = i
                else:
                    break
            pointer_pos = pointer_neg + 1
        else:
            pointer_neg = -1

        result = []
        while pointer_pos < len_nums or pointer_neg >= 0:
            pos_square = 10**9 if pointer_pos >= len_nums else nums[pointer_pos] ** 2
            neg_square = 10**9 if pointer_neg < 0 else nums[pointer_neg] ** 2

            if pointer_neg < 0 or pos_square <= neg_square:
                result.append(pos_square)
                pointer_pos += 1
            elif pointer_pos >= len_nums or pos_square > neg_square:
                result.append(neg_square)
                pointer_neg -= 1

        return result

sol = Solution()
nums = [0, 2]

result = sol.sortedSquares(nums)
print(result)