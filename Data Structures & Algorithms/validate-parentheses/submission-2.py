class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        para = {'(': ')', '{': '}', '[': ']'}
        # openPara = ['(', '{', '[']
        # closePara = [')', '}', ']']
        
        for c in s:
            if c in para.keys():
                stack.append(c)
            elif not stack and c in para.values():
                return False
            elif c in para.values() and stack:
                check = stack.pop() 
                if para[check] != c:
                    return False
        
        if stack:
            return False
        return True
            