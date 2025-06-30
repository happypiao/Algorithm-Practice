from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def search_combine(self, n: int, k: int, start_n: int, path: List[int]):
        if len(path) == k:
            self.result.append(path.copy())
        for i in range(start_n, n + 1):
            path.append(i)
            self.search_combine(n, k, i + 1, path)
            path.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.search_combine(n, k, 1, [])
        return self.result
