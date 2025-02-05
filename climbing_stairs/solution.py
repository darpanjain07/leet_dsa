class Solution:
    def climbStairs(self, n: int) -> int:
        if (n > 45) or (n<1):
            return 
        step1 = 1
        step2 = 1
        for i in range(2, n+1):
            curr = step1 + step2
            step2 = step1
            step1 = curr
        return step1

input = 4
output = Solution().climbStairs(n=input)
print(output)