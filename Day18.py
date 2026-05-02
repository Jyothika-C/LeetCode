class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        
        for num in range(1, n + 1):
            valid = True
            changed = False
            
            for ch in str(num):
                if ch in ['3', '4', '7']:
                    valid = False
                    break
                if ch in ['2', '5', '6', '9']:
                    changed = True
            
            if valid and changed:
                count += 1
        
        return count


# User Input
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    sol = Solution()
    result = sol.rotatedDigits(n)
    print("Number of good integers:", result)
    

# sample input and output
# Enter a number: 10
# Number of good integers: 4