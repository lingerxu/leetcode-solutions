from errno import ENETDOWN


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        last_occurance = {c: i for i,c in enumerate(s)}

        for i,c in enumerate(s):
            if c not in stack:
                while stack and c < stack[-1] and i < last_occurance[stack[-1]]:
                    stack.pop()
                stack.append(c)
        
        return "".join(stack)


sol = Solution()
s = "cbacdcbc"

result = sol.removeDuplicateLetters(s)
print(result)