class Solution:
    ans = 0
    
    def combinationSum4(self, nums: list[int], target: int) -> int:
        nums.sort()
        self.combination(nums, target, 0, [], 0)
        return self.ans

    def combination(self, nums, target, sum, now_nums, i):
        if sum == target:
            self.ans += 1
            print(now_nums)
            return
        if sum > target:
            return

        for i in range(len(nums)):
            sum += nums[i]
            now_nums.append(nums[i])
            self.combination(nums, target, sum, now_nums, i)
            sum -= nums[i]
            now_nums.pop()

        return

    
obj = Solution()
print(obj.combinationSum4([1,2,3], 4))