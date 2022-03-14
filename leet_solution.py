class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []

        for portion in path.split("/"):
            print(portion)
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == "." or not portion:
                continue
            else:
                stack.append(portion)

        final_path = "/" + "/".join(stack)
        return final_path




sol = Solution()

path = "/a/b/c/.././././//d"

result = sol.simplifyPath(path)
print(result)
