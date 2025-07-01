from typing import List


class Solution:
    DIG_ENG = {"2": ['a', 'b', 'c'],
               "3": ['d', 'e', 'f'],
               "4": ['g', 'h', 'i'],
               "5": ['j', 'k', 'l'],
               "6": ['m', 'n', 'o'],
               "7": ['p', 'q', 'r', 's'],
               "8": ['t', 'u', 'v'],
               "9": ['w', 'x', 'y', 'z']}

    def searchCombinations(self, char_list: List[List[str]], cur_index: int, path: List[str], result: list[str]):
        if cur_index > len(char_list) - 1:
            result.append(''.join(path[:]))
            return

        for char in char_list[cur_index]:
            self.searchCombinations(char_list, cur_index + 1, path + [char], result)

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        char_list = [self.DIG_ENG[c] for c in digits]
        result = []
        self.searchCombinations(char_list, 0, [], result)
        return result

# print(Solution().letterCombinations("23"))
