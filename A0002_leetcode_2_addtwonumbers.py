# Reference 
# https://github.com/kamyu104/LeetCode/blob/master/Python/add-two-numbers.py
# Time: O(n)
# Space: O(1)


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = ListNode(0)
        current, carry = temp, 0

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            carry = val // 10
            val = val % 10

            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(1)

        return temp.next


if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    s = Solution().addTwoNumbers(a, b)
    print(s.val, s.next.val, s.next.next.val)
