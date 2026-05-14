def isGood(nums):
    n = max(nums)

    # Length must be n + 1
    if len(nums) != n + 1:
        return False

    nums.sort()

    # Check numbers from 1 to n-1
    for i in range(1, n):
        if nums[i - 1] != i:
            return False

    # Last two elements must be n
    return nums[-1] == n and nums[-2] == n


# User Input
nums = list(map(int, input("Enter array elements: ").split()))

# Function Call
print(isGood(nums))

#sample input and output 

# Sample Input 
# 1 3 3 2
# Sample Output 
# True