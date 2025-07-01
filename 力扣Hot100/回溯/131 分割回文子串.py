from typing import List


class Solution:

    def search_paths(self, s: str, start_index: int, path: List[str], result: List[List[str]]):
        if start_index > len(s) - 1:
            result.append(path[:])
        for i in range(start_index, len(s)):
            if s[start_index: i + 1] == s[start_index: i + 1][::-1]:
                self.search_paths(s, i + 1, path + [s[start_index: i + 1]], result)

    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.search_paths(s, 0, [], result)
        return result


print(Solution().partition('aab'))
