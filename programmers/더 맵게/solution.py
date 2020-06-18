import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while 1:
        if len(scoville) == 1:
            if scoville[0] >= K:
                return answer
            return -1

        spicy1 = heapq.heappop(scoville)
        spicy2 = heapq.heappop(scoville)

        if spicy1 < K or spicy2 < K:
            newSpicy = spicy1 + (spicy2 * 2)
            heapq.heappush(scoville, newSpicy)
            answer += 1
        else:
            return answer
