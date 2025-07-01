from typing import List


class Solution:

    def __init__(self):
        self.result = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates) - 1
        candidates.sort()

        def search_combination(start: int, end: int, res: List[int]):
            if sum(res) == target:
                result.append(res)
            if sum(res) > target:
                return
            for i in range(start, end + 1):
                if sum(res + [candidates[i]]) > target:
                    break
                search_combination(i, n, res + [candidates[i]])

        search_combination(0, n, [])
        return result
