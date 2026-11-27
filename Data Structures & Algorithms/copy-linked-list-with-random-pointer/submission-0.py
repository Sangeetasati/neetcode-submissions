"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_nodes = {None: None}
        curr = head
        while curr:
            nxt = Node(curr.val)
            hash_nodes[curr] = nxt
            curr = curr.next

        curr = head
        while curr:
            copy = hash_nodes[curr]
            copy.next = hash_nodes[curr.next]
            copy.random = hash_nodes[curr.random]
            curr = curr.next

        return hash_nodes[head]
        






        