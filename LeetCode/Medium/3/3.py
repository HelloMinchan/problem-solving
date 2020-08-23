class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        
        for i in range(len(s)):
            temp = 1
            
            alpha_hash = dict()
            alpha_hash[s[i]] = 1
            
            for j in range(i + 1, len(s)):
                if alpha_hash.get(s[j], 0):
                    break
                else:
                    alpha_hash[s[j]] = 1
                    temp += 1
            
            answer = max(answer, temp)
        
        return answer
