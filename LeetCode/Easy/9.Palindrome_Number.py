# 106 ms, 13.8 MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False

a = Solution()
ans = a.isPalindrome(101)
print(ans)