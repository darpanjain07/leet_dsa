class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        last_space_index = s.rfind(' ')
        last_word_length = len(s[(last_space_index+1):])
        return last_word_length


input = "luffy is still joyboy"
output = Solution().lengthOfLastWord(s=input)
print(output)