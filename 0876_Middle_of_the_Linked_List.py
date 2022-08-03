import pytest
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    temp = head
    count = 0
    while temp.next is not None:
        count += 1
        temp = temp.next

    if count%2 == 0:
        mid = int(count/2)
    else:
        mid = int((count-1)/2) + 1

    for i in range(mid):
        head = head.next

    return head

if __name__ == "__main__":
    head = [1,2,3,4,5,6]
    res = middleNode(head)
    print(f"input {string} output {string}", head, res)