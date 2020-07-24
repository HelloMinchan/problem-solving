import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    A = list(input().rstrip())
    B = list(input().rstrip())

    answer = 0
    cur = 0
    isWrong = False
    isDiff = False
    temp = 0
    tempChar = A[0]

    while cur < n:
        if A[cur] != B[cur]:
            if tempChar > B[cur]:
                if isDiff:
                    A[temp] = tempChar
                    cur = temp
                    cur = temp
                    answer += 1
                else:
                    isWrong = True
                    break
            else:
                isDiff = True
                temp = cur
                tempChar = A[cur]
                A[cur] = B[cur]
                
                if cur + 1 < n:
                    if A[cur] != A[cur + 1]:
                        isDiff = False
                        answer += 1
                    cur += 1
                else:
                    answer += 1
                    break
        else:
            if isDiff:
                isDiff = False
                answer += 1
            cur += 1
    
    if isWrong or answer == 0:
        print(-1)
    else:
        print(answer)
