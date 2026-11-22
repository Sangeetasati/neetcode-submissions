class Solution:
    def isValid(self, s: str) -> bool:
        sym = { '(' : ')', '[' : ']', '{' : '}'}
        stack = []
        for i in range(len(s)):
            print('stack', stack)
            if stack and stack[-1] not in sym:
                return False
            if stack and sym[stack[-1]] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        if len(stack)>0:
            return False
        return True
