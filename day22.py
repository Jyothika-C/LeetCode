def rotateTheBox(boxGrid):
    m, n = len(boxGrid), len(boxGrid[0])

    # Step 1: Apply gravity (stones fall to the right)
    for i in range(m):
        empty = n - 1
        for j in range(n - 1, -1, -1):
            if boxGrid[i][j] == '*':
                empty = j - 1
            elif boxGrid[i][j] == '#':
                boxGrid[i][j] = '.'
                boxGrid[i][empty] = '#'
                empty -= 1

    # Step 2: Rotate 90° clockwise
    result = [[None] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            result[j][m - 1 - i] = boxGrid[i][j]

    return result


# -------- User Input --------
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

print("Enter the grid row by row (use #, *, .):")
boxGrid = []
for i in range(m):
    row = input().split()
    boxGrid.append(row)

# Function call
result = rotateTheBox(boxGrid)

# Output
print("\nRotated Box:")
for row in result:
    print(" ".join(row))

# #sample input:
# Enter number of rows: 2
# Enter number of columns: 4
# Enter the grid row by row:
# # . * .
# # # * .

# #sample output
# # .
# # #
# * *
# . .