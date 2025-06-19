# 使用三个指针
# 时间 O(N*N)
# 空间 O(1)
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for first_i in range(len(nums)):
            if nums[first_i] > 0:
                return result

            if first_i > 0 and nums[first_i] == nums[first_i - 1]:
                continue

            left, right = first_i + 1, len(nums) - 1
            while left < right:
                total = nums[first_i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    result.append([nums[first_i], nums[left], nums[right]])
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    left += 1
                    right -= 1

        return result

