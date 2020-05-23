import sys
input = sys.stdin.readline


def fibo(n, i, tb, ob):
    if n == i:
        print(tb + ob)
        exit()
    temp = tb + ob
    tb = ob
    ob = temp
    i += 1
    return fibo(n, i, tb, ob)


n = int(input())

if n == 0 or n == 1:
    print(n)
    exit()

tb = 0
ob = 1
i = 2
fibo(n, i, tb, ob)