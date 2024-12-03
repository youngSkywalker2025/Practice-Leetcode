class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_frequency_linked_list(head):
    # Step 1: Count frequencies using a dictionary
    freq = {}
    current = head
    while current:
        # Start at the head of linked list and check if its value is already in the freq dictionary
        freq[current.val] = freq.get(current.val, 0) + 1 # 'retrieve the current count for the value ( 0 returned if is not yet in dictionary +1 increase its frequency count in freq dictionary) '
        current = current.next

    # Step 2: Create a new linked list for the frequency counts
    dummy = ListNode(0) # common convention
    tail = dummy
    for count in freq.values(): # returns a view object that contains all the values in the freq dictionary
        tail.next = ListNode(count)
        tail = tail.next

    # Step 3: Return the head of the new linked list
    return dummy.next

'''

repeating elements linked list 
find unique values insert into hash table as key and count as frequency 
create a new linked list from the hash map 
'''