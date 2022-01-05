import heapq

def solution(food_times, stop_time):
    food_heapq = []
    
    for number, food_time in enumerate(food_times):
        heapq.heappush(food_heapq, (food_time, number + 1))
    
    food_heapq_length = len(food_heapq)
    pre_food_time = 0
    
    while food_heapq:
        if ((food_heapq[0][0] - pre_food_time) * food_heapq_length) <= stop_time:
            food_time, number = heapq.heappop(food_heapq)
            stop_time -= (food_time - pre_food_time) * food_heapq_length
            food_heapq_length -= 1
            pre_food_time = food_time
        else:
            stop_time = stop_time % food_heapq_length
            return sorted(food_heapq, key = lambda el:el[1])[stop_time][1]
    
    if not food_heapq:
        return -1
    else:
        return sorted(food_heapq, key = lambda el:el[1])[0][1]