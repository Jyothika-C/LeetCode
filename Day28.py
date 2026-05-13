def minMoves(nums, limit):
    n = len(nums)

    diff = [0] * (2 * limit + 2)

    for i in range(n // 2):
        a = nums[i]
        b = nums[n - 1 - i]

        low = min(a, b) + 1
        high = max(a, b) + limit
        s = a + b

        # Assume 2 moves for all sums
        diff[2] += 2

        # Reduce to 1 move range
        diff[low] -= 1
        diff[high + 1] += 1

        # Reduce to 0 move for exact sum
        diff[s] -= 1
        diff[s + 1] += 1

    ans = float('inf')
    curr = 0

    for x in range(2, 2 * limit + 1):
        curr += diff[x]
        ans = min(ans, curr)

    return ans


# User Input
n = int(input("Enter size of array: "))
nums = list(map(int, input("Enter array elements: ").split()))
limit = int(input("Enter limit: "))

print("Minimum moves required:", minMoves(nums, limit))


#sample input and out put
# Sample Input
# Enter size of array: 4
# Enter array elements: 1 2 4 3
# Enter limit: 4
# Sample Output
# Minimum moves required: 1