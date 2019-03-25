'''
55. Jump Game
Medium

https://leetcode.com/problems/jump-game/
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
'''
class Solution:
    def canJump(self, nums) -> bool:
        # 回溯法
        if nums == []:
            return False
        # 初始last是最后一个节点
        last = len(nums) - 1
        # 这里其实初始化为len(nums)-2,-1,-1 ，return last<=0,也是可以的，从倒数第二个节点开始判断是否可达倒数第一个节点，
        # 但是从len(nums) - 1, -1, -1虽然冗余一次但是健壮性更好，譬如len(nums)=1时，1-2 = -1 不好
        # 虽然提交了也AC了但是显然不健壮
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last:
                last = i
        return last == 0


# 思路：算法：贪心2-逆向思维
#             反过来思考整个跳跃的过程，如果能从某一个节点跳跃到达最后一个节点，那么从最后一个节点回看，一定能
#         到达第一个初始节点。
#     思路：
#         如果有一条路径A->B->C->D->FINAL，即最后到达FINAL，那么从FINAL开始向前看，若D是能到达FINAL的，
#         那么前面的位置只要能到达D就是到达FINAL的充分条件了，能到达D则一定能到达FINAL，倒着来看！
#         所以倒着遍历数组，设置一个last位置为最后一个需要被前面位置可达的位置，从最后一个位置开始，last = FINAL，
#         判断它的前一个节点pre的可达位置是否包括last位置，如果包括，即pre+nums[pre] >= last的话，就说明该pre节
#         点可达last，更新last = pre，继续向后判断，看后面的节点可否达当前last，依次循环遍历，直到最后判断last == 0
#         即最后一个需要可达的位置为初始节点

# 参考网址：https://blog.csdn.net/qq_28327765/article/details/84434412