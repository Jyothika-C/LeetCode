def maxScore(grid):
    n = len(grid)
    
    # prefix sum for each column
    prefix = [[0]*n for _ in range(n+1)]
    
    for j in range(n):
        for i in range(n):
            prefix[i+1][j] = prefix[i][j] + grid[i][j]
    
    dp = [0]*n
    
    for j in range(n):
        new_dp = [0]*n
        for i in range(n):
            for k in range(n):
                gain = 0
                
                if j > 0:
                    if k > i:
                        gain = prefix[k][j-1] - prefix[i][j-1]
                    else:
                        gain = prefix[i][j] - prefix[k][j]
                
                new_dp[i] = max(new_dp[i], dp[k] + gain)
        
        dp = new_dp
    
    return max(dp)


# -------- USER INPUT --------
n = int(input("Enter grid size (n): "))

grid = []
print("Enter the grid row by row:")

for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# -------- OUTPUT --------
result = maxScore(grid)
print("Maximum Score:", result)




#Sample Input
# Enter grid size (n): 3
# Enter the grid row by row:
# 1 2 3
# 4 5 6
# 7 8 9

#sample output
#Maximum Score: 24
