class Solution:
    def longestOnes(self, n: List[int], k: int) -> int:
        l = z = ans = 0
        for r in range(len(n)):
            if n[r] == 0:
                z += 1
            while k < z:
                if n[l] == 0:
                    z -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans
