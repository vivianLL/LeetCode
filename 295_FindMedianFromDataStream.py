'''
295. Find Median from Data Stream
Hard

https://leetcode.com/problems/find-median-from-data-stream/
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
For example,
[2,3,4], the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5
Design a data structure that supports the following two operations:
void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
'''
from heapq import heappop, heappush

class MedianFinder:

    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.stream = []

    # 每加一个就排序一次 超时 时间O(nlogn) 空间O(n)
    # def addNum(self, num: int) -> None:
    #     self.stream.append(num)
    #     self.stream.sort()
    #
    # def findMedian(self) -> float:
    #     n = len(self.stream)
    #     if n % 2 == 1:
    #         return self.stream[n//2]
    #     else:
    #         return (self.stream[n//2]+self.stream[n//2-1])/2


    # # 插入排序 超时 始终保持数组有序并向有序数组中插入新数 时间O(n) 空间O(n)
    # def addNum(self, num: int) -> None:
    #     if self.stream == []:
    #         self.stream.append(num)
    #     else:
    #         i = 0
    #         if self.stream[0] >= num:   # 注意插入数和数组内数相等的情况，考虑全面
    #             self.stream = [num] + self.stream
    #         while self.stream[i] < num:
    #             if len(self.stream) - 1 == i:
    #                 self.stream.append(num)
    #                 break
    #             elif self.stream[i + 1] >= num:
    #                 self.stream = self.stream[:i + 1] + [num] + self.stream[i + 1:]
    #                 break
    #             else:
    #                 i += 1
    #     print(self.stream)
    #
    # def findMedian(self) -> float:
    #     n = len(self.stream)
    #     if n % 2 == 1:
    #         return self.stream[n//2]
    #     else:
    #         return (self.stream[n//2]+self.stream[n//2-1])/2

    # 最大堆和最小堆 时间O(logn) 空间O(n)
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = []   # 右边
        self.max = []     # 左边  最小堆中所有数字都大于最大堆中的数字
        self.median = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num <= self.median:
            if len(self.min) >= len(self.max):  # 两堆数目之差不大于1，若新数比中值小，且右堆比左堆数目大，新数往左堆中插
                heappush(self.max, -num)        # heapq默认最小堆，所以实现最大堆插入负值
            else:
                top = heappop(self.max)         # 新数据比最大堆中一些数据小，则将最大堆中最大的数字pop出来插入最小堆后，再将数据插入
                heappush(self.min, -top)
                heappush(self.max, -num)
        else:
            if len(self.max) >= len(self.min):
                heappush(self.min, num)
            else:
                top = heappop(self.min)
                heappush(self.max, -top)
                heappush(self.min, num)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.min) == len(self.max):
            self.median = float(self.min[0] + (-self.max[0])) / 2
        elif len(self.min) > len(self.max):
            self.median = self.min[0]
        else:
            self.median = -(self.max[0])

        return self.median


obj = MedianFinder()
obj.addNum(6)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(10)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(2)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(6)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(5)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(6)
param_2 = obj.findMedian()
print(param_2)