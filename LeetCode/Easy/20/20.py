class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for p in s:
            if p == '(':
                stack.append(p)
            elif p == '[':
                stack.append(p)
            elif p == '{':
                stack.append(p)
            else:
                if stack:
                    top = stack.pop()

                    if p == ')':
                        if top != '(':
                            return False    
                    elif p == ']':
                        if top != '[':
                            return False
                    else:
                        if top != '{':
                            return False
                else:
                    return False
        else:
            if stack:
                return False
            else:
                return True