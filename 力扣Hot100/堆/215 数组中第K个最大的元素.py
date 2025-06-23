import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mid_num = random.choice(nums)
        large, mid, small = [], [], []
        for n in nums:
            if n > mid_num:
                large.append(n)
            elif n == mid_num:
                mid.append(n)
            else:
                small.append(n)

        if len(large) >= k:
            return self.findKthLargest(large, k)
        if len(nums) - len(small) < k:
            return self.findKthLargest(small, k - (len(nums) - len(small)))

        return mid_num
