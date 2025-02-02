class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        i = 0
        check = True
        l = len(x)
        while i <= int(len(x)/2):
            first = x[i]
            last = x[l-i-1]
            if first != last:
                check = False
                break
            i += 1
        return check

palindrome_check = Solution().isPalindrome(121)
print(palindrome_check)
