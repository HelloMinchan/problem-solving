class Solution:
    
    def removeElement(self, numbers: List[int], val: int) -> int:
        global nums
        
        while val in numbers:
            numbers.remove(val)
        
        return len(numbers)
