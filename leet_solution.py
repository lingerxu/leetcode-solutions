class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        len_pop = len(popped)
        stack = []
        pointer_pop = 0
        for val in pushed:
            stack.append(val)
            while pointer_pop < len_pop and stack and popped[pointer_pop] == stack[-1]:
                stack.pop()
                pointer_pop += 1

        return not stack


sol = Solution()
pushed = [0,1]
popped = [0,1]

result = sol.validateStackSequences(pushed, popped)
print(result)