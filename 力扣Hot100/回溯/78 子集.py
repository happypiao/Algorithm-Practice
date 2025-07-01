from typing import List


class Solution:

    def search_subsets(self, nums: List[int], start_index: int, path: List[int], result: List[List[int]]):
        result.append(path[:])
        if start_index > len(nums) - 1:
            return

        for i in range(start_index, len(nums)):
            self.search_subsets(nums, i + 1, path + [nums[i]], result)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.search_subsets(nums, 0, [], result)
        return result
