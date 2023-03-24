from collections import defaultdict

my_str = input().strip()

alpha_dict = defaultdict(int)
for alpha in my_str:
    alpha_dict[alpha] += 1

answer = ""
alpha_infos = sorted(
    alpha_dict.items(), key=lambda alpha_info: (-alpha_info[1], alpha_info[0])
)

max_count = alpha_infos[0][1]
for alpha_info in alpha_infos:
    if alpha_info[1] == max_count:
        answer += alpha_info[0]
    else:
        break

print(answer)
