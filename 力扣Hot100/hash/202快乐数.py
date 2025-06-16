import math


class Solution:
    def isHappy(self, n: int) -> bool:
        cal_records = set()

        while True:
            n = self.calculate_sum(n)
            if n == 1:
                return True

            if n in cal_records:
                return False
            else:
                cal_records.add(n)

    def calculate_sum(self, n: int) -> int:
        n_str = str(n)
        total = 0
        for c in n_str:
            total += int(math.pow(int(c), 2))

        return total

