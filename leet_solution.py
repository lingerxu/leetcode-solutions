class Solution(object):
    def minRemoveToMakeValid(self, s):
        stack = []
        removeinx = set()
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    removeinx.add(i)
        removeinx = removeinx.union(set(stack))
        result = []
        for i, c in enumerate(s):
            if i not in removeinx:
                result.append(c)
        return "".join(result)


sol = Solution()
path = "L(ee)))t(()co(de"

result = sol.minRemoveToMakeValid(path)
print(result)