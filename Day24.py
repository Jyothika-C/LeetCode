from collections import deque, defaultdict
from math import isqrt


class Solution:
    def minJumps(self, nums):
        n = len(nums)

        # Check prime
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, isqrt(x) + 1):
                if x % i == 0:
                    return False
            return True

        # Find prime factors
        def prime_factors(x):
            factors = set()
            d = 2
            while d * d <= x:
                while x % d == 0:
                    factors.add(d)
                    x //= d
                d += 1
            if x > 1:
                factors.add(x)
            return factors

        # Store indices divisible by prime
        divisible = defaultdict(list)

        for i, num in enumerate(nums):
            for p in prime_factors(num):
                divisible[p].append(i)

        # BFS
        q = deque([(0, 0)])
        visited = [False] * n
        visited[0] = True

        used_prime = set()

        while q:
            i, steps = q.popleft()

            if i == n - 1:
                return steps

            # Adjacent moves
            for nxt in [i - 1, i + 1]:
                if 0 <= nxt < n and not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, steps + 1))

            # Prime teleportation
            if is_prime(nums[i]) and nums[i] not in used_prime:
                p = nums[i]

                for nxt in divisible[p]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append((nxt, steps + 1))

                used_prime.add(p)

        return -1


# User Input
n = int(input("Enter size of array: "))
nums = list(map(int, input("Enter array elements: ").split()))

obj = Solution()
print("Minimum jumps required:", obj.minJumps(nums))

# Sample Input
# Enter size of array: 4
# Enter array elements: 1 2 4 6
# Sample Output
# Minimum jumps required: 2