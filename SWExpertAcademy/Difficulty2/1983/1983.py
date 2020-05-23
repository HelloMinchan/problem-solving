t = int(input())
for case in range(t):
    N, k = map(int, input().split())
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    sum_list = []
    for i in range(N):
        mid, fin, assign = map(int, input().split())
        sum_list.append([mid*0.35+fin*0.45+assign*0.2, i+1])
    sum_list.sort(reverse=True)
    for i in range(N):
        if sum_list[i][1] == k:
            rank = i
            break
    print('#{} {}'.format(case+1, grade[rank//(N//10)]))
