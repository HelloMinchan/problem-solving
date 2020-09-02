class Solution:
    
    def convert(self, s: str, numRows: int) -> str:

        def DFS(depth, s, numRows):
            global rows, pointer
            
            if depth == numRows - 1:
                if pointer < len(s):
                    rows[depth].append(s[pointer])
                    pointer += 1
                return
            
            rows[depth].append(s[pointer])
            pointer += 1
            
            if pointer < len(s):
                DFS(depth + 1, s, numRows)
                
            if depth != 0 and pointer < len(s):
                rows[depth].append(s[pointer])
                pointer += 1

        global rows, pointer
        
        pointer = 0
        rows = [[] for _ in range(numRows)]
        
        while pointer < len(s):
            DFS(0, s, numRows)
        
        answer = ""
        for row in rows:
            for char in row:
                answer += char
        
        return answer
