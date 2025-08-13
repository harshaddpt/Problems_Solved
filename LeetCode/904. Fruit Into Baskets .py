class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        f = {}
        l = 0
        ans = 0
        for i in range(len(fruits)):
            if fruits[i] in f:
                f[fruits[i]] += 1
            else:
                f[fruits[i]] = 1
            while len(f) > 2:
                first = fruits[l]
                f[first] -= 1
                if f[first] == 0:
                    del f[first]
                l += 1
            ans = max(ans, i-l+1)
        return ans
