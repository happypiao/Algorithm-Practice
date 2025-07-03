from typing import List, Set


class Solution:
    """
    使用回溯算法来计算
    """

    def split_word(self, s: str, start: int, wordDict: Set[str]):
        if start > len(s) - 1:
            return True

        for i in range(start, len(s)):
            new_word = s[start: i + 1]
            if new_word in wordDict and self.split_word(s, i + 1, wordDict):
                return True

        return False

    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     wordDict = set(wordDict)
    #     return self.split_word(s, 0, wordDict)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s_len = len(s)
        dp = [False] * (s_len + 1)
        dp[0] = True

        # 排列 先背包再物品
        for i in range(1, s_len + 1):
            for j in range(i):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]
