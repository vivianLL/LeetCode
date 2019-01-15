'''
225. Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/

Implement the following operations of a stack using queues.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
'''
# 注意：在LeetCode中提交没有pythonds库，需要手动加上Queue类
from pythonds import Queue

# 自己写的
# class MyStack:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.queue1 = Queue()
#         self.queue2 = Queue()
#
#     def push(self, x):
#         """
#         Push element x onto stack.
#         :type x: int
#         :rtype: void
#         """
#         if self.queue1.size() >= 1:
#             self.queue2.enqueue(self.queue1.dequeue())  # 注意这里应是入队而不应该是append
#         self.queue1.enqueue(x)   # 注意这里应是入队而不应该是append
#         print(self.queue1.items,self.queue2.items)
#
#
#     def pop(self):
#         """
#         Removes the element on top of the stack and returns that element.
#         :rtype: int
#         """
#         if self.queue1.size() == 1:
#             return self.queue1.dequeue()
#         elif self.queue1.size() > 1:
#             self.queue2.enqueue(self.queue1.dequeue())
#             return self.queue1.dequeue()
#         else:
#             while self.queue2.size() > 1:
#                 print("pop", self.queue1.items, self.queue2.items)
#                 self.queue1.enqueue(self.queue2.dequeue())
#                 print("pop",self.queue1.items, self.queue2.items)
#             return self.queue2.dequeue()
#
#
#     def top(self):
#         """
#         Get the top element.
#         :rtype: int
#         """
#         if self.queue1.isEmpty() != True:
#             if len(self.queue1.items) >= 1:
#                 return self.queue1.items[len(self.queue1.items) - 1]
#         else:
#             if self.queue2.isEmpty() != True:
#                 return self.queue2.items[0]
#             else:
#                 return False
#
#
#     def empty(self):
#         """
#         Returns whether the stack is empty.
#         :rtype: bool
#         """
#         return self.queue1.items == [] and self.queue2.items == []
#
#     def size(self):
#         return len(self.queue1.items)+len(self.queue2.items)

# 别人写的
class MyStack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        if self.q1:
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))
            return self.q1.pop(0)
        elif not self.q1 and self.q2:
            self.q1, self.q2 = self.q2, self.q1
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))
            return self.q1.pop(0)

    def top(self):
        if self.q1:
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))
            return self.q1[0]
        else:
            self.q1, self.q2 = self.q2, self.q1
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))
            return self.q1[0]

    def empty(self):
        return not self.q1 and not self.q2

# Your MyStack object will be instantiated and called as such:
# obj = Queue()
# obj.enqueue(6)
# obj.enqueue(7)
# obj.enqueue(5)
# print(obj.items)  #[5, 7, 6]
# param_1 = obj.dequeue()
# obj.enqueue(4)
# param_2 = obj.dequeue()
# param_3 = obj.dequeue()
# param_4 = obj.dequeue()
# print(param_1,param_2,param_3,param_4) #6 7 5 4

obj = MyStack()
obj.push(1)

obj.push(2)

obj.push(3)

param_1 = obj.top()


param_2 = obj.pop()
param_3 = obj.top()
print(param_3)
# param_4 = obj.pop()
# param_5 = obj.top()
# param_6 = obj.empty()
# param_7 = obj.pop()
# param_8 = obj.empty()
# print(param_1,param_2,param_3,param_4,param_5,param_6,param_7,param_8)

