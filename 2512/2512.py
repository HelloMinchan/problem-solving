import sys
input = sys.stdin.readline

N = int(input())
inquiredBudget = list(map(int, input().split()))
totalBudget = int(input())
result = 0
left = 0
right = max(inquiredBudget)

while left <= right:
    assignedBudget = 0
    mid = (left + right) // 2

    for budget in inquiredBudget:
        if budget - mid < 0:
            assignedBudget += budget
            continue
        assignedBudget += mid
    
    if totalBudget < assignedBudget:
        right = mid - 1
    else:
        print(result)
        result = mid
        left = mid + 1

print(result)