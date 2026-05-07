class Solution:
    def maxValue(self, nums):
        n = len(nums)

        # suffix minimum array
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        ans = [0] * n

        start = 0
        current_max = nums[0]
        component_max = nums[0]

        for i in range(n - 1):
            current_max = max(current_max, nums[i])
            component_max = max(component_max, nums[i])

            # End of connected component
            if current_max < suffix_min[i + 1]:

                for j in range(start, i + 1):
                    ans[j] = component_max

                start = i + 1
                current_max = nums[start]
                component_max = nums[start]

        # Fill remaining component
        component_max = max(nums[start:])

        for j in range(start, n):
            ans[j] = component_max

        return ans


# User Input
nums = list(map(int, input("Enter array elements: ").split()))

sol = Solution()
result = sol.maxValue(nums)

print("Maximum reachable values:", result)


# #sample input
# 2 3 1
# #sample output
# Maximum reachable values: [3, 3, 3]