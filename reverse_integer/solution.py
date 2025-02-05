import math

class Solution:
    def reverse(self, x: int) -> int:

        # if (x > math.pow(-2, 31)) or (x < (math.pow(2, 31)-1)):
        #     return 0

        len_no = len(str(x)) -1
        rev = 0
        y = 0
        if x<0:
            len_no = len(str(x)) - 2
            y = x
            x = x * (-1)
        while x > 0:
            d = (x%10)
            rev = rev + (d * math.pow(10,len_no))
            x = int(x/10)
            len_no -= 1

        if y != 0:
            rev = rev * (-1)

        if (rev < math.pow(-2, 31)) or (rev > (math.pow(2, 31)-1)):
            return 0

        return int(rev)

input = 123
output = Solution().reverse(x=input)
print(output)