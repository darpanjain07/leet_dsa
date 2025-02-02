import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        normal = x
        rev = 0
        c = (len(str(x)) - 1)
        while x > 0:
            t = x % 10
            rev = int(rev + (math.pow(10, c) * t))
            c -=1
            x = int(x/10)
        if normal == rev:
            return True
        else:
            return False


palindrome_check = Solution().isPalindrome(123421)
print(palindrome_check)
