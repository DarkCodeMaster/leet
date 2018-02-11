# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i = 0
        num1 = 0
        while l1 != None:
            x = (l1.val*(10**i))
            num1 += x
            i += 1
            l1 = l1.next
        print(num1)
        j = 0
        num2 = 0
        while l2 != None:
            y = (l2.val*(10**j))
            num2 += y
            j += 1
            l2 = l2.next
        print(num2)
        result = str(num1 + num2)
        l3 = ListNode(0)
        scan = l3
        for x in result[:0:-1]:
            temp = ListNode(None)
            scan.val = int(x)
            scan.next = temp
            scan = scan.next
        scan.val = int(result[0])
        return l3
