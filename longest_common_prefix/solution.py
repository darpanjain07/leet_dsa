from typing import List

class Solution:
    def min_length_list(self, strs):
        min_length = min(len(str) for str in strs)
        return min_length

    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = self.min_length_list(strs)
        i = 0
        common = ""
        while i <= min_length -1:
            common_element = ""
            for str in strs:
                str = str.strip()
                if len(str) == 0 and len(str) < 0 and len(str) > 200:
                    common = ""
                    return common
                if not common_element:
                    common_element = str[i]
                else:
                    if str[i] == common_element:
                        continue
                    else:
                        common_element = common_element[:-1]
                        break
            if not common_element:
                break
            else:
                common = common + common_element
            i += 1
        
        return common
    

input = ["dog","racecar","car"]
common_prefix = Solution().longestCommonPrefix(strs=input)
print(common_prefix)