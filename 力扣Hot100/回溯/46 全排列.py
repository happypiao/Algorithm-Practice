# 时间复杂度  O(n!)
# 空间复杂度  O(n)
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [0] * len(nums)
        self.search_permute(nums, used, [], result)
        return result

    def search_permute(self, nums: List[int], used: List[int], path: List[int], result: List[List[int]]):
        if sum(used) == len(nums):
            result.append(path[:])
        for i, num in enumerate(nums):
            if used[i] == 0:
                used[i] = 1
                self.search_permute(nums, used, path + [num], result)
                used[i] = 0
