# 시간복잡도 O(8^n) 이므로 시간초과
# 후에 동적계획법 배우고 다시 해결할 것

from collections import deque
import sys
input = sys.stdin.readline


def BFS(i, j):
    dq = deque()
    dq.append((i, j))
    wordPointer = 1

    while(len(dq)):
        if len(word) == wordPointer:
            return True

        dqSize = len(dq)
        for _ in range(dqSize):
            x, y = dq.popleft()

            for way in range(8):
                ii = x + dx[way]
                jj = y + dy[way]
            
                if ii < 0 or ii > 4 or jj < 0 or jj > 4:
                    continue

                if word[wordPointer] == gameBoard[ii][jj]:
                    dq.append((ii, jj))

        wordPointer += 1
    
    return False


C = int(input())
dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(C):
    gameBoard = [list(input().rstrip()) for _ in range(5)]
    N = int(input())
    
    for _ in range(N):
        word = input().rstrip()

        isPossible = False
        for i in range(5):
            for j in range(5):
                if gameBoard[i][j] == word[0]:
                    if(BFS(i, j)):
                        isPossible = True
                        break
                if isPossible:
                    break

        if isPossible:
            print(word, "YES")
            continue

        print(word, "NO")