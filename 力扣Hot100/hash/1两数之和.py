import sys


class Solution(object):

    def two_sum(self, nums: list[int], target: int) -> list[int]:
        result = []

        try:
            # Step 1. 定义一个set来保存数组中的元素，用于对元素进行快速查找
            item_map = dict()

            # Step 2. 遍历数组array, 判断target-array元素的余数是否在item_map中
            for index, item in enumerate(nums):
                free_num = target - item
                if free_num in item_map:
                    result = [item_map[free_num], index]
                    break
                item_map[item] = index

        except Exception as err:
            # Exception暂统一处理
            print(err)
            return []

        return result


if __name__ == "__main__":
    input_nums = list(map(int, sys.stdin.readline().strip().split(',')))
    input_target = int(sys.stdin.readline().strip())
    print(Solution().two_sum(nums=input_nums, target=input_target))
