'''
82. Remove Duplicates from Sorted List II

https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicatesII(self, head: ListNode) -> ListNode:
        # 在83题的基础上加上一个指向当前结点前一个结点的指针
        # 参考网址：https://blog.csdn.net/qq_17550379/article/details/80668036
        h = ListNode(-1)
        h.next = head
        pre = h
        cur = head
        while cur != None:
            duplicate = False
            while cur.next != None and cur.val == cur.next.val:  # 遇到重复结点先别急着删除，继续向下遍历直到不重复为止
                cur = cur.next
                duplicate = True

            if duplicate == False:  # 当没有重复时再移动pre结点，有重复时pre先不动，找到最后一个重复结点再动
                pre = cur
            else:
                pre.next = cur.next

            cur = cur.next

        return h.next

        # 遍历head节点，如果出现存在两个相同节点时，就进入if循环过滤到这些相同的节点，如果不存在，就让新节点指向那个节点
        # 参考网址：https://blog.csdn.net/Sun_White_Boy/article/details/82855767
        head2 = ListNode(0)
        p = head2

        while head:
            if head.next and head.next.val == head.val:
                val = head.val
                while head and head.val == val:
                    head = head.next
                # 这一步是防止链表尾全部相同时，新链表尾节点的next不为空
                p.next = head
            else:
                p.next = head
                p = head
                head = head.next
        return head2.next

        # 遍历一遍，生成一个哈希表，生成一个不重复的顺序表，然后通过遍历顺序表，判断该数在哈希表中的值组成新链表
        # 顺序表
        only_list = []
        # 哈希表
        only_dict = {}

        # 新头节点
        head2 = ListNode(0)
        p = head2
        while head:
            if head.val in only_dict:
                only_dict[head.val] += 1
            else:
                only_list.append(head.val)
                only_dict[head.val] = 1
            head = head.next
        for i in only_list:
            if only_dict[i] == 1:
                new = ListNode(i)
                p.next = new
                p = p.next
        return head2.next


lNode0=ListNode(0)
lNode1=ListNode(1)
lNode2=ListNode(2)
lNode3=ListNode(3)
lNode4=ListNode(4)
lNode5=ListNode(5)
lNode0.next=lNode1
lNode1.next=lNode2
lNode2.next=lNode3
lNode3.next=lNode4
lNode4.next=lNode5
sol = Solution()
head = sol.deleteDuplicatesII(lNode0)
while head.next:
    print(head.val)
    head = head.next

# 思路：在83题的基础上记录当前结点的前一个结点
# 注意删除头结点的情况和多个（奇数个）重复结点的问题