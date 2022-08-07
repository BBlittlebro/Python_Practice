class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        test = minutesToTest / minutesToDie + 1
        return ceil(log(buckets) / log(test))

# ref:https://leetcode.com/problems/poor-pigs/discuss/2386318/C%2B%2B-solution-100-faster-with-some-some-explaination