class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        accept = False
        patterns = ['{}', '[]', '()']
        for i in s:
            if i in ("[", "{", "("):
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                value = stack.pop()
                if (value + i) in patterns:
                    accept = True
                else:
                    accept = False
                    break
        
        if not accept or len(stack) != 0:
            return False
        else:
            return True