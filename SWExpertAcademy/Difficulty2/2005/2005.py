t = int(input())
for case in range(t):
    print('#{}'.format(case+1))
    height = int(input())
    pre = []    #이전 행의 규칙을 저장해 놓을 리스트
    for h in range(1, height+1):
        arr = []    #현재 행의 규칙을 저장할 리스트
        for i in range(h):
            #규칙 1. 첫 번째 줄은 항상 숫자 1이다.
            if i == 0:
                arr.append(1)
            #규칙 2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.
            else:
            #현재 행이 마지막 인덱스일 경우 이전 행의 전체 길이와 같으므로 1삽입
                if i == len(pre):
                    arr.append(1)
                #아닐 경우 현재 행의 인덱스 기준으로 이전 행에서 값을 구함
                else:
                    arr.append(pre[i]+pre[i-1])
            print(arr[i] , end = ' ')
        #이전 행의 규칙에 현재 행의 규칙 저장
        pre = arr
        print()
