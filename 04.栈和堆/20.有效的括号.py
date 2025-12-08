class Solution:
    def isValid(self, s: str) -> bool:
        #遇到左括号压栈，遇到右括号就检查栈顶是否是对应的左括号。
        stack = []
        pair = {')':'(', ']':'[', '}':'{'}
        
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack or stack[-1] != pair[c]:
                    return False
                stack.pop()
        
        return not stack
