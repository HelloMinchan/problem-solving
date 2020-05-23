t = int(input())
for case in range(t):
    #리스트 영역에 파리 개수 담기
    N, M = map(int, input().split())
    arr = [[0]*N for row in range(N)]
    for row in range(len(arr)):
        temp = input()
        temp = temp.split()
        arr[row] = [int(x) for x in temp]

    #최대 죽은 파리 개수 구하기
    max = 0 #죽은 파리 개수의 최댓값을 저장할 변수
    #행 반복문
    for i in range(N - M + 1):
        k = 0   #한 번에 내리칠 수 있는 열의 크기 제한할 변수
        #열 반복문
        while True:
            temp = 0    #한 번 내리쳐 죽인 파리 개수 저장할 변수
            #한 번에 내리칠 수 있는 열의 크기 제한 조건
            if k == N - M + 1:
                break
            #한 번에 내리칠 수 있는 행의 크기 제한 반복문
            for j in range(M):
                temp += sum(arr[i + j][k : k + M])
            #내리쳤을 때 죽은 파리 개수의 최댓값을 찾는 비교 조건
            if max < temp:
                max = temp
            k += 1

    print('#{} {}'.format(case+1, max))
