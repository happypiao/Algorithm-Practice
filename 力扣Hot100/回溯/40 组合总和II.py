from typing import List


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates) - 1
        candidates.sort()

        def search_combination(start: int, end: int, path: List[int], free: int):
            if free == 0:
                result.append(path[:])
            for i in range(start, end + 1):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > free:
                    break
                search_combination(i + 1, n, path + [candidates[i]], free - candidates[i])

        search_combination(0, n, [], target)
        return result