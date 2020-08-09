# Definition for singly-linked list.
import sys
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return str(self.val) + " " + str(self.next)



def main():
    n1 = ListNode(1)
    n2 = ListNode(4)
    n3 = ListNode(5)

    n1.next = n2
    n2.next = n3

    n4 = ListNode(1)
    n5 = ListNode(3)
    n6 = ListNode(4)

    n4.next = n5
    n5.next = n6

    n7 = ListNode(2)
    n8 = ListNode(6)

    n7.next = n8

    l = [ n1, n4, n7]
    res = mergeKLists(l)
    print(res)

def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """


        lo = sys.maxsize
        n = None
        i = -1
        j = 0
        while j < len(lists):
            l = lists[j]
            if (l == None):
                lists.pop(j)
                if(i > j):
                    i -=1
                j -=1
            elif (l.val < lo):
                lo = l.val
                n = l
                i = j
            j +=1

        if(n != None):
            current.next = ListNode(n.val)
            current = current.next
            lists[i] = lists[i].next

    return head.next


main()
