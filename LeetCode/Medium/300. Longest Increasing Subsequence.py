from bisect import bisect, bisect_left


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        temp = [nums.pop(0)]
        for n in nums:
            if n > temp[-1]:
                temp.append(n)
            else:
                temp[bisect_left(temp, n)] = n
        return len(temp)

#[11,12,13,14,15,6,7,8,101,18]
#[0,1,0,3,2,3]
#[1,3,6,7,9,4,10,5,6]
#[10,22,9,33,21,50,41,60,80]
nums = [10,22,9,33,21,50,41,60,80]
ans = Solution()
print('ans', ans.lengthOfLIS(nums))


            
