import sys
input = sys.stdin.readline


def failFunc(clock):
    table = [0] * len(clock)
    j = 0

    for i in range(1, len(clock)):
        while j > 0 and clock[i] != clock[j]:
            j = table[j - 1]
        
        if clock[i] == clock[j]:
            j += 1
            table[i] = j

    return table


def KMP(clock1 , clock2):
    j = 0

    for i in range(len(clock1)):
        while j > 0 and clock1[i] != clock2[j]:
            j = table2[j - 1]
        
        if clock1[i] == clock2[j]:
            if j == len(clock2) - 1:
                return True
            else:
                j += 1
    
    return False


n = int(input())

hash1 = ['0'] * 360000
hash2 = ['0'] * 360000

clock1 = list(map(int, input().split()))
clock2 = list(map(int, input().split()))

for time in clock1:
    hash1[time] = '1'

for time in clock2:
    hash2[time] = '1'

string1 = "".join(hash1)
string1 = string1 * 2
string2 = "".join(hash2)

table2 = failFunc(string2)

if KMP(string1, string2):
    print("possible")
else:
    print("impossible")
