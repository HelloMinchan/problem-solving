def DFS(numbers, nums, stack, visit, isPrime):
    if stack:
        nums.add(int("".join(stack)))
            
    for i in range(len(numbers)):
        if not visit[i]:
            visit[i] = True
            stack.append(numbers[i])
            DFS(numbers, nums, stack, visit, isPrime)
            visit[i] = False
            stack.pop()

    
def solution(numbers):
    answer = 0
    
    isPrime = [False] + [False] + [True] * (9999997)
    
    for i in range(2, 9999997):
        if isPrime[i]:
            for j in range(i * 2, 9999997, i):
                isPrime[j] = False
        
    stack = []
    nums = set()
    visit = [False] * len(numbers)
    
    DFS(numbers, nums, stack, visit, isPrime)
    
    for num in nums:
        if isPrime[num]:
            answer += 1
            
    return answer
