class Solution:
    def maximumJumps(self, nums, target):
        n = len(nums)

        # dp[i] = maximum jumps to reach index i
        dp = [-1] * n
        dp[0] = 0

        for i in range(n):
            if dp[i] == -1:
                continue

            for j in range(i + 1, n):
                if abs(nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)

        return dp[-1]


# User Input
nums = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target: "))

obj = Solution()
print("Maximum jumps:", obj.maximumJumps(nums, target))
#sample input and output

# Sample Input
# Enter array elements: 1 3 6 4 1 2
# Enter target: 2
# Sample Output
# Maximum jumps: 3
