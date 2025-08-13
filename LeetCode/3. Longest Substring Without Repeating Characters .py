class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            temp = ''
            for j in range(i,len(s)):
                if s[j] in temp:
                    break
                else:
                    temp += s[j]
            if ans <= len(temp):
                ans = len(temp)
        return ans