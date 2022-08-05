# 69 ms, 13.8 MB
class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        dict2 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0

        for key, val in dict1.items():
            if s.find(key) != -1:
                ans += val
                s = s.replace(key, '')
        
        for key, val in dict2.items():
            num = s.count(key)
            ans += val * num
            s = s.replace(key, '')
        return ans

#######################
# 改成直接取得字串
# 84 ms, 14 MB
class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        dict2 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0

        print(dict2["I"])

        for key, val in dict1.items():
            if s.find(key) != -1:
                ans += val
                s = s.replace(key, '')
        
        for i in s:
            ans += dict2[i]
        return ans

a = Solution()
ans = a.romanToInt("MCMXCIV")
print(ans)

