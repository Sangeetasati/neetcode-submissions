class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        max_l = 0
        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[i])
            max_l = max(max_l, len(char_set))
        return max_l
            

