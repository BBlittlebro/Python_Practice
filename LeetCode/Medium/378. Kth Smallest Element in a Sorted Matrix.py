class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        ans = []
        for i in matrix:
            for j in i:
               ans.append(j)
        ans.sort()
        return ans[k-1]

ans = Solution()
print(ans.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
print(ans.kthSmallest([[-5]], 1))

###############################

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        return sorted(sum(matrix, []))[k-1]

###############################

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)

        left = matrix[0][0]
        right = matrix[-1][-1]

        while left < right:
            mid = (left + right) // 2
            temp = n - 1
            count = 0

            for i in range(n):
                while temp >= 0 and matrix[i][temp] > mid:
                    temp -= 1
                count += (temp+1)
            
            if count < k:
                left = mid + 1
            else:
                right = mid
        
        return left
