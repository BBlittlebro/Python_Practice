# 46 ms, 14 MB          => 遞迴
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def dfs(num):
            if num < 0:
                return 0
            if num == 0:
                return 1
            if num in dp:
                return dp[num]
            
            one_step = dfs(num-1)
            two_step = dfs(num-2)

            dp[num] = one_step + two_step
            return dp[num]
        
        return dfs(n)

#############################
# 39 ms, 13.9 MB        => 費氏
class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1

        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            for i in range(2, n+1):
                temp = b
                b += a
                a = temp
        return b

a = Solution()
ans = a.climbStairs(6)
print(ans)
