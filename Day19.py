class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in (s + s)

# User Input
s = input("Enter string s: ")
goal = input("Enter goal string: ")

sol = Solution()
result = sol.rotateString(s, goal)

print("Output:", result)

#sample  input
# Enter string s: abcde
# Enter goal string: cdeab
# sample output:
# Output: True
