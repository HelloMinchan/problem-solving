from collections import deque
import sys

input = sys.stdin.readline


# bfs 함수
def bfs(dq):
    # 단지의 집 개수를 저장하는 변수
    count = 0

    # 큐가 존재 할 때까지
    while dq:
        # 큐에 있는 집의 좌표를 꺼냄
        i, j = dq.popleft()

        # 집이 있었으므로 카운트 1 증가
        count += 1


        # 방향 벡터를 돌림 동, 서, 남, 북
        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            # 보드를 초과한 좌표는 생략 (왜? 리스트 아웃오브 레인지 에러가 발생하니까)
            if ii < 0 or ii > N - 1 or jj < 0 or jj > N - 1:
                continue
            
            # 만약에 보드가 1이고(집인경우), 비짓이 아니면(방문을 안했다면)
            if board[ii][jj] == "1" and not visit[ii][jj]:
                # 방문한다
                visit[ii][jj] = True

                # 큐에 좌표를 넣음
                dq.append((ii, jj))
    
    # 단지의 집 개수를 답 리스트에 추가함
    answer_list.append(count)

    
N = int(input())

# 보드를 받아옴
board = [list(input().rstrip()) for _ in range(N)]
# 방문기록 저장 배열 만듬
visit = [[False for _ in range(N)] for _ in range(N)]

# 방향 벡터
dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 답을 저장할 리스트
answer_list = []

# 완전 탐색
for i in range(N):
    for j in range(N):
        if board[i][j] == "1" and not visit[i][j]:
            # 방문 기록 남김
            visit[i][j] = True

            # 큐 생성
            dq = deque()
            # 큐에 단지의 시작 좌표를 추가함
            dq.append((i,j))

            # bfs 돌림
            bfs(dq)

# 단지수 출력
print(len(answer_list))
# 오름차순으로 단지의 집 개수 출력
for answer in sorted(answer_list):
    print(answer)