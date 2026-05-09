class Solution:
    def rotateGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        for layer in range(layers):
            elements = []

            top, left = layer, layer
            bottom, right = m - layer - 1, n - layer - 1

            # Top row
            for j in range(left, right + 1):
                elements.append(grid[top][j])

            # Right column
            for i in range(top + 1, bottom):
                elements.append(grid[i][right])

            # Bottom row
            for j in range(right, left - 1, -1):
                elements.append(grid[bottom][j])

            # Left column
            for i in range(bottom - 1, top, -1):
                elements.append(grid[i][left])

            # Rotate counter-clockwise
            rot = k % len(elements)
            elements = elements[rot:] + elements[:rot]

            idx = 0

            # Fill Top row
            for j in range(left, right + 1):
                grid[top][j] = elements[idx]
                idx += 1

            # Fill Right column
            for i in range(top + 1, bottom):
                grid[i][right] = elements[idx]
                idx += 1

            # Fill Bottom row
            for j in range(right, left - 1, -1):
                grid[bottom][j] = elements[idx]
                idx += 1

            # Fill Left column
            for i in range(bottom - 1, top, -1):
                grid[i][left] = elements[idx]
                idx += 1

        return grid


# User Input Program
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

print("Enter matrix values:")
grid = []
for i in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

k = int(input("Enter k value: "))

obj = Solution()
result = obj.rotateGrid(grid, k)

print("Rotated Matrix:")
for row in result:
    print(*row)


#sample input and out put 
# Enter number of rows: 4
# Enter number of columns: 4
# Enter matrix values:
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# Enter k value: 2

# Rotated Matrix:
# 3 4 8 12
# 2 11 10 16
# 1 7 6 15
# 5 9 13 14