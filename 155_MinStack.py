'''
155. Min Stack
Easy

https://leetcode.com/problems/min-stack/
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''


class MinStack:

    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.stack = []
    #
    # def push(self, x: int) -> None:
    #     self.stack.append(x)
    #
    #
    # def pop(self) -> None:
    #     return self.stack.pop()
    #
    # def top(self) -> int:
    #     return self.stack[-1]
    #
    # def getMin(self) -> int:
    #     return sorted(self.stack)[0]
    # # 或    return min(self.l)

    def __init__(self):
        self.stack = []
        self.minimum = []   # 按顺序存放当前的最小值

    def push(self, x):
        self.stack.append(x)
        try:
            oldMin = self.minimum[-1]
            if x < oldMin:
                self.minimum.append(x)
            else:
                self.minimum.append(oldMin)
        except:
            self.minimum.append(x)

    def pop(self):
        self.minimum.pop()
        return (self.stack.pop())

    def top(self):
        return (self.stack[-1])

    def getMin(self):
        return (self.minimum[-1])




minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  #-3
minStack.pop()
minStack.top()     #0
print(minStack.getMin())