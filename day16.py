class Solution:
    def maxPathScore(self, grid, k):
        m, n = len(grid), len(grid[0])

        dp = [[-1] * (k + 1) for _ in range(n)]
        dp[0][0] = 0

        for i in range(m):
            new_dp = [[-1] * (k + 1) for _ in range(n)]

            for j in range(n):
                for c in range(k + 1):
                    if dp[j][c] == -1:
                        continue

                    # Move right
                    if j + 1 < n:
                        cost = 1 if grid[i][j + 1] == 1 else 0
                        if c + cost <= k:
                            new_dp[j + 1][c + cost] = max(
                                new_dp[j + 1][c + cost],
                                dp[j][c] + grid[i][j + 1]
                            )

                    # Move down
                    if i + 1 < m:
                        cost = 1 if grid[i + 1][j] == 1 else 0
                        if c + cost <= k:
                            new_dp[j][c + cost] = max(
                                new_dp[j][c + cost],
                                dp[j][c] + grid[i + 1][j]
                            )

                    # Start cell
                    if i == 0 and j == 0 and c == 0:
                        new_dp[j][c] = 0

            dp = new_dp

        ans = max(dp[n - 1])
        return ans if ans != -1 else -1


# -------- USER INPUT --------
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

print("Enter grid row by row (space-separated 0/1/2):")
grid = []
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

k = int(input("Enter k value: "))

# -------- RUN --------
sol = Solution()
result = sol.maxPathScore(grid, k)

print("Maximum Path Score:", result)

# sample input
# Enter number of rows: 2
# Enter number of columns: 2
# Enter grid row by row (space-separated 0/1/2):
# 0 1
# 2 0
# Enter k value: 1

# output
# Maximum Path Score: 2
