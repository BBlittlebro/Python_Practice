class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from math import factorial
        down = m-1
        right = n-1
        total = down + right
        return int(factorial(total) / factorial(down) / factorial(right))