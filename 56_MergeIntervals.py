'''
56. Merge Intervals
Medium

https://leetcode.com/problems/merge-intervals/
Given a collection of intervals, merge all overlapping intervals.
'''
class Solution:
    def merge(self, intervals):
        # # 先排序 自己写的
        # if len(intervals)==0 or len(intervals)==1:
        #     return intervals
        # intervals = sorted(intervals,key=lambda x:x[0])
        # # print(intervals)
        # newlist = []
        # temp = intervals[0]
        # for i in range(1,len(intervals)):
        #     if temp[1]>=intervals[i][0]:
        #         # if i != 1:
        #         #     newlist.append(intervals[i - 1])
        #         temp = [temp[0],max(temp[1],intervals[i][1])]
        #         # print(temp)
        #     else:
        #         newlist.append(temp)
        #         temp = intervals[i]
        #     # print(newlist)
        # newlist.append(temp)
        # return newlist

        # 排序 官网简洁写法
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


sol = Solution()
ans = sol.merge([[2,3],[4,5],[6,7],[8,9],[1,10]])
print(ans)
ans = sol.merge([[0,1],[2,4],[4,5]])
print(ans)
ans = sol.merge([[1,4],[0,4]])
print(ans)
ans = sol.merge([[1,4],[2,3]])
print(ans)
ans = sol.merge([[1,4],[0,2],[3,5]])
print(ans)
ans = sol.merge([])
print(ans)
ans = sol.merge([[]])
print(ans)
# 思路：官方solution还有一种构建图的方法，没太懂，且复杂度高