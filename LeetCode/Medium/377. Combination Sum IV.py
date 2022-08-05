class Solution:
    ans = 0
    dp = {}
    
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
##################################################
# DP 作法
def combinationSum4(self, nums: list[int], target: int) -> int:
	
		# Sort the nums to break the loop when total - num becomes negative.
        nums.sort()
		# Allocates the dp table
        dp = [0] * (target + 1)
        # The case total becomes 0 is only 1 (nothing add)
        dp[0] = 1

		# Try the all cases the total from 1 to target
        for total in range(1, target + 1):
			# Try all possible numbers.
            for num in nums:
                if total - num >= 0:
					# Uses the previous information
                    dp[total] += dp[total - num]
                else:
                    break
        return dp[target]

##################################################
# dict 結合 DP
class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = {}
        dp[0] = [1]   # {0: [1]}

        def search(target):
            if target < 0:
                return
            if target in dp:
                return dp[target]
            sum = 0
            for num in nums:
                if num < target:
                    sum += search(target-num)
                elif num == target:
                    sum += 1
            dp[target] = sum
            return sum
        return search(target)
                
obj = Solution()
print(obj.combinationSum4([4,2,1], 32))