'''
347. Top K Frequent Elements
Medium

https://leetcode.com/problems/top-k-frequent-elements/
Given a non-empty array of integers, return the k most frequent elements.
'''
import heapq
import collections
class Solution:
    def topKFrequent(self, nums, k: int):
        # # 思路：字典计数后排序，排序时间复杂度大
        # ans = []
        # freqDict = {}
        # for x in nums:
        #     freqDict[x] = 1 if x not in freqDict else freqDict[x]+1
        # i = 0
        # for key in sorted(freqDict,key = freqDict.__getitem__,reverse=True):
        #     i += 1
        #     if i<=k:
        #         ans.append(key)
        # # # or
        # # output = sorted(freqDict.items(), key=lambda e: e[1], reverse=True)
        # # for i in range(k):
        # #     ans.append(output[i][0])
        #
        # return ans

        # # 思路：桶排序
        # data, res = {}, []
        # for i in nums:
        #     data[i] = data[i] + 1 if i in data else 1
        # # print(data)
        # bucket = [[] for _ in range(len(nums) + 1)]
        # for key in data:
        #     bucket[data[key]].append(key)
        # # print(bucket)
        # for i in range(len(bucket) - 1, -1, -1):
        #     if bucket[i]:
        #         res.extend(bucket[i])
        #     if len(res) >= k:
        #         break
        # return res[:k]

        # 思路：优先队列
        data, res, pq = {}, [], []
        for i in nums:
            data[i] = data[i] + 1 if i in data else 1
        for key in data:
            heapq.heappush(pq, (-data[key], key))   # 由于heapq默认是最小堆，代码中在堆的push时给权重加了负号，这样堆顶部对应的实际上是出现次数最多的数。
        for i in range(k):
            res.append(heapq.heappop(pq)[1])
        return res


        # # 思路：优先队列——堆 调库
        # count = collections.Counter(nums)   # O(N)
        # print(count)
        # return heapq.nlargest(k,count.keys(),key=count.get)   # O(Nlog(k))
        # # or
        # return [item[0] for item in counter.most_common(k)]

sol = Solution()
ans = sol.topKFrequent(nums = [1,1,1,2,3,3], k = 2)
print(ans)
# ans = sol.topKFrequent([1], 1)
# print(ans)
# ans = sol.topKFrequent([-1,-1], 1)
# print(ans)
# ans = sol.topKFrequent([1,2], 2)
# print(ans)
# 注意：不能使用字典倒置，因为字典的值对应的键可能不唯一