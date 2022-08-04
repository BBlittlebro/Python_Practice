class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        Gcd = self.gcd(p,q)     # 不一定要最簡，不要都是 2 的倍數就好
        box = q / Gcd
        reflect = p / Gcd

        if reflect % 2 == 0:
            return 2
        elif box % 2 == 0: return 0
        else: return 1

    def gcd(self, p, q):
        p = p % q
        if p == 0:
            return q
        else:
            return self.gcd(q, p)


ans = Solution()
print(ans.mirrorReflection(14, 6))