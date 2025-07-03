
import sys
from typing import List
from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        字母异或词分组
        时间复杂度：O(nmlogm), strs长度为n, 每个sorted实质为快排 时间复杂度为mlogm
        空间复杂度: O(nm)
        :param strs: 字符串列表
        :return:
        """
        # Step 1. tmp_result将字符串按照异或词分类保存
        tmp_result = defaultdict(list)

        # Step 2. 遍历每个元素，对字符串进行排序， 排序结果一致则为异或词
        for item in strs:
            # tmp_result[''.join(list(sorted(item)))].append(item)

            # 采用列表来计数
            chr_count = [0] * 26
            for char in item:
                chr_count[(ord(char) - ord('a')) % 26] += 1

            # 字典的key必须是不可变的值
            tmp_result[tuple(chr_count)].append(item)

        # Step 3. 结果返回
        return list(tmp_result.values())

