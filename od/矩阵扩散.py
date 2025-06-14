import sys
from collections import deque

squa_m, squa_n, point_i, point_j, point_k, point_l = map(int, sys.stdin.readline().strip().split(','))

init_array = [[0] * squa_n for _ in range(squa_m)]
visited_array = [[0] * squa_n for _ in range(squa_m)]

visited_array[point_i][point_j] = 1
visited_array[point_k][point_l] = 1
# 定义一个队列来取值遍历
search_queue = deque()

search_queue.append((point_i, point_j, 0))
search_queue.append((point_k, point_l, 0))


def around_search(search_queue):
    cost_max_time = 0
    while search_queue:
        search_i, search_j, cost_time = search_queue.popleft()

        if init_array[search_i][search_j] == 0:
            init_array[search_i][search_j] = 1
            visited_array[search_i][search_j] = 1
            for move_x, move_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_point_x = search_i + move_x
                new_point_y = search_j + move_y
                if squa_m > new_point_x >= 0 and 0 <= new_point_y < squa_n and visited_array[new_point_x][new_point_y] == 0:
                    search_queue.append((new_point_x, new_point_y, cost_time + 1))

        cost_max_time = max(cost_max_time, cost_time)

    return cost_max_time


if __name__ == "__main__":
    print(around_search(search_queue))
