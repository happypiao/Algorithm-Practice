from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        left, right = 0, m - 1
        k = (m + n + 1) // 2
        while left <= right:
            i = (left + right) // 2
            j = k - i
            if i > 0 and nums1[i - 1] > nums2[j]:
                right = i - 1
            elif i < m and nums2[j - 1] > nums1[i]:
                left = i + 1
            else:
                # 左边最大
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_left

                # 右边最小
                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums2[j], nums1[i])

                return (max_left + min_right) / 2.0
