from collections import defaultdict


def solution(id_list, report, k):
    answer = []

    report_list = defaultdict(set)
    black_list = defaultdict(int)

    # 중복제거
    for name in report:
        p1, p2 = name.split()
        report_list[p1].add(p2)

    # 블랙리스트 찾기
    for names in report_list.values():
        for name in names:
            black_list[name] += 1

    # 신고한 사람 별 블랙리스트 찾기
    for name in id_list:
        count = 0
        if report_list.get(name, 0):
            for report_name in report_list[name]:
                if black_list[report_name] >= k:
                    count += 1

        answer.append(count)

    return answer