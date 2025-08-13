class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        p = sorted(p)
        pp = len(p)
        for i in range((len(s)-pp)+1):
            if len(s[i: (i + pp)]) == pp and sorted(s[i: (i + pp)]) == p:
                ans.append(i)
        return ans