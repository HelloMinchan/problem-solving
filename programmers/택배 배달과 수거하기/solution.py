def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    total_delivery = 0
    total_pickup = 0

    for i in range(n):
        total_delivery += deliveries[i]
        total_pickup += pickups[i]

        while total_delivery > 0 or total_pickup > 0:
            total_delivery -= cap
            total_pickup -= cap
            answer += (n - i) * 2

    return answer
