def solution(n, times):
    left = 0
    right = max(times) * n
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        processing_count = 0

        for time in times:
            processing_count += mid // time

        if processing_count >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer