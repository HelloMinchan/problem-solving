class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        N = len(s1)

        s1 = sorted(list(s1))[:]
        s2 = sorted(list(s2))[:]
        
        for i in range(N):
            if s1[i] < s2[i]:
                break
        else:
            return True
        
        for i in range(N):
            if s1[i] > s2[i]:
                break
        else:
            return True
        
        return False