#  区间合并，考虑左右边界重叠问题
# 时间复杂度，O(NlogN)
# 空间复杂度 O(1)
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merge_result = []
        tmp_merge = intervals[0]
        for n in intervals[1:]:
            if n[0] <= tmp_merge[1]:
                tmp_merge = [tmp_merge[0], max(tmp_merge[1], n[1])]
            else:
                merge_result.append(tmp_merge)
                tmp_merge = n

        if tmp_merge:
            merge_result.append(tmp_merge)

        return merge_result


