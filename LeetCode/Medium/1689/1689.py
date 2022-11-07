# 06:00 ~ 6:16
class Solution:
    def minPartitions(self, n: str) -> int:
        answer = 0

        while int(n) != 0:
            if len(n) == 1:
                return answer + int(n)
            
            first_number = n[0]

            new_n = ""
            
            for digit in n[1:]:
                if digit > first_number:
                    new_n += str(int(digit) - int(first_number))
                else:
                    new_n += "0"
            
            n = str(int(new_n))
            answer += int(first_number)
        
        return answer
        
