from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx +=1
            
        return idx


idx = Solution().removeElement(nums=[0,1,2,2,3,0,4,2], val=2)
print(idx)
