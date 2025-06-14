import sys


def find_max_sort(total_num, max_k_num, shumu_dp):
    left_i = 0
    right_i = 0
    max_length_num = 0
    for i in ''.join(map(str, shumu_dp)).split('1'):
        if len(i) > max_length_num:
            max_length_num = len(i)
    while right_i < total_num:
        tmp_sum = sum(shumu_dp[left_i: right_i + 1])
        if tmp_sum <= max_k_num:
            max_length_num = max(max_length_num, right_i - left_i + 1)
            right_i += 1
        else:
            left_i += 1
    return max_length_num


if __name__ == "__main__":
    total_num = int(sys.stdin.readline().strip())
    noactive_num = int(sys.stdin.readline().strip())
    noactive_ids = list(map(int, sys.stdin.readline().strip().split()))
    shumu_dp = [0] * total_num
    for noactive_id in noactive_ids:
        shumu_dp[noactive_id - 1] = 1
    max_k_num = int(sys.stdin.readline().strip())
    print(find_max_sort(total_num, max_k_num, shumu_dp))