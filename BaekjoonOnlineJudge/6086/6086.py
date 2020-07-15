from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

# 최대 정점의 수(알파벳 대문자의 수 + 알파벳 소문자의 수)
MAX = 52
# 최소 유량을 찾기 위한 양의 무한대 값
INF = 2147483647


# 정점 표시 알파벳을 숫자로 변환하는 함수
def CtoI(target):
    # 대문자일 경우 아스키 코드로 변환
    if ord(target) <= ord('Z'):
        return ord(target) - ord('A')
    
    # 소문자일 경우 아스키 코드로 변환
    return ord(target) - ord('a') + 26


# 너비 우선 탐색 함수
def BFS(source, sink, visit):
    # 너비 우선 탐색 큐
    dq = deque()

    # source 방문 표시
    visit[source] = True
    # 큐에 source 푸시
    dq.append(source)

    # 큐가 빌 때까지 탐색
    while dq:
        # 탐색할 시작 정점 팝
        sv = dq.popleft()
        
        # 시작 정점에서 가능한 도착 정점 탐색
        for dv in adjList[sv]:
            # 만약 용량이 꽉 차지 않아 흐를 수 있는 도착 정점이 있고 그 정점을 방문한적이 없다면
            if capacity[sv][dv] - flow[sv][dv] > 0 and visit[dv] == -1:
                # 도착 정점이 어떤 시작 정점에서 왔는지 대입
                visit[dv] = sv
                # 도착 정점 큐에 푸시
                dq.append(dv)

                # 만약 도착 정점이 sink라면 
                if dv == sink:
                    # 그래프 내에 흐를 수 있는 경로가 존재함
                    return True

    # 그래프 내에 흐를 수 있는 경로가 존재하지 않음
    return False


# 에드먼드 카프 알고리즘 함수
def edmondsKarp(source, sink):
    # 최대 유량 저장 변수(답)
    maximumFlow = 0

    # sink로 가는 가능한 플로우가 없을 때까지 너비 우선 탐색 실시
    while 1:
        # 너비 우선 탐색 반복 시 visit 배열 초기화
        visit = [-1] * MAX

        # 너비 우선 탐색 실패 시 가능한 플로우가 없으므로 종료
        if not BFS(source, sink, visit):
            break
        
        # 최소 유량을 기록할 변수 양의 무한대 값으로 초기화
        minFlow = INF

        # 반복 제어 변수 sink 값으로 초기화
        i = sink
        
        # 너비 우선 탐색으로 찾은 경로의 가능한 최소 유량을 찾음
        # (반복 제어 변수가 source가 아닐 때까지 반복, 찾은 경로를 거꾸로 되돌아가면서 최소 유량 찾기)
        while i != source:
            # visit[i] = sv, i = dv 이므로 용량 리스트와 유량 리스트에서 visit[i][i]로 가능한 최소 유량 찾기
            minFlow = min(minFlow, capacity[visit[i]][i] - flow[visit[i]][i])
            # 현재 정점이 어디서 왔는지 계속 되물어 감
            i = visit[i]
        
        # 반복 제어 변수 sink 값으로 초기화
        i = sink
        
        # 탐색한 경로의 최소 유량을 찾았으므로 최소유량을 경로에 갱신해줌
        # (반복 제어 변수가 source가 아닐 때까지 반복, 찾은 경로를 거꾸로 되돌아가면서 최소 유량 갱신)
        while i != source:
            # 정방향 유량 리스트에 현재 흐르고 있는 유량 갱신
            flow[visit[i]][i] += minFlow
            # 역방향 유량 리스트에 현재 흐르고 있는 유량 갱신 (유량 상쇄를 위하여)
            flow[i][visit[i]] -= minFlow
            # 현재 정점이 어디서 왔는지 계속 되물어 감
            i = visit[i]
        
        # 최대 유량에 흘러간 유량 갱신
        maximumFlow += minFlow

    # 더이상 흐를 수 있는 경로가 없을 시 최대 유량이 흐른 것이므로 답 출력
    print(maximumFlow)


# 메인 함수
if __name__ == "__main__":
    # 정점의 수
    N = int(input())

    # 인접 리스트
    adjList = [[] for _ in range(MAX)]
    # 용량 리스트
    capacity = [[0] * MAX for _ in range(MAX)]
    # 유량 리스트
    flow = [[0] * MAX for _ in range(MAX)]

    # 인접 리스트 및 용량 초기화
    for _ in range(N):
        # sv = 시작 정점, dv = 도착 정점, f = 유량
        sv, dv, f = input().split()

        # 시작 정점 알파벳 숫자로 변환
        sv = CtoI(sv)
        # 도착 정점 알파벳 숫자로 변환
        dv = CtoI(dv)

        # 용량 초기화 (중복 간선이 있으므로 += 연산)
        capacity[sv][dv] += int(f)
        capacity[dv][sv] += int(f)

        # 인접 리스트 초기화
        adjList[sv].append(dv)
        adjList[dv].append(sv)

    # source는 'A'
    source = CtoI('A')
    # sink는 'Z'
    sink = CtoI('Z')

    # 에드먼드 카프 알고리즘 적용
    edmondsKarp(source, sink)
