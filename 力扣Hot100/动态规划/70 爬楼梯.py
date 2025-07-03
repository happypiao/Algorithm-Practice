class Solution:
    def climbStairs(self, n: int) -> int:
        step1, step2 = 0, 1
        tmp = 0
        for i in range(2, n+1):
            tmp = step1 + step2
            step1, step2 = step2, tmp
        return tmp


