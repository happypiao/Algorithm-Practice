# 使用小顶堆来实现 前K个高频元素
# 时间复杂度 O(Nlogk)
# 空间复杂度 O(N)
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. 统计元素出现的频率
        stat_map = {}
        for n in nums:
            stat_map[n] = stat_map.get(n, 0) + 1

        # 2. 构造数量为K的小顶堆来
        small_dq = []
        for n, freq in stat_map.items():
            heapq.heappush(small_dq, (freq, n))
            if len(small_dq) > k:
                heapq.heappop(small_dq)

        # 3. 输出结果
        result = []
        for _ in range(k):
            result.append(heapq.heappop(small_dq)[1])

        return result
