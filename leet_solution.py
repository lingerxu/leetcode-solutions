class Solution(object):
    def isValid(self, s: str) -> bool:
        stackparen = []
        for c in s:
            match c:
                case '(':
                    stackparen.append(c)
                case ')':
                    if not stackparen or stackparen[-1] != '(':
                        return False
                    else:
                        stackparen.pop()
                case '{':
                    stackparen.append(c)
                case '}':
                    if not stackparen or stackparen[-1] != '{':
                        return False
                    else:
                        stackparen.pop()
                case '[':
                    stackparen.append(c)
                case ']':
                    if not stackparen or stackparen[-1] != '[':
                        return False
                    else:
                        stackparen.pop()

        if stackparen:
            return False
        else:
            return True
                



sol = Solution()

s = "(]"
print(s)

result = sol.isValid(s)
print(result)
