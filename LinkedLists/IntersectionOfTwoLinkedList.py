'''
Adjusting Starting Points: move head of longer list forward so both lists are equally far from the end.
The end because both lists end intersecting ( thing of like a sideways steak fork )

move pointer of longer list forward until same length as smaller list
Then check for shared nodes by reference

What if problem was Arrays instead of linked list?
* this problem would be like identifying the first common subarray (sequence of elements with identfical values)
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length


def getIntersectionNode(headA, headB):
    lenA, lenB = get_length(headA), get_length(headB)

    # Adjust starting points
    while lenA > lenB:
        headA = headA.next
        lenA -= 1
    while lenB > lenA:
        headB = headB.next
        lenB -= 1

    # Traverse and find the intersection
    # check for shared nodes by reference
    while headA != headB:
        headA = headA.next
        headB = headB.next






'''

get lengths
adjust length of the longer list
traverse lists and find intersection 
'''