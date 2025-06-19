# 单调队列-适用双端队列
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()

        for i, n in enumerate(nums):
            # 队列中小于n的元素需要全部pop出来
            while dq and dq[-1] < n:
                dq.pop()
            dq.append(n)

            # 判断队列左边第一个元素刚好等于上个窗口需要抛弃的元素时，直接popleft出去
            if i >= k and nums[i - k] == dq[0]:
                dq.popleft()

            # 当下标i大于等于k-1 也就是第一个滑动窗口最右边的下标时，dq[0]即为最大值
            if i >= k - 1:
                result.append(dq[0])

        return result

