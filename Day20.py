class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # Step 1: Transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()


# ---- User Input ----
n = int(input("Enter size of matrix: "))
matrix = []

print("Enter matrix rows:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Process
obj = Solution()
obj.rotate(matrix)

# Output
print("Rotated Matrix:")
for row in matrix:
    print(*row)

# sample input:
# Enter size of matrix: 3
# Enter matrix rows:
# 1 2 3
# 4 5 6
# 7 8 9
# sample output
# Rotated Matrix:
# 7 4 1
# 8 5 2
# 9 6 3