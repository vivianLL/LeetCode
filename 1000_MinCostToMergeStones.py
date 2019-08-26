'''
1000. Minimum Cost to Merge Stones
Hard

https://leetcode.com/problems/minimum-cost-to-merge-stones/
There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.
A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these K piles.
Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.
'''
class Solution:
    def mergeStones(self, stones, K):
        # # 法一
        # n = len(stones)
        # inf = float('inf')
        # prefix = [0] * (n + 1)
        # for i in range(n):
        #     prefix[i + 1] = prefix[i] + stones[i]
        #
        # import functools
        #
        # @functools.lru_cache(None)   # 将函数或类方法的结果缓存住，后续调用则直接返回缓存的结果。如果不加这两句则会超时
        # def dp(i, j, m):
        #     if (j - i + 1 - m) % (K - 1):
        #         return inf
        #     if i == j:
        #         return 0 if m == 1 else inf
        #     if m == 1:
        #         return dp(i, j, K) + prefix[j + 1] - prefix[i]
        #     return min(dp(i, mid, 1) + dp(mid + 1, j, m - 1) for mid in range(i, j, K - 1))
        #
        # res = dp(0, n - 1, 1)
        # return res if res < inf else -1

        n = len(stones)
        if n == 1: return 0
        if n < K: return -1
        if (n - K) % (K - 1): return -1

        inf = float('inf')
        memo = {}   # 相当于用memo来缓存

        def dp(i, j, m):
            if (i, j, m) in memo: return memo[(i, j, m)]
            if i == j:
                res = 0 if m == 1 else inf
                memo[(i, j, m)] = res
                return res

            if m == 1:
                res = dp(i, j, K) + sum(stones[i:j + 1])
            else:
                res = inf
                for mid in range(i, j, K - 1):  # length must be K+n*(K-1)
                    res = min(res, dp(i, mid, 1) + dp(mid + 1, j, m - 1))
            memo[(i, j, m)] = res
            return res

        res = dp(0, n - 1, 1)
        return res if res < inf else -1




sol = Solution()
ans = sol.mergeStones([3,5,1,2,6],3)
print(ans)
# 思路：https://blog.csdn.net/vivian_ll/article/details/100077000