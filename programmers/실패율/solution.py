from collections import deque


def solution(N, stages):
    stages.sort()
    stage_queue = deque(stages)

    arrive_list = []
    for stage in range(1, N + 1):
        total_user = len(stage_queue)
        stage_count = 0

        while stage_queue and stage_queue[0] == stage:
            stage_queue.popleft()
            stage_count += 1

        if stage_count == 0 or total_user == 0:
            arrive_list.append((stage, 0))
        else:
            arrive_list.append((stage, stage_count / total_user))

    arrive_list.sort(key=lambda arrive: (-arrive[1], arrive[0]))

    return [arrive[0] for arrive in arrive_list]
