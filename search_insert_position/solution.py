from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = 0
        for i in range(len(nums)):
            if target > nums[-1]:
                idx = len(nums)
                break
            elif nums[i] >= target:
                idx = i
                break
        return idx

i = Solution().searchInsert(nums=[1,3,5,6], target=5)
print(i)
