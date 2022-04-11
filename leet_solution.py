class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for val in ops:
            print(val)
            if val == "C":
                stack.pop()
            elif val == "D":
                stack.append(stack[-1] * 2)
            elif val == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(val))
            print(stack)

        return sum(stack)

sol = Solution()
ops = ["5","-2","4","C","D","9","+","+"]

result = sol.calPoints(ops)
print(result)