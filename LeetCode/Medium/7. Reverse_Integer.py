# 84 ms, 13.9 MB, 整數算法
class Solution:
    def reverse(self, x: int) -> int:
        less_than_0 = False
        ans = 0
        
        if x < 0:
            less_than_0 = True
            x = -x
        elif x == 0:
            return 0
    
        while x > 0:
            temp = x % 10
            ans *= 10
            ans += temp
            x //= 10
        
        if less_than_0:
            ans *= -1
        
        if ans > 2147483647 or ans < -2147483648:
            return 0
        else:
            return ans
########################################

# 41 ms, 13.8 MB, 轉成字串
class Solution:
    def reverse(self, x: int) -> int:
        ans = ''
        if x < 0:
            x = str(-x)
            ans += '-'
        elif x > 0:
            x = str(x)
        else:
            return 0
        x = x[::-1]
        
        if int(x) > 2147483647:
            return 0
        
        flag = False
        for i in x:
            if flag == False:
                if i != '0':
                    ans += i
                    flag = True
            else:
                ans += i
        ans = int(float(ans))
        
        if ans > 2147483647 or ans < -2147483648:
            return 0
        else:
            return ans
        