'''
232. Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/

Implement the following operations of a queue using stacks.
push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
'''
from pythonds import Stack

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 初始化
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.items.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.stack2.isEmpty()!=True: #判断栈2是否为空
            return self.stack2.items.pop()
        else:
            if self.stack1.isEmpty()!=True:
                while self.stack1.size()!=1:
                    self.stack2.items.append(self.stack1.items.pop())
                return self.stack1.items.pop()
            else:
                if self.stack2.isEmpty() != True:
                    return self.stack2.items.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack2.isEmpty() != True:
            if len(self.stack2.items) >= 1:
                return self.stack2.items[len(self.stack2.items) - 1]
        else:
            if self.stack1.isEmpty() != True:
                return self.stack1.items[0]
            else:
                return False

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stack1.items == [] and self.stack2.items == []

    def size(self):
        return len(self.stack1.items)+len(self.stack2.items)

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(6)
print(obj.peek())
obj.push(7)
print(obj.peek())
obj.push(5)
param_1 = obj.pop()
obj.push(4)
param_2 = obj.pop()
param_3 = obj.pop()
print(obj.peek())
param_4 = obj.pop()
param_5 = obj.peek()
param_6 = obj.empty()
print(param_1,param_2,param_3,param_4,param_5,param_6)


#两个栈实现一个队列
#入队：元素进栈A
#出队：先判断栈B是否为空，为空则将栈A中的元素 pop 出来并 push 进栈B，再栈B出栈，如不为空则栈B直接出栈
#改进：
#入队：元素进栈A
#出队：先判断栈B是否为空，为空则将栈A中的n-1个元素 pop 出来并 push 进栈B，最先压入栈A的元素不pop再push到栈B，直接从栈A pop出栈，如不为空则栈B直接出栈
# 注意怎样把Queue的操作和Stack的操作联系起来