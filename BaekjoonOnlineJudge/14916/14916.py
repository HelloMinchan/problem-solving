# 5:06 ~ 5:15 (9분)

n = int(input())

dp_table = [-1 for _ in range(n + 1)]

for i in range(1, n + 1):
    if i == 2:
        dp_table[i] = 1
    elif i == 5:
        dp_table[i] = 1
    else:
        if i >= 2 and dp_table[i - 2] != -1:
            dp_table[i] = dp_table[i - 2] + 1
        if i >= 5 and dp_table[i - 5] != -1:
            dp_table[i] = dp_table[i - 5] + 1

print(dp_table[-1])
