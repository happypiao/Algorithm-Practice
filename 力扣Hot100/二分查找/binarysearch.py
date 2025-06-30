from typing import List


def search(nums: List[int], target: int) -> int:
    # 二分查找 采用左闭右闭
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def get_right_boarder(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    right_boarder = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            right_boarder = mid
            left = mid + 1
        else:
            left = mid + 1

    return right_boarder


def get_left_boarder(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    left_boarder = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            left_boarder = mid
            right = mid - 1
        else:
            left = mid + 1

    return left_boarder


print(get_left_boarder([1, 3, 3, 4], 3))
