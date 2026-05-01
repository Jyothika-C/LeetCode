def maxRotateFunction(nums):
    n = len(nums)
    total_sum = sum(nums)
    
    # Compute F(0)
    f = 0
    for i in range(n):
        f += i * nums[i]
    
    max_val = f
    
    # Compute F(1) to F(n-1)
    for k in range(1, n):
        f = f + total_sum - n * nums[n - k]
        max_val = max(max_val, f)
    
    return max_val


# -------- USER INPUT --------
nums = list(map(int, input("Enter numbers separated by space: ").split()))

result = maxRotateFunction(nums)
print("Maximum Rotate Function Value:", result)

# Input:

# Enter numbers separated by space: 4 3 2 6

# Output:

# Maximum Rotate Function Value: 26