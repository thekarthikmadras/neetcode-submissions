class Solution:
    def isValid(self, s: str) -> bool:
        opntocls = {'}':'{', ']':'[', ')':'('}
        stack = []
        for c in s:
            if c in opntocls:
                if stack and stack[-1] == opntocls[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return False if stack else True
            
