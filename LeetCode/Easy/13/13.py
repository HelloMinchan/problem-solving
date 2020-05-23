class Solution:
    def f(x):
        return {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}[x]
    def romanToInt(self, s: str) -> int:
        sum = 0
        temp = 0
        
        i=0
        while i<len(s):
            x = Solution.f(s[i])
            if i!=len(s)-1:
                temp = Solution.f(s[i+1]) - x
                if temp==4 or temp==9 or temp==40 or temp==90 or temp==400 or temp==900:
                    sum += temp
                    i+=1
                else:
                    sum += x
            else:
                sum += x
            i+=1
        
        return sum
