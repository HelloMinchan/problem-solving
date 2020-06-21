def DFS(L, nums, visit):
    global ans, stack
    
    if len(stack) == 3:
        ans.append(sum(stack))
        return
    
    for i in range(L, len(nums)):
        if not visit[i]:
            visit[i] = True
            stack.append(nums[i])
            DFS(i + 1, nums, visit)
            visit[i] = False
            stack.pop()
            
    
def solution(nums):
    global ans, stack
    answer = 0
    ans = []
    stack = []
    
    visit = [False] * len(nums)
    DFS(0, nums, visit)
    
    isPrime = [False] + [False] + [True] * (max(ans) - 1)

    for i in range(2, max(ans) + 1):
        if isPrime[i]:
            for j in range(i * 2, max(ans) + 1, i):
                isPrime[j] = False
    
    for num in ans:
        if isPrime[num]:
            answer += 1
            
    return answer
