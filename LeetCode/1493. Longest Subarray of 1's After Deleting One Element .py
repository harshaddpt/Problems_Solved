class Solution:
    def longestSubarray(self, n: List[int]) -> int:
        l = z = ans = 0
        for r in range(len(n)):
            if n[r] == 0:
                z += 1
            while 1 < z:
                if n[l] == 0:
                    z -= 1
                l += 1
            ans = max(ans, r-l+1)
        if n.count(1) == len(n):
            return len(n)-1
        elif n.count(0) == len(n):
            return 0
        return ans-1
