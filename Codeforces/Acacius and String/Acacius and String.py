from collections import deque
import sys
input = sys.stdin.readline


def isPossible(string):
    possible = False
    correct = "abacaba"
    count = 0
    temp = list(string)
    for i in range(len(string)):
        if temp[i] == correct[count]:
            count += 1
        else:
            if temp[i] == '?':
                dq.append(correct[count])
                temp[i] = correct[count]
                count += 1
            else:
                count = 0
                continue
        if count == 7:
            ol = 0
            for i in range(n - 7 + 1):
                if "abacaba" in "".join(temp[i:i + 7]):
                    ol += 1
            if ol == 1:
                possible = True
            break

    return possible


T = int(input())

for _ in range(T):
    n = int(input())
    string = input().rstrip()
    dq = deque()

    isQuestion = False
    if '?' in string:
        isQuestion = True
        
    overlap = 0
    for i in range(n - 7 + 1):
        if "abacaba" in string[i:i + 7]:
            overlap += 1
    
    # 가능한 경우
    if overlap == 1:
        print("Yes")
        if isQuestion:
            for s in string:
                if s == '?':
                    print('z', end="")
                else:
                    print(s, end="")
            print()
        else:
            print(string)
    else:
        if overlap != 0:
            print("No")
        else:
            # 아모른직다
            if isQuestion:
                if isPossible(string):
                    print("Yes")
                    for s in string:
                        if s == "?":
                            if dq:
                                print(dq.popleft(), end="")
                            else:
                                print('z', end="")
                        else:
                            print(s, end="")
                    print()
                else:
                    print("No")
            else:
                print("No")
